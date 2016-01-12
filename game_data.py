import json

class ContentData:
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
		
	def Clean(self):
		self.textSet = {}
		self.baseId = 1
			
	def SaveToFile(self, fileName):
		f = open(fileName, "w")
		try:
			f.write(json.dumps(self.textSet))
		finally:
			f.close()
		
	def ReadFromFile(self, fileName):
		self.Clean()
		f = open(fileName, "r")
		try:
			d = f.read()
			self.textSet = json.loads(d)
		finally:
			f.close()
			keys = max(self.textSet.keys())
			self.baseId = int(keys) + 1;


def ContentTreeNode2Dict(obj):
    #convert object to a dict
    d = {}
    d.update(obj.__dict__)
    return d
 
def Dict2ContentTreeNode(d):
    #convert dict to object
    if'__class__' in d:
        args = dict((key.encode('ascii'), value) for key, value in d.items()) #get args
        inst = ContentTreeNode(**args) #create new instance
    else:
        inst = d
    return inst
			
class ContentTreeNode:
	def __init__(self, id, left='0', right='0', content='0'):
		self.id = id
		self.left = left
		self.right = right
		self.content = content
		
	def __str__(self):
		return "["+self.id + ","+self.left +","+self.right+","+self.content+"]";
		
	def Clean(self):
		self.left = "0"
		self.right = "0"
		self.content = "0"
			
class ConentTree:
	def __init__(self):
		self.allNode = {"0":ContentTreeNode("0")}
		self.baseId = 0
		
	def Clean(self):
		self.allNode = {"0":ContentTreeNode("0")}
		self.baseId = 0

	def NewNode(self):
		self.baseId = self.baseId + 1
		n = ContentTreeNode(str(self.baseId))
		self.allNode[n.id] = n
		
	def GetNode(self, id):
		return self.allNode.get(id, None)

	def GetSortedKeys(self):
		return sorted(self.allNode)
		
	def SaveToFile(self, fileName):
		f = open(fileName, "w")
		try:
			f.write(json.dumps(self.allNode, default=ContentTreeNode2Dict))
		finally:
			f.close()
		
	def ReadFromFile(self, fileName):
		self.Clean()
		f = open(fileName, "r")
		try:
			d = f.read()
			self.allNode = json.loads(d,object_hook = Dict2ContentTreeNode)
		finally:
			f.close()
			keys = max(self.allNode.keys())
			self.baseId = int(keys) + 1;
		
			
if __name__ == "__main__":
	data = ContentData()
	print(data.GetTextContentById(str(0)))
	for i in range(1, 1000):
		data.InsertTextContent(str(i))
	
	data.SaveToFile("fffff")
	data.ReadFromFile("fffff")
	
	tree = ConentTree();
	n = tree.GetNode("0")
	if n :
		print(n)
	else :
		print("empyt")
		
	print(tree.GetSortedKeys())
	for i in range(1, 1000):
		tree.NewNode()
	tree.SaveToFile("tttt")
	tree.ReadFromFile("tttt")
	