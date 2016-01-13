import game_data
import tkinter

class NodePanel(tkinter.Frame):
	def __init__(self, parent, removeFunc=None):
		tkinter.Frame.__init__(self, parent, width = 100, height = 100, bg="red")
		self.pack()
		
		#content
		self.content = tkinter.Frame(self)
		self.content.pack(side=tkinter.TOP, expand=tkinter.YES, fill=tkinter.BOTH)
		
		self.id = tkinter.Label(self.content, text="abcd");
		self.id.pack(side=tkinter.TOP, fill=tkinter.X)
		
		self.cList = tkinter.Listbox(self.content)
		self.cList.pack(side=tkinter.TOP, expand=tkinter.YES, fill=tkinter.BOTH)
		
		#romve btn
		btn = tkinter.Button(self, text='del', height= 10, width=10, command=self.RemoveSelf)
		btn.pack(side=tkinter.BOTTOM, padx="2m",fill=tkinter.X)
		
		self.removeCall = removeFunc
		
	def Edit(self):
		print("edit")
		
	def SetData(self, data):
		self.id["text"] = data.id
		
	def RemoveSelf(self):
		if self.removeCall:
			self.removeCall(self)
		
		
			
if __name__ == "__main__":
	root = tkinter.Tk()
	frame = NodePanel(root)
	frame.SetData(game_data.ContentTreeNode('123'))
	root.mainloop()
