import game_data
import tkinter

class ContentDlg:
	def __init__(self, root, content = None):
		self.root = tkinter.Toplevel(takefocus=True)
		self.root.attributes("-toolwindow", 1)
		self.root.wm_attributes("-topmost", 1)
		self.content = content

		btn = tkinter.Button(self.root, text='OK', command=self.OK)
		btn.pack(side=tkinter.LEFT, padx="2m")
	
	def OK(self):
		self.root.destroy()
		
			
if __name__ == "__main__":
	dlg = ContentDlg()
