

class GameData:
	def __init(self):
		self.baseId = 0
		self.textSet = {}
		
	def GetTextContentById(self, id):
		try:
			return self.textSet[id]
		except:
			return "unkown text " + str(id)
			

if __name__ == "__main__":
	data = GameData()
	print(data.GetTextContentById(0)) 