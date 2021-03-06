from bge import logic
import aud


class Collectable:
	def __init__(self, obj, sensor):
		self.obj = obj
		self.sensor = sensor

		try:
			logic.globalDict['collectables'] += 1
		except KeyError:
			logic.globalDict['collectables'] = 1

		print("Num collectables", logic.globalDict['collectables'])

	def run(self):
		if self.sensor.positive:
			print("HIT!")
			logic.globalDict['collectables'] -= 1
			aud.device().play(aud.Factory(logic.expandPath("//../sounds/completetask_0.mp3")))
			self.obj.endObject()


def main(cont):
	ob = cont.owner

	try:
		ob['class'].run()
	except KeyError:
		sensor = cont.sensors['Collision']
		ob['class'] = Collectable(ob, sensor)