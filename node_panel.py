import game_data
import tkinter

class NodePanel:
	def __init__(self, parent):
		#frame
		self.root = tkinter.Frame(parent, width = 100, height = 100, bg="red")
		self.root.pack()
		
		#content
		self.content = tkinter.Frame(self.root)
		self.content.pack(side=tkinter.TOP, expand=tkinter.YES, fill=tkinter.BOTH)
		
		self.id = tkinter.Label(self.content, text="abcd");
		self.id.pack(side=tkinter.TOP, fill=tkinter.X)
		
		self.cList = tkinter.Listbox(self.content)
		self.cList.pack(side=tkinter.TOP, expand=tkinter.YES, fill=tkinter.BOTH)
		
		#editor btn
		#btn = tkinter.Button(self.root, text='...', height= 10, command=self.Edit)
		#btn.pack(side=tkinter.BOTTOM, padx="2m",fill=tkinter.X)
		
	def Edit(self):
		print("edit")
		
	def SetData(self, data):
		self.id["text"] = data.id
		
			
if __name__ == "__main__":
	root = tkinter.Tk()
	frame = NodePanel(root)
	frame.SetData(game_data.ContentTreeNode('123'))
	root.mainloop()
