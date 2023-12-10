from tkinter import *


import subprocess



root=Tk()
root.title("fontpage")
root.configure(bg="light gray")
root.geometry('%dx%d+0+0'%(root.winfo_screenwidth(),root.winfo_screenheight()))
#to goto homepage

def homepage(event):
    subprocess.run(["python","homepage.py"])



#bus_image
    
image = PhotoImage(file="bus.png")
Label(root,image=image).pack()
#title
title_project= Label(root,text="Online Bus Booking System",bg="light blue",fg="orangered2",font=('Poppins',40,'bold'),padx=50)
title_project.pack()

#name of student
name_student= Label(root,text="Student Name : Priyanshi Mishra ",fg="Dodgerblue3",bg="light gray",font=('Poppins',15),pady=30)
name_student.pack()
#enrollment no.
enroll= Label(root,text="Enrollment No. : 221B473 ",fg="Dodgerblue3",bg="light gray",pady=30,font=('Poppins',15))
enroll.pack()



#mobile number
mobile= Label(root,text="Mobile No. : 9302364167 ",fg="Dodgerblue3",bg="light gray",pady=30,font=('Poppins',15))
mobile.pack()

#teacher name
teacher= Label(root,text="Submitted To : Dr. Mahesh Kumar ",bg="cyan2",fg="red",pady=10,font=('Poppins',15))
teacher.pack()

#bind with key so that after pressing any key it would redirect to homepage

root.bind("<Key>",homepage)

root.mainloop()
