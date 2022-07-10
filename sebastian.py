import pandas as pd
#import numpy as np
#from  socket import *
#open cv
#https://stackoverflow.com/questions/67539425/how-can-i-connect-two-computers-with-python-socket


#https: // dock2learn.com / tech / how - to - upload - files - to - sharepoint - using - python /

from tkinter import *
from tkinter import ttk
from datetime import datetime

root = Tk()
frm = ttk.Frame(root, padding=200)
frm.grid()
ttk.Label(frm, text="rejects").grid(column=0, row=0)
with open('counts.csv', 'a') as the_file:
    the_file.write("time,count T10,count T6,count I2,count I3\n")

countT6= StringVar()
countT10= StringVar()
countI3= StringVar()
countI2= StringVar()
countT6.set('0')
countT10.set('0')
countI3.set('0')
countI2.set('0')



def T10up():
    i=countT10.get()
    countT10.set(int(i)+1)
def T6up():
    i=countT6.get()
    countT6.set(int(i)+1)
def I3up():
    i=countI3.get()
    countI3.set(int(i)+1)
def I2up():
    i=countI2.get()
    countI2.set(int(i)+1)
def submit():
    with open('counts.csv', 'a') as the_file:
        dt=datetime.now()
        the_file.write(f"{dt},{countT10.get()},{countT6.get()},{countI2.get()},{countI3.get()}\n")

ttk.Button(frm, text="T10", command=T10up).grid(column=1, row=0)
ttk.Label(frm, textvariable=countT10).grid(column=1, row=1)

ttk.Button(frm, text="T6", command=T6up).grid(column=2, row=0)
ttk.Label(frm, textvariable=countT6).grid(column=2, row=1)

ttk.Button(frm, text="I3", command=I3up).grid(column=3, row=0)
ttk.Label(frm, textvariable=countI3).grid(column=3, row=1)

ttk.Button(frm, text="I2", command=I2up).grid(column=4, row=0)
ttk.Label(frm, textvariable=countI2).grid(column=4, row=1)

ttk.Button(frm, text="submit", command=submit).grid(column=5, row=0)


root.mainloop()