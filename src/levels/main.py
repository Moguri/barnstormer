import sys
import os


from bge import logic


def update_path():
	if ".." not in sys.path:
		sys.path.append("..")
		os.chdir(logic.expandPath("//"))


def init():
	update_path()


def level_select(cont):
	init()
	logic.startGame(logic.expandPath("//free_roam.blend"))


def free_roam(cont):
	init()
