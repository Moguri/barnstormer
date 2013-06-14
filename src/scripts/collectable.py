from bge import logic


class Collectable:
	def __init__(self, obj, sensor):
		self.obj = obj
		self.sensor = sensor

	def run(self):
		if self.sensor.positive:
			print("HIT!")
			self.obj.endObject()


def main(cont):
	ob = cont.owner

	try:
		ob['class'].run()
	except KeyError:
		sensor = cont.sensors['Collision']
		ob['class'] = Collectable(ob, sensor)