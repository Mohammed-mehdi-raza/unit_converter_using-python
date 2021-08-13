from tkinter import *
from tkinter import messagebox

window=Tk()
window.title("unit converter")
window.resizable(False,False)
window.configure(bg="#47d147")
window.geometry("250x250")
l=Label(window,text=" ",font="arial 15",bg="#47d147",fg="BLUE")
l.place(x=30,y=75)

def click():
    text=clicked.get()
    if text=="Length":
        var.set("cm to m")
        options1=[
            'cm to m',
            'm to cm',
            'm to km',
            'km to m',
            'cm to km',
            'km to cm'
            ]
        selected(options1)
    elif text=="Mass":
        var.set("mg to gm")
        options1=[
            'mg to gm',
            'gm to mg',
            'gm to kg',
            'kg to gm',
            'mg to kg',
            'kg to mg'
            ]
        selected(options1)
    elif text=="Time":
        var.set("sec to min")
        options1=[
            'sec to min',
            'min to sec',
            'min to hr',
            'hr to min',
            'sec to hr',
            'hr to sec'
            ]
        selected(options1)
    elif text=="Temperature":
        var.set("cel to fah")
        options1=[
            'cel to fah',
            'fah to cel',
            'fah to kelvin',
            'kelvin to fah',
            'cel to kelvin',
            'kelvin to cel'
            ]
        selected(options1)
    else:
        return
    return

def click1(l):
    tx=var.get()
    if tx=="cm to m":
        x=e1.get()
        x=int(x)
        ans=x/100
        ans=str(ans)
        sr="Result:"+ans+" m"
        l['text']=sr
    elif tx=="m to cm":
        x=e1.get()
        x=int(x)
        ans=x*100
        ans=str(ans)
        sr="Result:"+ans+" cm"
        l['text']=sr
    elif tx=="m to km":
        x=e1.get()
        x=int(x)
        ans=x/1000
        ans=str(ans)
        sr="Result:"+ans+" km"
        l['text']=sr
    elif tx=="km to m":
        x=e1.get()
        x=int(x)
        ans=x*1000
        ans=str(ans)
        sr="Result:"+ans+" m"
        l['text']=sr
    elif tx=="cm to km":
        x=e1.get()
        x=int(x)
        ans=x/100000
        ans=str(ans)
        sr="Result:"+ans+" km"
        l['text']=sr
    elif tx=="km to cm":
        x=e1.get()
        x=int(x)
        ans=x*100000
        ans=str(ans)
        sr="Result:"+ans+" cm"
        l['text']=sr
    elif tx=="mg to gm":
        x=e1.get()
        x=int(x)
        ans=x/1000
        ans=str(ans)
        sr="Result:"+ans+" gm"
        l['text']=sr
    elif tx=="gm to mg":
        x=e1.get()
        x=int(x)
        ans=x*1000
        ans=str(ans)
        sr="Result:"+ans+" mg"
        l['text']=sr
    elif tx=="gm to kg":
        x=e1.get()
        x=int(x)
        ans=x/1000
        ans=str(ans)
        sr="Result:"+ans+" kg"
        l['text']=sr
    elif tx=="kg to gm":
        x=e1.get()
        x=int(x)
        ans=x*1000
        ans=str(ans)
        sr="Result:"+ans+" gm"
        l['text']=sr
    elif tx=="kg to mg":
        x=e1.get()
        x=int(x)
        ans=x*1000000
        ans=str(ans)
        sr="Result:"+ans+" mg"
        l['text']=sr
    elif tx=="mg to kg":
        x=e1.get()
        x=int(x)
        ans=x/1000000
        ans=str(ans)
        sr="Result:"+ans+" kg"
        l['text']=sr
    elif tx=="sec to min":
        x=e1.get()
        x=int(x)
        ans=x/60
        ans=str(ans)
        sr="Result:"+ans+" min"
        l['text']=sr
    elif tx=="min to sec":
        x=e1.get()
        x=int(x)
        ans=x*60
        ans=str(ans)
        sr="Result:"+ans+" sec"
        l['text']=sr
    elif tx=="min to hr":
        x=e1.get()
        x=int(x)
        ans=x/60
        ans=str(ans)
        sr="Result:"+ans+" hr"
        l['text']=sr
    elif tx=="hr to min":
        x=e1.get()
        x=int(x)
        ans=x*60
        ans=str(ans)
        sr="Result:"+ans+" min"
        l['text']=sr
    elif tx=="hr to sec":
        x=e1.get()
        x=int(x)
        ans=x*3600
        ans=str(ans)
        sr="Result:"+ans+" sec"
        l['text']=sr
    elif tx=="sec to hr":
        x=e1.get()
        x=int(x)
        ans=x/3600
        ans=str(ans)
        sr="Result:"+ans+" hr"
        l['text']=sr
    elif tx=="cel to fah":
        x=e1.get()
        x=int(x)
        ans=(x*9/5)+32
        ans=str(ans)
        sr="Result:"+ans+" F"
        l['text']=sr
    elif tx=="fah to cel":
        x=e1.get()
        x=int(x)
        ans=(x-32)*5/9
        ans=str(ans)
        sr="Result:"+ans+" C"
        l['text']=sr
    elif tx=="fah to kelvin":
        x=e1.get()
        x=int(x)
        ans=(x-32)*5/9+273.15
        ans=str(ans)
        sr="Result:"+ans+" K"
        l['text']=sr
    elif tx=="kelvin to fah":
        x=e1.get()
        x=int(x)
        ans=(x-273.15)*9/5+32
        ans=str(ans)
        sr="Result:"+ans+" F"
        l['text']=sr
    elif tx=="kelvin to cel":
        x=e1.get()
        x=int(x)
        ans=x-273.15
        ans=str(ans)
        sr="Result:"+ans+" C"
        l['text']=sr
    elif tx=="cel to kelvin":
        x=e1.get()
        x=int(x)
        ans=x+273.15
        ans=str(ans)
        sr="Result:"+ans+" K"
        l['text']=sr
    else:
        l['text']=" "
    return

options=[
    "Length",
    "Mass",
    "Time",
    "Temperature"
    ]

clicked=StringVar()
clicked.set("Select")
drop=OptionMenu(window,clicked,*options,command=lambda x:click())
drop.config(width=25,bg="#adebad",highlightthickness=0)
drop["menu"].config(bg="#adebad")
drop.place(x=30,y=30)

var=StringVar()
e1=Entry(window,width=10,bg="#adebad",highlightthickness=0,font="arial 14")

def selected(options1):
     e1.place(x=10,y=120)
     drop1=OptionMenu(window,var,*options1)
     drop1.config(width=10,bg="#adebad",highlightthickness=0)
     drop1["menu"].config(bg="#adebad")
     drop1.place(x=140,y=120)
     b1=Button(window,text="Submit",command=lambda:click1(l),bg="#adebad",activebackground="blue",activeforeground="white").place(x=105,y=180)
     return

window.mainloop()

