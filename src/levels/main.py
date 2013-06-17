import sys
import os


from bge import logic
from mathutils import Vector


def update_path():
	if ".." not in sys.path:
		sys.path.append("..")
		os.chdir(logic.expandPath("//"))


def init():
	update_path()

	# Do the import here so we know our path is good to go
	import bgui.bge
	logic.ui_system = bgui.bge.System()


def level_select(cont):
	try:
		logic.ui_system.run()
	except AttributeError:
		init()

		from scripts.layouts import LevelSelectLayout
		logic.ui_system.load_layout(LevelSelectLayout, None)


def free_roam(cont):
	init()
	
	
def five_stunt(cont):
	init()
	
	scene = logic.getCurrentScene()
	with open("fivestunt.data", "r") as fin:
		for item in fin.readlines():
			floats = [float(i) for i in item.split(',')]
			newob = scene.addObject("Collectable", "World")
			newob.worldPosition = Vector(floats)
