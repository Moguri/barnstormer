import bge


def main(cont):
	player = bge.logic.getSceneList()[1].objects["PlayerController"]
	camera = cont.owner
	
	camera.worldOrientation = player.worldOrientation