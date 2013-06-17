import sys
import os


from bge import logic


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
