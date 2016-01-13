import game_data
import tkinter

class EditorMain:
	def __init__(self):
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
		self.TestNodeButton(10000)
		
	def TestNodeButton(self, count):
		for i in range(1, count):
			self.view_frame.create_window( 50 + 100 * (i % 1000), 30 + 40 * i / 1000, tags='BTN1',window=tkinter.Button(self.view_frame,text=u'侦听'+str(i),width=8))
		
		
	def Save(self):
		print("Save")

	def Load(self):
		print("Load")

	def Exit(self):
		self.root.quit()

	def About(self):
		print("About")
		
	def run(self):
		self.root.mainloop()
		
		
			
if __name__ == "__main__":
	editor = EditorMain()
	editor.run()
