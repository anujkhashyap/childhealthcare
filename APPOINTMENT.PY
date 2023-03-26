from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox
from tkcalendar import *
import sqlite3

from tkinter import *
from tkinter import messagebox
from tkcalendar import *
import sqlite3

root2=Tk()
root2.geometry("800x900")
root2.state("zoomed")
root2.title("Appointment Screen")
root2.configure(bg="light grey")
txtname=StringVar()
txtgender=IntVar()
txtcontactno=StringVar()
txtaddress=StringVar()
txtdate=StringVar()
txttimeslot=StringVar()
txtrefer=StringVar()
gender=""

def selection():
     g = txtgender.get()
     global gender

     if g==1:
        gender="Male"
     else:
        gender="Female"
def validation():
        text1=t1.get()

def insert_clicked():
    global gender
    con = sqlite3.connect("appform")
    c = con.cursor()
    p = txtname.get()
    b = txtcontactno.get()
    a = txtaddress.get()
  #  d = txtdate.get()
    d=cal.get_date()
   # t = txttimeslot.get()
    t=min_sb.get()
    n = txtrefer.get()

    if len(p) == 0:
        msg = "The name field can\'t be empty"
        messagebox.showinfo('message', msg)
        t1.focus_set()

    elif len(b) < 10:
        msg1 = "Contact no must have 10 characters"
        messagebox.showinfo('message', msg1)
        t4.focus_set()

    elif len(a) == 0:
        msg2 = "Address field cannot be empty"
        messagebox.showinfo('message', msg2)
        t5.focus_set()
    elif len(d) == 0:
        msg3 = "Date field cannot be empty"
        messagebox.showinfo('message', msg3)
        cal.focus_set()
    elif len(t) == 0:
        msg4 = "Time slot cannot be empty"
        messagebox.showinfo('message', msg4)
        min_sb.focus_set()
    elif len(n) == 0:
        msg5 = "Referred by field cannot be empty"
        messagebox.showinfo('message', msg5)
    if len(p) and len(gender) and len(b) and len(b)==10 and len(a) and len(d) and len(t) and len(n)>0:
        c.execute("insert into slot(name,gender,contactno,address,date,timeslot,referenceby) values(?,?,?,?,?,?,?)",(p,gender,b,a,d,t,n))
        con.commit()
        messagebox.showinfo("Great!","Data Submitted...")
        clear_clicked()

def clear_clicked():
    txtname.set("")
    txtcontactno.set("")
    txtaddress.set("")
    txtdate.set("")
    txttimeslot.set("")
    txtrefer.set("")

def cancel_clicked():
    root2.destroy()

f1=Frame(root2,bg="white",relief=RIDGE,height=60)
f1.pack(side=TOP,fill="x")
l0=Label(f1,fg="darkblue",text="Child Care System",font="Algerian 40 bold",bg="orange",pady=20)
l0.pack(fill="x")



f2=Frame(root2,bg="white",relief=RIDGE)
f2.place(x=100,y=150)
l1=Label(f2,bg="darkblue",font="Algerian 29 bold",text="Personal information",fg="yellow")
l1.pack()


f3=Frame(root2,bg="white",relief=RIDGE)
f3.place(x=80,y=250)
l1=Label(f3,bg="darkblue",font="Algerian 15 bold",text="Name",fg="yellow")
l1.pack()

f4=Frame(root2,bg="white",relief=RIDGE)
f4.place(x=250,y=250)
t1=Entry(f4,textvariable=txtname)
t1.pack()



f5=Frame(root2,bg="white",relief=RIDGE)
f5.place(x=80,y=330)
l1=Label(f5,bg="darkblue",font="Algerian 15 bold",text="Gender",fg="yellow")
l1.pack()

f6=Frame(root2,bg="white",relief=RIDGE)
f6.place(x=250,y=330)
r1=Radiobutton(f6,bg="white",font="Algerian 15 bold",text="Male",fg="red",command=selection,value=1,variable=txtgender)
r1.pack()
r2=Radiobutton(f6,bg="white",font="Algerian 15 bold",text="Female",fg="red",command=selection,value=1,variable=txtgender)
r2.pack()


f7=Frame(root2,bg="white",relief=RIDGE)
f7.place(x=80,y=410)
l4=Label(f7,bg="darkblue",font="Algerian 15 bold",text="Contact No",fg="yellow")
l4.pack()

f8=Frame(root2,bg="white",relief=RIDGE)
f8.place(x=250,y=410)
t4=Entry(f8,textvariable=txtcontactno)
t4.pack()


f8=Frame(root2,bg="white",relief=RIDGE)
f8.place(x=80,y=500)
l5=Label(f8,bg="darkblue",font="Algerian 15 bold",text="Address",fg="yellow")
l5.pack()

f9=Frame(root2,bg="white",relief=RIDGE)
f9.place(x=250,y=500)
t5=Entry(f9,textvariable=txtaddress)
t5.pack()

f10=Frame(root2,bg="white",relief=RIDGE)
f10.place(x=600,y=150)
l6=Label(f10,bg="darkblue",font="Algerian 29 bold",text="Appointment Information",fg="yellow")
l6.pack()


f11=Frame(root2,bg="white",relief=RIDGE)
f11.place(x=600,y=250)
l7=Label(f11,bg="darkblue",font="Algerian 15 bold",text="Date",fg="yellow")
l7.pack()

cal=Calendar(root2,selectmode='day',year=2023,month=1,day=1)

cal.place(x=760,y=250)

f12=Frame(root2,bg="white",relief=RIDGE)
f12.place(x=1100,y=250)
l8=Label(f12,bg="darkblue",font="Algerian 15 bold",text="Time",fg="yellow")
l8.pack()

min_sb = Spinbox(root2,from_=7,to=19,wrap=True,width=2,state="readonly",font="Tahoma",justify=CENTER)
min_sb.place(x=1250,y=250)

f13=Frame(root2,bg="white",relief=RIDGE)
f13.place(x=1100,y=390)




f14=Frame(root2)
f14.place(x=250,y=550)
b1=Button(f14,text="Submit",width="15",command=insert_clicked,bg="dark blue",fg="yellow",font=("Algerian",13))
b1.pack()


f15=Frame(root2)
f15.place(x=550,y=550)
b2=Button(f15,text="Clear",width="15",command=clear_clicked,bg="dark blue",fg="yellow",font=("Algerian",13))
b2.pack()

f16=Frame(root2)
f16.place(x=850,y=550)
b3=Button(f16,text="Cancel",width="15",command=cancel_clicked,bg="dark blue",fg="yellow",font=("Algerian",13))
b3.pack()

root2.mainloop()
