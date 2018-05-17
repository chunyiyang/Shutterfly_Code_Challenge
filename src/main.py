import json
import sys 
import operator
from datetime import datetime
from events import Customer
from events import Visit
from events import Image
from events import Order


def updateCustomer(e, D):
    """
    Update customer data information
    input:
    e: event
    D: data(in-memory dictionary)
    no return value, only update in-memory dictionary
    """
    for key, value in e.items():
        if value != None:
            D['customer'][e['key']].__dict__[key] = value

def updateOrder(e, D):
    """
    Update order data information
    input:
    e: event
    D: data(in-memory dictionary)
    no return value, only update in-memory dictionary
    """
    for key, value in e.items():
        if value != None:
            D['order'][e['key']].__dict__[key] = value

def updateVisit(e, D):
    """
    Update visit data information
    input:
    e: event
    D: data(in-memory dictionary)
    no return value, only update in-memory dictionary
    """
    for key, value in e.items():
    	print (e['key'])
    	print (key, value)
    	if value != None:
        	D['visit'][e['key']].__dict__[key] = value

def updateImage(e, D):
    """
    Update visit data information
    input:
    e: event
    D: data(in-memory dictionary)
    no return , only update in-memory dictionary
    """
    for key, value in e.items():
        if value != None:
            D['image'][e['key']].__dict__[key] = value


def load(path = "./input/input.txt"):
	"""
	convert the input text file into json format
	path: file path
	jsonData: list of data in json format
	"""
	file = open(path, 'r')
	data = file.read()
	jsonData = json.loads(data)
	return jsonData

def Ingest(e, D):
    if e['type'] == 'CUSTOMER':
        # if key is new, add this into dictionary, otherwise update object
        if e['key'] not in D['customer'].keys():
            D['customer'][e['key']] = Customer( e['type'], e['verb'], e['key'], e['event_time'], e['last_name'], e['adr_city'], e['adr_state'] )
        elif e['key'] in D['customer'].keys() and e['verb'] == 'UPDATE':
            updateCustomer( e, D )
    elif e['type'] == 'IMAGE':
        # if key is new, add this into dictionary, otherwise update object
        if e['key'] not in D['image'].keys():
            D['image'][e['key']] = Image( e['type'], e['verb'], e['key'], e['event_time'], e['customer_id'], e['camera_make'], e['camera_model'] )
        elif e['key'] in D['image'].keys():
            updateImage( e, D )
    elif e['type'] == 'ORDER':
        # if key is new, add this into dictionary, otherwise update object
        if e['key'] not in D['order'].keys():
            D['order'][e['key']] = Order( e['type'], e['verb'], e['key'], e['event_time'], e['customer_id'], e['total_amount'] )
        elif e['key'] in D['order'].keys() and e['verb'] == 'UPDATE':
            updateOrder( e, D )
    elif e['type'] == 'SITE_VISIT':
        # if key is new, add this into dictionary, otherwise update object
        if e['key'] not in D['visit'].keys():
            D['visit'][e['key']] = Visit( e['type'], e['verb'], e['key'], e['event_time'], e['customer_id'],e['tags'] )
        elif e['key'] in D['visit'].keys():
        	updateVisit(e, D)


def TopXSimpleLTVCustomers(x, D):
    """
    To calculate the top x highest LTV customers
    input:
    x: number of customers
    D: in-memory dictionary
    return:
    top customers id and LTV
    """
    res = dict()
    for cusId in D['customer'].keys():
        res[cusId] = calculateLTV(cusId, D)

    sorted_res = sorted(res.items(), key = operator.itemgetter(1), reverse=True)    

    size = min(len(sorted_res), x)

    with open("./output/output.txt","w") as output:
    	output.write("customer_id  calculateLTV \n")
    	for i in range(size):
            output.write(str(sorted_res[i][0]))
            output.write(' ')
            output.write(str(sorted_res[i][1]))
            output.write('\n')
    return sorted_res[:size]

def calculateLTV(cusId, D, t = 10):
    """
    For each customer_id, calculate the LTV
    input:
    cusId: customer_id
    D: in-memory dictionary
    t: life span
    return:
    ltv: calculated ltv(float type)
    """   
    expense = 0
    for v in D['order'].values():
    	if v.__dict__['customer_id'] == cusId:
    		total_amount = v.__dict__['total_amount']
    		tokens = total_amount.split(' ')
    		expense += float(tokens[0])

    lastVisit = convertWeek( max( v.__dict__['event_time'] for v in D['visit'].values() ) )
    firstVisit = convertWeek( min( v.__dict__['event_time'] for v in D['visit'].values() ) )
    weeks = (lastVisit[0] - firstVisit[0]) * 52 + (lastVisit[1] - firstVisit[1])
    # If time span is less than 1 week, use 1 week to calculate 
    a = expense
    # If time span is longer than 1 week, use real week number to calculate
    if weeks > 1:
    	a = expense / weeks
    ltv = 52 * a * t
    return ltv


def expensePerVisit(totalExpense, visitCount):
    """
    input:
    totalExpense: float
    visitCount: integer
    return:
    float
    """
    if not visitCount:
    	print( 'visitCount can not be 0, change visitCount to 1' )
    	visitCount = 1
    return totalExpense/visitCount

def visitPerWeek(visitCount, weekCount):
    """
    input:
    visitCount: integer
    totalExpense: integer
    return:
    float
    """
    if not weekCount:
    	print( 'weekCount can not be 0, change visitCount to 1' )
    	weekCount = 1
    return float(visitCount/weekCount)


def convertWeek(timestamp):
    """
    input:
    timestamp: datatime object (Ex: '2017-01-06T12:46:46.384Z')
    return:
    week (Ex: (2017, 1, 5))
    """
    if not timestamp:
        print( 'Please input correct time' )
        return None
    time = parseTimeStamp(timestamp)
    return time.isocalendar()

def parseTimeStamp(timestamp):
    """
    input:
    timestamp: string 
    return:datatime object
    """
    if not timestamp:
        print( "Please input correct time" )
        return None
    return datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%fZ')
            

def main(x = 10, path = "./input/input.txt"):
    rootList = {}
    rootList['customer'] = {}
    rootList['visit'] = {}
    rootList['image'] = {}
    rootList['order'] = {}
    data = load(path)
    for e in data:
        Ingest(e, rootList)
    print (rootList)
    TopXSimpleLTVCustomers(x, rootList)
    return rootList 

if __name__ == '__main__':
	argv = sys.argv
	if len(argv) <= 1:
		main()
	else:
		x = int(argv[1])
		inputPath = argv[2]	
		main(x, inputPath)