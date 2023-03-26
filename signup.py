from tkinter import *
from tkinter import messagebox
import sqlite3


b=Tk()
b.title("Login screen")
b.state("zoomed")

b.minsize(1800, 900)
b.maxsize(1800, 900)

frame=Frame(b, bg="white",width=1200, height=950)
frame.place(x=293, y=0 )
heading=Label(frame, text="SIGN UP", fg="blue", bg="white", font=("Playfair Display Font", 60, "underline") )
heading.place(x=450, y=10)

def login():
    import Login




u = Label(b, text="Username", font="comicsansms 30 italic", bg="white").place(x=600, y=130)
p = Label(b, text="Password", font="comicsansms 30 italic", bg="white").place(x=600, y=210)
cp = Label(b, text="Confirm Password", font="comicsansms 30 italic", bg="white").place(x=540, y=290)
pn = Label(b, text="Phone no", font="comicsansms 30 italic", bg="white").place(x=600, y=370)
ad = Label(b, text="Address", font="comicsansms 30 italic", bg="white").place(x=600, y=450)
e = Label(b, text="Email Id", font="comicsansms 30 italic", bg="white").place(x=600, y=530)
gen = Label(b, text="Gender", font="comicsansms 30 italic", bg="white").place(x=600, y=610)
age = Label(b, text="Age", font="comicsansms 30 italic", bg="white").place(x=620, y=690)

uvalue = StringVar()
pvalue = StringVar()
cpvalue = StringVar()
pnvalue = StringVar()
advalue = StringVar()
evalue = StringVar()
var = IntVar()
agevalue = StringVar()
city=StringVar()


def c_c():
    con = sqlite3.connect("project1.sqlite")
    con1 = sqlite3.connect("project2.sqlite")
    con2= sqlite3.connect("project3.sqlite")
    c = con.cursor()
    d = con1.cursor()
    f = con2.cursor()

    u1 = uvalue.get()
    p1 = pvalue.get()
    cp1 = cpvalue.get()
    pn1 = pnvalue.get()
    e1 = evalue.get()

    c.execute("select * from lab22 where username=? and password=?", (u1, p1))
    d.execute("select * from phone22 where phone=?", (pn1,))
    f.execute("select * from email22 where email=?", (e1,))

    data = c.fetchall()
    data1 = d.fetchall()
    data2 = f.fetchall()

    if p1 != cp1:
        messagebox.showinfo("Alert!", "Check your Password")
    elif len(pn1)!=10:
        messagebox.showinfo("Alert!", "Enter valid phone no")
    elif len(data) > 0:
        messagebox.showinfo("Alert!", "Username/Password already exits")
    elif len(data1) > 0:
        messagebox.showinfo("Alert!", "Phone no already exits")
    elif len(data2) > 0:
        messagebox.showinfo("Alert!", "Email Id  already exits")



    else:

        c.execute("insert into lab22(username,password) values (?,?)", (u1, p1))
        d.execute("insert into phone22(phone) values (?)", (pn1,))
        f.execute("insert into email22(email) values (?)", (e1,))

        con.commit()
        con1.commit()
        con2.commit()
        messagebox.showinfo("Great!", "User Created...")












uentry = Entry(b, textvariable=uvalue, borderwidth=10, font="Algerian 18 italic").place(x=940, y=130)
pentry = Entry(b, textvariable=pvalue, borderwidth=10, font="Algerian 18 italic").place(x=940, y=210)
cpentry = Entry(b, textvariable=cpvalue, borderwidth=10, font="Algerian 18 italic").place(x=940, y=290)
pnentry = Entry(b, textvariable=pnvalue, borderwidth=10, font="Algerian 18 italic").place(x=940, y=370)
adentry = Entry(b, textvariable=advalue, borderwidth=10, font="Algerian 18 italic").place(x=940, y=450)
eentry = Entry(b, textvariable=evalue, borderwidth=10, font="Algerian 18 italic").place(x=940, y=530)
radio = Radiobutton(b, bg="white", font="Algerian 18 italic", text="Male", variable=var, value=1).place(x=940, y=630)
radio = Radiobutton(b, bg="white", font="Algerian 18 italic", text="Female", variable=var, value=2).place(x=1060, y=630)
ageentry = Entry(b, textvariable=agevalue, borderwidth=10, font="Algerian 18 italic").place(x=940, y=690)
label111=Label(b,text="City")
label111.place(x=940 ,y=580 )







button= Button(frame, width=30, fg="white", bg="darkblue", text="SIGN UP", pady=7, border=0, font=("Century Gothic", 15),command=c_c)
button.place(x=450, y=750)

l2=Label(frame, text="Already have an account?", font=("Gill Sans MT", 20), fg="black", bg="white")
l2.place(x=395, y=840)
signup=Button(frame, width=7, text="Login", border=0, bg="white", fg="darkblue", font=("Gill Sans MT", 17, "bold"), cursor="hand2"
              ,command=login)
signup.place(x=710, y=835)

back=Button(frame, text="BACK ⏎", font=("Gill Sans MT", 15, "bold"), cursor="hand2", bg="white", width=7, border=0, fg="darkblue")
back.place(x=820, y=840)

b.mainloop()
