from tkinter import *

s = m = a = p = 0

#Start
def Nothing():
    j = 0


def Go():
    global s, m, a, Start, p
    a = 1
    if p == 0:
        if s < 60:
            s = s + 1
        else:
            m = m + 1
            s = 0
        if s < 10 and m < 10:
            Num.configure(text='0'+str(m) + ':' + '0'+str(s))
        elif s < 10:
            Num.configure(text=str(m) + ':' + '0' + str(s))
        elif m < 10:
            Num.configure(text='0'+str(m) + ':' + str(s))
        else:
            Num.configure(text=str(m)+':'+str(s))
        Start.configure(command=Nothing)
        W.after(1000, Go)
    elif p != 0:
        p = 0
        a = 0


#Reset
def Reseting():
    global a, s, m, p, Start
    if a == 1:
        s = m = 0
        p = 1
        Num.configure(text='00:00')
        Start.configure(command=Go)
        a = 0
    elif a == 0:
        s = m = 0
        Num.configure(text='00:00')
        Start.configure(command=Go)


#Stop
def Stoping():
    global p, a
    if a == 1:
        p = 2
        Start.configure(command=Go)


W = Tk()
W.geometry('400x250')
W.title = 'Timer'

down = Frame(W).pack()
up = Frame(W).pack(side='top')
Check = IntVar()

global Num
Num = Label(text='00:00', font='normal 100')
Num.place(x=30, y=20)


Start = Button(up, text='Start', font='normal 16', bg='green', command=Go, height=2, width=5)
Start.place(x=160, y=180)
Stop = Button(up, text='Stop', font='normal 16', bg='red', command=Stoping, height=2, width=5).place(x=80, y=180)
Reset = Button(up, text='Reset', font='normal 16', bg='gray', command=Reseting, height=2, width=5).place(x=240, y=180)

W.mainloop()