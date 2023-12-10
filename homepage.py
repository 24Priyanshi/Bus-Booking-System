from tkinter import *
import subprocess


root=Tk()
root.title("homepage")
root.geometry('%dx%d+0+0'%(root.winfo_screenwidth(),root.winfo_screenheight()))

root.configure(bg="light gray")

frame=LabelFrame(root,padx=50,pady=10,borderwidth=0)
frame.pack(padx=10)



image = PhotoImage(file="bus.png")
Label(frame,image=image).pack()

def bookbus():
    subprocess.run(["python","bookbus.py"])
    root.destroy()

def checkbus():
    subprocess.run(["python","checkbookseat.py"])
    root.destroy()

def admin():
    subprocess.run(["python","admin_use.py"])
    root.destroy()



frame2=LabelFrame(root,padx=10,pady=10,borderwidth=0)
frame2.pack(padx=10)

title_project= Label(frame2,text="Online Bus Booking System",relief="ridge",bg="Dodgerblue3",fg="orangered3",font=('Poppins',40,'bold'),padx=50)
title_project.grid(row=0,column=3)

seat_book_button=Button(frame2, text="Seat Booking",padx=20,relief="ridge",bg="dark olive green",font=('Helvetica 13 bold'),command=bookbus)
seat_book_button.grid(row=1,column=1,pady=30)

check_book_button=Button(frame2, text="Check Booked Seat ",relief="groove",padx=30,bg="gold",font=('Helvetica 13 bold'),command=checkbus)
check_book_button.grid(row=1,column=3,pady=30)

detail_book_button=Button(frame2, text="Add Bus Details ",relief="ridge",padx=20,bg="orange",font=('Helvetica 13 bold'),command=admin)
detail_book_button.grid(row=1,column=4,pady=30)

label1=Label(frame2,text="For Admin Only",fg="red")
label1.grid(row=2,column=4)


root.mainloop()
