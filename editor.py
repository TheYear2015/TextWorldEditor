import game_data
import tkinter

class EditorMain:
	def __init__(self):
		self.root = tkinter.Tk()
		self.root.title("Text World Editor")
		
		self.menu_frame = tkinter.Frame(self.root)
		self.menu_frame.pack(fill=tkinter.X, side=tkinter.TOP)
		self.menu_frame.tk_menuBar(self.file_menu(), self.help_menu())

	def file_menu(self):
		btn = tkinter.Menubutton(self.menu_frame, text='File', underline=0)
		btn.pack(side=tkinter.LEFT, padx="2m")
		btn.menu = tkinter.Menu(btn)
		btn.menu.add_command(label="Save", underline=0, command=self.Save)
		btn.menu.add_command(label="Load", underline=0, command=self.Load)
		btn.menu.add_command(label="Exit", underline=0, command=self.Exit)
		btn['menu'] = btn.menu
		return btn

	def help_menu(self):
		help_btn = tkinter.Menubutton(self.menu_frame, text='Help', underline=0)
		help_btn.pack(side=tkinter.LEFT, padx="2m")
		help_btn.menu = tkinter.Menu(help_btn)
		help_btn.menu.add_command(label="About", underline=0, command=self.About)
		help_btn['menu'] = help_btn.menu
		return help_btn
		
	def Save(self):
		print("Save")

	def Load(self):
		print("Load")

	def Exit(self):
		print("Exit")

	def About(self):
		print("About")
		
	def run(self):
		self.root.mainloop()
			
if __name__ == "__main__":
	editor = EditorMain()
	editor.run()
