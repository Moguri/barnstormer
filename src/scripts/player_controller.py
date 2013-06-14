from bge import logic, events
from mathutils import Vector, Matrix

import math
import time

class PlayerController:
	DYAW = math.radians(1.0)
	DPITCH = math.radians(1.0)
	IDLE_THROTTLE = 0.25
	MAX_THROTTLE = 0.35
	TICK_RATE = 1/60  # Expected tic rate

	def __init__(self, ob):
		self.obj = ob
		self.last_update = time.time()
		print("Attaching player controller to", ob)

	def run(self):
		# Default values
		throttle = self.IDLE_THROTTLE
		yaw = 0
		pitch = 0

		dt = time.time() - self.last_update
		dtscale = dt / self.TICK_RATE

		# Get input
		for keycode, status in logic.keyboard.active_events.items():
			if keycode == events.SPACEKEY:
				throttle = self.MAX_THROTTLE
			elif keycode == events.LEFTARROWKEY:
				yaw += self.DYAW
			elif keycode == events.RIGHTARROWKEY:
				yaw -= self.DYAW
			elif keycode == events.UPARROWKEY:
				pitch += self.DPITCH
			elif keycode == events.DOWNARROWKEY:
				pitch -= self.DPITCH

		# Adjust pitch (local x)
		transform = Matrix.Rotation(pitch * dtscale, 4, 'X')

		# Adjust yaw (local z)
		transform = Matrix.Rotation(yaw * dtscale, 4, 'Z') * transform

		# Move forward (down the local -y)
		transform = Matrix.Translation((0, -throttle * dtscale, 0)) * transform

		self.obj.localTransform = self.obj.localTransform * transform

		# Roll correction
		if yaw == 0:
			error = 0 - self.obj.localOrientation.to_euler()[1]
			#print(error)
			self.obj.applyRotation((0, error*0.03*dtscale, 0), True)

		self.last_update = time.time()

def main(cont):
	ob = cont.owner

	try:
		ob['pc'].run()
	except KeyError:
		ob['pc'] = PlayerController(ob)
		
