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
