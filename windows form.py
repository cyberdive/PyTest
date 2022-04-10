from tkinter import*
from tkinter import messagebox
def msgCallBack():
   messagebox.showinfo("WayToLearnX", "Welcome to WayToLearnX!")
obj=Tk()

obj.title("c# corner")  
obj.geometry("730x450")


Label(obj, text="Firstname").grid(row=0)
Label(obj, text="Lastname").grid(row=1)
e1 = Entry(obj)
e2 = Entry(obj)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)


btn = Button(obj, text ="Cliquez ici!", command = msgCallBack)


wintext = Text(obj)
wintext.insert(INSERT, "Hello.....")
wintext.insert(END, "welcome to c# corner.....")
wintext.grid(row=3,column=1)
btn.grid(row=2,column=1)
obj.mainloop() 
