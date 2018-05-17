# Code Challenge for Shutterfly

# Introduction
This project is to ingest event data and implement analytic method:

execute file: ./src/main.py

definition file: ./src/events.py

input file: ./input/input.txt

sample input file: ./sample_input/input.txt

output file: ./output/output.txt    


# Programming Language
This project is implemented in Python3. 

# Dependancies 
* sys  -> to get input file path and top x arguments from user
* json -> to convert the text file content into in-memory dictionary 
* operator -> to sort the dictionary by its value()

# Execution:
Execute with Python3

To execute this program, please run below command.

> python ./src/main.py 10 ./input/input.txt

format: python execute_file  [arg1]x [arg2]input_path
x: the first parameter for TopXSimpleLTVCustomers(x, D), default = 10
input.txt: the file path for ingestion, default = './input/input.txt'


# Data structure
This project used python dictionary to store the data.
rootList is the dictionary that store all four-type events information.
The four events: customer, visit, image, order are stored as key in rootList, their values are dictionaries.
Definition of rootList:

>    rootList = {}
>    rootList['customer'] = {}
>    rootList['visit'] = {}
>    rootList['image'] = {}
>    rootList['order'] = {}


# Process flow
Step1. load file into python object - data

Step2. ingest data into in-memory dictionary - rootList

Step3. print dictionary rootList

Step4. calculate TopXSimpleLTVCustomers

Step5. write result of step4 into output file.


