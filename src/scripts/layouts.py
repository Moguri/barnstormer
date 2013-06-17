import bgui
import bgui.bge


from bge import logic, events


class LevelSelectLayout(bgui.bge.Layout):
	def __init__(self, sys, data):
		super().__init__(sys, data)

		bgui.Label(self, text="Press the spacebar to start")

	def update(self):
		if events.SPACEKEY in logic.keyboard.active_events:
			logic.startGame(logic.expandPath("//free_roam.blend"))