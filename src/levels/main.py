import sys
import os


from bge import logic


def init():
	sys.path.append("..")
	os.chdir(logic.expandPath("//"))

def level_select(cont):
	init()
	logic.startGame(logic.expandPath("//free_roam.blend"))


def free_roam(cont):
	init()
