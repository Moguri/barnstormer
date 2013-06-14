from bge import logic, events
from mathutils import Vector, Matrix
import aud

import math
import time

class PlayerController:
	DYAW = math.radians(1.0)
	DPITCH = math.radians(1.0)
	MAX_BANK = math.radians(40.0)
	IDLE_THROTTLE = 0.25
	MAX_THROTTLE = 0.35
	TICK_RATE = 1/60  # Expected tic rate

	def __init__(self, ob):
		self.obj = ob
		self.last_update = self.start_time = time.time()
		self.end_time = None
		print("Attaching player controller to", ob)

		self.engine_sound = aud.device().play(aud.Factory(logic.expandPath("//../sounds/engine.ogg")).loop(-1))
		self.bg_music = aud.device().play(aud.Factory(logic.expandPath("//../sounds/Circus Waltz FX.ogg")).loop(-1))

	def __del__(self):
		print("Destroying sound handles")
		self.engine_sound.stop()
		self.bg_music.stop()

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
		roll = self.obj.localOrientation.to_euler()[1]
		if yaw == 0:
			error = 0 - roll
		elif yaw < 0:
			error = -self.MAX_BANK - roll
		else:
			error = self.MAX_BANK - roll
		self.obj.applyRotation((0, error*0.03*dtscale, 0), True)

		# Alter the pitch of the engine noise based on throttle
		if throttle == self.MAX_THROTTLE:
			self.engine_sound.pitch = 1.5
		else:
			self.engine_sound.pitch = 1

		# Check how many collectables we have left
		if not self.end_time and logic.globalDict['collectables'] <= 0:
			self.end_time = time.time() - self.start_time
			print("All collectables gathered in %f seconds!" % self.end_time)

		self.last_update = time.time()

def main(cont):
	ob = cont.owner

	try:
		ob['pc'].run()
	except KeyError:
		ob['pc'] = PlayerController(ob)
		
