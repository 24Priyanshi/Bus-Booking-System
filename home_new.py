from tkinter import *
root=Tk()

root.geometry('1000x400')

img=PhotoImage(file='.\\Bus.png')
Label(root, image=img).grid(row=0, column=0, padx=600, columnspan=13)

Label(root, text='Online Bus Booking System', font='Arial 30 bold', bg='light blue', fg='red').grid(row=1, column=6, columnspan=3)
Label(root, text='Name: Priyanshi Mishra', font='Arial 18 bold', fg='navy').grid(row=4, column=7,pady=40)
Label(root, text='Er: 221B473', font='Arial 18 bold', fg='navy').grid(row=6, column=7,pady=40)
Label(root, text='Mobile:9302364167', font='Arial 18 bold', fg='navy').grid(row=8, column=7,pady=40)

Label(root, text="Submitted to: Dr. Mahesh Kumar", font='Arial 30 bold', bg="light blue", fg='red').grid(row=9, column=7,pady=50)


Label(root, text="Project based learning", font='Arial 18 bold', fg='red').grid(row=10, column=7)

root.mainloop()




