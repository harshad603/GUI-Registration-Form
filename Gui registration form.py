from tkinter import *

from tkinter import ttk

win=Tk()
win.title("Form") 
win.geometry("1000x900")
win.configure(background='#d9d2e9')
Label(win,text='Registation Form',bg='#d9d2e9',font=('Arial Rounded MT Bold',25)).place(x=350,y=10)




Label(win,text="Full Name",bg='#d9d2e9',font=("Arial Rounded MT Bold",10)).place(x=20,y=100)
Label(win,text="E-Mail",bg='#d9d2e9',font=("Arial Rounded MT Bold ",12)).place(x=20,y=140)
Label(win,text="Mobile No",bg='#d9d2e9',font=("Arial Rounded MT Bold",10)).place(x=20,y=180)
Label(win, text="GENDER",bg='#d9d2e9',font=('Arial Rounded MT Bold',12)).place(x=20,y=250)
Label(win, text="TIME",bg='#d9d2e9',font=('Arial Rounded MT Bold',12)).place(x=20,y=320)
Label(win, text="COURCES",bg='#d9d2e9',font=('Arial Rounded MT Bold',12)).place(x=20,y=430)
texts=Entry(win,width=35)
texts.place(x=120,y=100)
text2=Entry(win,width=35)
text2.place(x=120,y=140)
text3=Entry(win,width=35)
text3.place(x=120,y=180)


var = IntVar()
var1 =Radiobutton(win,text="Male",bg='#d9d2e9',variable=var,value=0).place(x=120,y=255)
var2=Radiobutton(win,text="Female",bg='#d9d2e9',variable=var,value=1).place(x=220,y=255)

var3 = IntVar()
Checkbutton(win, text="8:00 AM",bg='#d9d2e9',variable=var1).place(x=120,y=330)
var4 = IntVar()
Checkbutton(win, text="10:00 AM",bg='#d9d2e9', variable=var2).place(x=220,y=330)
var5 = IntVar()
Checkbutton(win, text="12:00 PM",bg='#d9d2e9', variable=var2).place(x=120,y=380)
var6= IntVar()
Checkbutton(win, text="2:00 PM",bg='#d9d2e9', variable=var2).place(x=220,y=380)




   
def ok():
    a=texts.get()
    Label(win,text=a,bg='#d9d2e9').place(x=380,y=100)
    a=text2.get()
    Label(win,text=a,bg='#d9d2e9').place(x=380,y=140)
    a=text3.get()
    Label(win,text=a,bg='#d9d2e9').place(x=380,y=180)
    if(var.get()==0):
        print('male')
        Label(win,text=' Male',bg='#d9d2e9').place(x=380,y=260)
    if(var.get()==1):
        print('female')
        Label(win,text=' Female',bg='#d9d2e9').place(x=380,y=260)
    if(vars.get()==0):
     Label(win,text='C').place(x=600,y=600)
  
    if(vars.get()==0):
          Label(win,text='PYTHON').place(x=0,y=0)
    if(vars.get()==1):
          Label(win,text='JAVA').place(x=260,y=550)
    if(vars.get()==0):
          Label(win,text='DATA SCIENCE').place(x=260,y=550)
    if(vars.get()==0):
          Label(win,text='FULLSTACK').place(x=260,y=550)
          

    a=courcechosen.get()

    Label(win,text=a).place(x=50,y=100)
Label(win, text = "Select The Cource :",bg='#d9d2e9',font = ("Arial Rounded MT Bold", 10)).place(x=120,y=460)
a = IntVar()
courcechosen = ttk.Combobox(win, width = 27, textvariable = a)
courcechosen['values'] = (' PYTHON',
						' JAVA',
						' DATA SCIENCE',
						' POWER BI',
                                    'FULLSTACK')
courcechosen.place(x=260,y=460)
Button(win, text='SUBMIT',bg='#69e279',width='12',command=ok ).place(x=400,y=580)
Button(win, text='CLOSE',bg="#ff5154",width='12', command=win.quit).place(x=530,y=580)

win.mainloop()