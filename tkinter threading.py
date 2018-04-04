# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 20:28:30 2018

@author: Mik
"""
import wmi
from tkinter import *
import threading
import pythoncom


ip = 'localhost'

class App(threading.Thread):

    def __init__(self, tk_root):
        
        self.root = tk_root
        threading.Thread.__init__(self)
        
        self.start()

    def run(self):
        
        pythoncom.CoInitialize()
        c=wmi.WMI(ip)
        process_watcher = c.Win32_Process.watch_for("creation")
        
        while True :
            new_process = process_watcher()         
            
            x = new_process.Caption
       
            label = Label(self.root, text=x)
            label.pack()
                


ROOT = Tk()
APP = App(ROOT)
LABEL = Label(ROOT, text="Hello, world!")
LABEL.pack()
ROOT.mainloop()