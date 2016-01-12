import json

class GameContentData:
	def __init__(self):
		self.baseId = 1
		self.textSet = {}
		
	def GetTextContentById(self, id):
		try:
			return self.textSet[id]
		except:
			return "unkown text " + id
			
	def InsertTextContent(self, text):
		self.baseId = self.baseId + 1
		self.SetTextContent(str(self.baseId), text)
			
	def SetTextContent(self, id, text):
		self.textSet[id] = text
		
	def RemoveTextContent(self, id):
		self.pop(id)
		
	def ClearTextContent(self):
		self.textSet = {}
		self.baseId = 1
			
	def SaveToFile(self, fileName):
		f = open(fileName, "w")
		try:
			f.write(json.dumps(self.textSet))
		finally:
			f.close()
		
	def ReadFromFile(self, fileName):
		self.ClearTextContent()
		f = open(fileName, "r")
		try:
			d = f.read()
			self.textSet = json.loads(d)
		finally:
			f.close()
			keys = max(self.textSet.keys())
			self.baseId = int(keys) + 1;
			
class ContentTreeNode:
	def __inti__(self, id):
		self.id = id
		self.left = 0
		self.right = 0
		self.content = 0
			
class ConentTree:
	def __init__(self):
		self.allNode = []
			
if __name__ == "__main__":
	data = GameContentData()
	print(data.GetTextContentById(str(0)))
	for i in range(1, 1000):
		data.InsertTextContent(str(i))
	
	data.SaveToFile("fffff")
	data.ReadFromFile("fffff")
	