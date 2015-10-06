from papukaaniApp.services.lajistore_service import LajiStoreAPI

class Device():

	def __init__(self, id, deviceId, deviceType, deviceManufacturer, createdAt, createdBy, lastModifiedAt, lastModifiedBy, facts, **kwargs):
		self.id = id		
		self.deviceId = deviceId
		self.deviceType = deviceType
		self.deviceManufacturer = deviceManufacturer
		self.createdAt = createdAt
		self.createdBy = createdBy
		self.lastModifiedAt = lastModifiedAt
		self.lastModifiedBy = lastModifiedBy
		self.facts = facts

	def delete(self):
		LajiStoreAPI.delete_device(self.id)

	def update(self):
		LajiStoreAPI.update_device(**self.__dict__) #__dict__ puts all arguments here

def find(**kwargs):
	return _get_many(**kwargs)

def get_all():
	return _get_many()

def get(deviceId):
	device = LajiStoreAPI.get_device(deviceId)
	return Device(**device)

def create(deviceId, deviceType, deviceManufacturer, createdAt, createdBy, lastModifiedAt, lastModifiedBy, facts):
	device = LajiStoreAPI.post_device(deviceId, deviceType, deviceManufacturer, createdAt, createdBy, lastModifiedAt, lastModifiedBy, facts)
	return Device(**device)

def _get_many(**kwargs):
	data = LajiStoreAPI.get_all_devices(**kwargs)
	devices = []
	for device in data:	#creates a list of devices to return
		devices.append(Device(**device))
	return devices



