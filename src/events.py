
class Customer(object):
	"""
	sample input:
	{"type": "CUSTOMER", 
	"verb": "NEW", 
	"key": "96f55c7d8f42", 
	"event_time": "2017-01-06T12:46:46.384Z", 
	"last_name": "Smith", 
	"adr_city": "Middletown", 
	"adr_state": "AK"}
	"""
	def __init__(self, type, verb, key, event_time, last_name = None, \
		adr_city = None, adr_state = None):
		self.type = type
		self.verb = verb
		self.key = key
		self.event_time = event_time
		self.last_name = last_name
		self.adr_city = adr_city
		self.adr_state = adr_state


class Visit(object):
	"""
	sample input:
	{"type": "SITE_VISIT", 
	"verb": "NEW", 
	"key": "ac05e815502f", 
	"event_time": "2017-01-06T12:45:52.041Z", 
	"customer_id": "96f55c7d8f42", 
	"tags": [{"some key": "some value"}]}
	"""
	def __init__(self, type, verb, key, event_time, customer_id, tags = None):
		self.type = type
		self.verb = verb
		self.key = key
		self.event_time = event_time
		self.customer_id = customer_id
		self.tags = tags

class Image(object):
	"""
	sample input:
	{"type": "IMAGE", 
	"verb": "UPLOAD", 
	"key": "d8ede43b1d9f", 
	"event_time": "2017-01-06T12:47:12.344Z", 
	"customer_id": "96f55c7d8f42", 
	"camera_make": "Canon", 
	"camera_model": "EOS 80D"}
	"""
	def __init__(self, type, verb, key, event_time, customer_id, camera_make = None, camera_model = None):
		self.type = type
		self.verb = verb
		self.key = key
		self.event_time = event_time
		self.customer_id = customer_id
		self.camera_make = camera_make
		self.camera_model = camera_model


class Order(object):
	"""
	{"type": "ORDER", 
	"verb": "NEW", 
	"key": "68d84e5d1a43", 
	"event_time": "2017-01-06T12:55:55.555Z", 
	"customer_id": "96f55c7d8f42", 
	"total_amount": "12.34 USD"}
	"""
	def __init__(self, type, verb, key, event_time, customer_id, total_amount):
		self.type = type
		self.verb = verb
		self.key = key
		self.event_time = event_time
		self.customer_id = customer_id
		self.total_amount = total_amount


