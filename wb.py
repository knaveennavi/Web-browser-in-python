from tkinter import *
import webbrowser
def ig():
    webbrowser.open("https://www.instagram.com/")
def fb():
    webbrowser.open("https://www.facebook.com/")
def wa():
    webbrowser.open("https://web.whatsapp.com/")
def tw():                                       
    webbrowser.open("https://twitter.com/")
def em():
    webbrowser.open("https://mail.google.com/")
def yt():
    webbrowser.open("https://www.youtube.com/")    
def se():
    w=x.get()
    s="https://www.google.com/search?q="+w
    webbrowser.open(s)
m=Tk()
m.title("Browser")
n=Frame(m,bg='#4FC3F7',height=400,width=400)
n.pack()
x=StringVar()
l= Label(m,text='Pynavee Browser',bg='#4FC3F7',font="PhytonScriptDemo").place(x=120,y=70)                          
l1= Label(m,text='Pynavee',bg='#4FC3F7' ).place(x=150,y=370)
b1=Button(m,text ='Instagram',command=ig).place(x=10, y=200,width=80,height=30)
b2=Button(m,text ='Facebook',command=fb).place(x=100, y=200,width=80,height=30)
b3=Button(m,text ='Whatsapp',command=wa).place(x=190, y=200,width=80,height=30)
b4=Button(m,text ='Twitter',command=tw).place(x=280, y=200,width=80,height=30)
b5=Button(m,text ='Gmail',command=em).place(x=100, y=250,width=80,height=30)
b6=Button(m,text ='YouTube',command=yt).place(x=190,y=250,width=80,height=30)
b7=Button(m,text ='Search',command=se).place(x=280,y=150,width=80,height=30)
e1= Entry(m,bd=5,textvariable=x).place(x=20, y=150,width=240,height=30)
l.pack()
l1.pack()
b1.pack()
b2.pack()
b3.pack()
b4.pack()
b5.pack()
b6.pack()
e1.pack()
m.mainloop()
