from tkinter import *
from PIL import Image,ImageTk
a=Tk()
a.state("zoomed")
a.minsize(1300,750)


def signup():
    import Signup

def login():
    import Login





f1=Frame(a,bg="white",relief=RIDGE,height=60)
f1.pack(side=TOP,fill="x")
l1=Label(f1,fg="darkblue",text="CHILD HEALTH CARE",font="Algerian 40 bold",bg="pink",pady=20)
l1.pack(fill="x")

f2=Frame(a,bg="black",relief=RIDGE,height=10)
f2.pack(fill="x")


img=Image.open("C:\\Users\\argha\\OneDrive\\Desktop\\Child Care\\image2.jpg")
resized=img.resize((792,450),Image.ANTIALIAS)
ph=ImageTk.PhotoImage(resized)
l=Label(a,image=ph,fg="red",borderwidth=7,bg="black")
l.place(x=0,y=110)






f5=Frame(a,bg="white",relief=RIDGE)
f5.place(x=0,y=574)
l1=Label(f5,font="Algerian 40 bold",bg="darkblue",width=400,height=100)
l1.pack(fill="x")






img77=Image.open("C:\\Users\\argha\\OneDrive\\Desktop\\SSC Python Project\\55.png")
r77=img77.resize((155,150),Image.ANTIALIAS)
ph77=ImageTk.PhotoImage(r77)

img78=Image.open("C:\\Users\\argha\\OneDrive\\Desktop\\SSC Python Project\\56.jpg")
r78=img78.resize((155,150),Image.ANTIALIAS)
ph78=ImageTk.PhotoImage(r78)

img79=Image.open("C:\\Users\\argha\\OneDrive\\Desktop\\SSC Python Project\\57.jpg")
r79=img79.resize((155,150),Image.ANTIALIAS)
ph79=ImageTk.PhotoImage(r79)

img80=Image.open("C:\\Users\\argha\\OneDrive\\Desktop\\SSC Python Project\\58.jpg")
r80=img80.resize((155,150),Image.ANTIALIAS)
ph80=ImageTk.PhotoImage(r80)


img3=Image.open("C:\\Users\\argha\\OneDrive\\Desktop\\Child Care\\image3.jpg")
resized3=img3.resize((792,450),Image.ANTIALIAS)
ph3=ImageTk.PhotoImage(resized3)
l3=Label(a,image=ph3,fg="red",borderwidth=7,bg="black")
l3.place(x=730,y=110)



createuser= Button(a,image=ph77, borderwidth=8,command=signup,bg="darkblue")
createuser.place(x=250,y=575)

login= Button(a,bg="darkblue", image=ph78, borderwidth=8,command=login)
login.place(x=530,y=575)


Review= Button(a,bg="darkblue", image=ph79, borderwidth=8)
Review.place(x=790,y=575)

exit= Button(a,bg="darkblue", image=ph80, borderwidth=8,command=quit)
exit.place(x=1070,y=575)

f6=Frame(a,bg="black",relief=RIDGE,width=1,height=15)
f6.place(x=210,y=570)
l11=Label(f6,bg="black",width=1,height=15)
l11.pack()

f6=Frame(a,bg="white",relief=RIDGE)
f6.place(x=470,y=570)
l11=Label(f6,bg="black",width=1,height=100)
l11.pack()

f6=Frame(a,bg="white",relief=RIDGE)
f6.place(x=750,y=570)
l11=Label(f6,bg="black",width=1,height=100)
l11.pack()

f6=Frame(a,bg="white",relief=RIDGE)
f6.place(x=1010,y=570)
l11=Label(f6,bg="black",width=1,height=100)
l11.pack()

f6=Frame(a,bg="white",relief=RIDGE)
f6.place(x=1280,y=570)
l11=Label(f6,bg="black",width=1,height=100)
l11.pack()

f6=Frame(a,bg="white",relief=RIDGE)
f6.place(x=230,y=745)
l11=Label(f6,bg="darkblue", font="Algerian 24 bold",text="CREATE USER",fg="yellow")
l11.pack()

f6=Frame(a,bg="white",relief=RIDGE)
f6.place(x=570,y=745)
l11=Label(f6,bg="darkblue",font="Algerian 24 bold",text="LOGIN",fg="yellow")
l11.pack()

f6=Frame(a,bg="white",relief=RIDGE)
f6.place(x=830,y=745)
l11=Label(f6,bg="darkblue",font="Algerian 24 bold",text="FAQ",fg="yellow")
l11.pack()

f6=Frame(a,bg="white",relief=RIDGE)
f6.place(x=1100,y=745)
l11=Label(f6,bg="darkblue",font="Algerian 29 bold",text="EXIT",fg="yellow")
l11.pack()

f6=Frame(a,bg="white",relief=RIDGE)
f6.place(x=1330,y=570)
l11=Label(f6,bg="darkblue",font="Algerian 20 bold",text="Made By-",fg="yellow")
l11.pack()

f6=Frame(a,bg="white",relief=RIDGE)
f6.place(x=1330,y=600)
l11=Label(f6,bg="darkblue",font="Algerian 16 bold",text="Arghadeep Nath",fg="yellow")
l11.pack()

f6=Frame(a,bg="white",relief=RIDGE)
f6.place(x=1330,y=630)
l11=Label(f6,bg="darkblue",font="Algerian 14 bold",text="2210990152",fg="yellow")
l11.pack()

f6=Frame(a,bg="white",relief=RIDGE)
f6.place(x=1330,y=700)
l11=Label(f6,bg="darkblue",font="Algerian 14 bold",text="2210990151",fg="yellow")
l11.pack()

f6=Frame(a,bg="white",relief=RIDGE)
f6.place(x=1330,y=770)
l11=Label(f6,bg="darkblue",font="Algerian 14 bold",text="2210990145",fg="yellow")
l11.pack()

f6=Frame(a,bg="white",relief=RIDGE)
f6.place(x=1330,y=670)
l11=Label(f6,bg="darkblue",font="Algerian 16 bold",text="Archita",fg="yellow")
l11.pack()

f6=Frame(a,bg="white",relief=RIDGE)
f6.place(x=1330,y=740)
l11=Label(f6,bg="darkblue",font="Algerian 16 bold",text="Anuj",fg="yellow")
l11.pack()















a.mainloop()
