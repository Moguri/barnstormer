from bge import logic, events
from mathutils import Vector, Matrix

import math

class PlayerController:
	DYAW = math.radians(1.0)
	DPITCH = math.radian(1.0)

	def __init__(self, ob):
		self.obj = ob
		print("Attaching player controller to", ob)

	def run(self):
		# Default values
		throttle = 1
		yaw = 0
		pitch = 0

		# Get input
		for keycode, status in logic.keyboard.active_events.items():
			if keycode == events.SPACEKEY:
				throttle = 2
			elif keycode == events.LEFTARROWKEY:
				yaw -= self.DYAW
			elif keycode == events.RIGHTARROWKEY:
				yaw += self.DYAW
			elif keycode == events.UPARROWKEY:
				pitch += self.DPITCH
			elif keycode == events.DOWNARROWKEY:
				pitch -= self.DPITCH

		transform = self.obj.localTransform

		# Move forward (down the local -y)
		transform = Matrix.Translation((0, -throttle, 0)) * transform

		# Adjust yaw (local z)
		transform = Matrix.Rotation(yaw, 4, 'Z') * transform

		# Adjust pitch (

		self.obj.localTransform = transform

def main(cont):
	ob = cont.owner

	try:
		ob['pc'].run()
	except KeyError:
		ob['pc'] = PlayerController(ob)
		
