import bgui
import bgui.bge


from bge import logic, events
from collections import OrderedDict


class LevelSelectLayout(bgui.bge.Layout):
	class LevelListRenderer:
		def __init__(self, listbox):

			self.frame = bgui.Frame(listbox, size=[1, 1])
			self.label = bgui.Label(listbox)

			#self.frame.size = self.label.size
			self.frame.colors = [(1, 1, 1, 0) for i in range(4)]

			self.listbox = listbox

		def render_item(self, item):
			self.label.text = str(item)

			if item == self.listbox.selected:
				self.label.color = [0.5,0,0,1]
			else:
				self.label.color = self.label.theme['Color']

			return self.label

	def __init__(self, sys, data):
		super().__init__(sys, data)

		bgui.Label(self, text="Barnstormer", pos=[0.1, 0.8])
		bgui.Label(self, text="Use the arrow keys to select a level and space or enter to start that level", pos=[0.1, 0.1])

		self.levels = OrderedDict()
		self.levels["Free Roam"] = "free_roam.blend"
		self.levels["Collection Training"] = "five_stunt.blend"

		self.listbox = bgui.ListBox(self, items=self.levels.keys(), pos=[0.15, 0.2], size=[0.6, 0.55])
		self.listbox.renderer = self.LevelListRenderer(self.listbox)
		self.listbox.on_click = self.lb_click

		self.listbox.selected = list(self.levels.keys())[0]

	def lb_click(self, lb):
		if self.listbox.selected:
			logic.startGame(logic.expandPath("//"+self.levels[self.listbox.selected]))

	def update(self):
		keys = logic.keyboard.active_events
		level_list = list(self.levels.keys())

		if events.SPACEKEY in keys:
			self.lb_click(self.listbox)
		if events.ENTERKEY in keys:
			self.lb_click(self.listbox)
		if events.PADENTER in keys:
			self.lb_click(self.listbox)
		if events.DOWNARROWKEY in keys and keys[events.DOWNARROWKEY] == logic.KX_INPUT_JUST_ACTIVATED:
			self.listbox.selected = level_list[(level_list.index(self.listbox.selected) + 1) % len(level_list)]
		if events.UPARROWKEY in keys and keys[events.UPARROWKEY] == logic.KX_INPUT_JUST_ACTIVATED:
			self.listbox.selected = level_list[level_list.index(self.listbox.selected) - 1]
