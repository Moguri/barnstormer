from bge import logic, events
from mathutils import Vector

class PlayerController:
	def __init__(self, ob):
		self.obj = ob
		print("Attaching player controller to", ob)

	def run(self):
		# Default values
		throttle = 1

		# Get input
		for keycode, status in logic.keyboard.active_events.items():
			if keycode == events.SPACEKEY:
				throttle = 2

		# Move forward (down the -y)
		self.obj.localPosition += Vector((0, -throttle, 0))

def main(cont):
	ob = cont.owner

	try:
		ob['pc'].run()
	except KeyError:
		ob['pc'] = PlayerController(ob)
		
