# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 18:03:11 2018

@author: Mik
"""
import threading, time
from datetime import datetime
import wmi
import csv
from tkinter import *
import os
from datetime import datetime, timedelta, timezone
import pythoncom
global v
root = Tk()
v = StringVar()
lab = Label(root,  textvariable=v )
lab.pack()
v.set("New Text!")


x = "aaa"
#def func1():
#    for j in range (300):
#       
#       
#        print(x)
#        time.sleep(0.1)
        
ip = 'n036-d'
username = r'artefactory\administrator'
password = r'/SoGoodToRemember2013_'



pythoncom.CoInitialize()
c=wmi.WMI(ip, user=username, password=password)
process_watcher = c.Win32_Process.watch_for("creation")
#new_process = process_watcher()
#x="retrieved" + str(new_process.caption)
#g=(process_watcher().Caption)
#print(g)


#t1 = threading.Thread(target = func1)
#t2 = threading.Thread(target = func2)
#t1.start()
#t2.start()
#t1.join()
#t2.join()

mainloop()