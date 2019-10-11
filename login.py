from tkinter import*
from pyautogui import size

screen_width,screen_height=size()


class gui_manager:
	
	def __init__(self):
		
		self.main_app=Tk()
		self.main_app.resizable(0,0)
		self.main_app.title("Paymaster")
		self.main_app.geometry(f"{int(screen_width*.7)}x{int(screen_height*.7)}+{int(screen_width*.26)}+{int(screen_height*.2)}")
		self.widget_pack()
		self.main_menu=Menu(self.main_app)
		self.main_menu.add_cascade(label="File")
		self.main_menu.add_command(label="Exit",command=self.main_app.destroy)
		self.main_app.configure(background="grey",menu=self.main_menu)
		self.main_app.mainloop()

	def widget_pack(self):
	
		self.main_menu=Menu(self.main_app)
		
		self.main_menu.add_cascade(label="File",menu=self.main_menu)
		
		self.labeF=LabelFrame(background="#444")
		
		self.labeF.pack()
		
		self.main_label=Label(self.labeF,text="Enter your username and password",font=("old english text mt",15,"bold"))
		self.labeF=LabelFrame(self.main_app)
		self.labeF.pack()
		self.user_label=Label(self.labeF,text="Username")
		self.user_label.pack(side="left")
		self.username_entry=Entry(self.labeF,width=20,font=("old english text mt",16,"bold"))
		self.username_entry.pack()

		self.labeF=LabelFrame(self.main_app)
		self.labeF.pack()
		self.password_entry=Entry(self.labeF,width=20,show="*",font=("old english text mt",16,"bold"))
		self.password_entry.pack()
		self.main_label.pack()

gui_manager()