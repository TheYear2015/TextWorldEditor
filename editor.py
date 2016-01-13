import game_data
import node_panel
import tkinter

class EditorMain:
	def __init__(self):
		self.allNode=[]
		
		self.content = game_data.ContentData()
		self.tree = game_data.ConentTree()
	
		self.root = tkinter.Tk()
		self.root.title("Text World Editor")
		
		#tool bar
		self.tool_bar = tkinter.Frame(self.root)
		btn = tkinter.Button(self.tool_bar, text='Save', command=self.Save)
		btn.pack(side=tkinter.LEFT, padx="2m")
		
		btn = tkinter.Button(self.tool_bar, text='Load', command=self.Load)
		btn.pack(side=tkinter.LEFT, padx="2m")
		
		self.tool_bar.pack(side=tkinter.TOP, fill=tkinter.X)
		
		#view frame
		frame = tkinter.Frame(self.root)
		frame.pack(side=tkinter.TOP, expand=tkinter.YES, fill=tkinter.BOTH)
		
		self.view_frame = tkinter.Canvas(frame, scrollregion=(0,0,3000,3000))

		scrl = tkinter.Scrollbar(frame, command=self.view_frame.yview)
		self.view_frame.configure(yscrollcommand = scrl.set)
		scrl.pack(side=tkinter.RIGHT, fill=tkinter.Y)
		
		scrl = tkinter.Scrollbar(frame, orient = tkinter.HORIZONTAL, command=self.view_frame.xview)
		self.view_frame.configure(xscrollcommand = scrl.set)
		scrl.pack(side=tkinter.BOTTOM, fill=tkinter.X)

		self.view_frame.pack(side=tkinter.LEFT, expand=tkinter.YES, fill=tkinter.BOTH)
		
		
		#test
		self.TestNode(10000)
		
	def RemoveNode(self, b):
		self.allNode.remove(b)
		b.destroy()
		
	def NewNode(self, posx, posy):
		b = node_panel.NodePanel(self.view_frame,removeFunc=self.RemoveNode)
		self.view_frame.create_window( posx, posy, window=b);
		self.allNode.append(b)
		return b
		
	#重新排版
	def ReLayout():
		#没有关联的放在最后
		print("ReLayout")
		
	def TestNode(self, count):
		for i in range(1, count):
			b = self.NewNode( 50 + 100 * (i % 1000), 30 + 300 * i / 1000)
			
		self.view_frame.update_idletasks()
			
		w = self.view_frame.winfo_screenwidth()
		h = self.view_frame.winfo_screenheight() 
		self.view_frame['scrollregion'] = self.view_frame.bbox('all')
		
	def Save(self):
		print("Save")
		self.content.Save("content_data.pck")
		self.tree.Save("content_tree.pck")

	def Load(self):
		print("Load")
		self.content.Load("content_data.pck")
		self.tree.Load("content_tree.pck")
		
		for b in self.allNode:
			b.destroy()
		self.allNode = []

	def Exit(self):
		self.root.quit()

	def About(self):
		print("About")
		
	def run(self):
		self.root.mainloop()
		
		
			
if __name__ == "__main__":
	editor = EditorMain()
	editor.run()
