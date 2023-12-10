from tkinter import *
import subprocess


root=Tk()
root.geometry('%dx%d+0+0'%(root.winfo_screenwidth(),root.winfo_screenheight()))
def newop():
    subprocess.run(["python","newop.py"])
    root.destroy()


def newbus():
    subprocess.run(["python","newbus.py"])
    root.destroy()


def newroute():
    subprocess.run(["python","newroute.py"])
    root.destroy()


def newrun():
    subprocess.run(["python","newrun.py"])
    root.destroy()

def homepage():
    subprocess.run(["python","homepage.py"])
    root.destroy()

root.title("checkbookedseat")
root.configure(bg="light gray")



frame=LabelFrame(root,padx=10,pady=10,borderwidth=0)
frame.pack(padx=10)
image = PhotoImage(file="bus.png")
Label(frame,image=image).pack()


frame2=LabelFrame(root,padx=10,pady=10,borderwidth=0)
frame2.pack(padx=10)

title_project= Label(frame2,text="Online Bus Booking System",relief="groove",font=('Helvetica 40 bold'),bg="turquoise",fg="red",padx=50)
title_project.grid(row=0,column=3,pady=50)

frame3=LabelFrame(root,padx=10,pady=10,borderwidth=0)
frame3.pack(padx=10)

Label(frame2,text="Add New Details to Database",fg="orangered2",font=('Helvetica 22 bold')).grid(row=1,column=3,pady=10)



Button(frame3,text="New Operator",bg="light slate blue",font=('Helvetica 20 bold'),command=newop).grid(row=2,column=2,padx=20,pady=10)


Button(frame3,text="New Bus",bg="khaki",font=('Helvetica 20 bold'),command=newbus).grid(row=2,column=3,padx=20,pady=10)

Button(frame3,text="New Route",bg="aquamarine2",font=('Helvetica 20 bold'),command=newroute).grid(row=2,column=4,padx=20,pady=10)

Button(frame3,text="New Run",bg="sienna1",font=('Helvetica 20 bold'),command=newrun).grid(row=2,column=6,padx=20,pady=10)


home=PhotoImage(file="homelogo.png")
home_button=Button(frame2,image=home,bg="lime green",command=homepage)
home_button.grid(row=3,column=5,pady=10)

root.mainloop()
