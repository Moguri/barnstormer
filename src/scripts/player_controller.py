from bge import logic

class PlayerController:
	def __init__(self, ob):
		self.obj = ob
		print("Attaching player controller to", ob)

	def run(self):
		pass

def main(cont):
	ob = cont.owner

	try:
		ob['pc'].run()
	except KeyError:
		ob['pc'] = PlayerController(ob)
		
