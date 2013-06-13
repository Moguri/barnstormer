from bge import logic
import sys

def init():
	sys.path.append(".."),

def level_select(cont):
	init()
	logic.startGame(logic.expandPath("//free_roam.blend"))

def free_roam(cont):
	init()
