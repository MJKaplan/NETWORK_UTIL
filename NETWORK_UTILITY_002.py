# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import wmi
import csv
from tkinter import *
import os
import datetime


hosts = []



master = Tk()
var = IntVar()
nommachine = StringVar()


def togglespawn():
#    print("test")
    for process in connection.Win32_Process ():   #DETECTE SPAWNER
        if process.name == "vrayspawner2017.exe":
            stopspawner()
            chkspawn.deselect()
            return
    startspawner()        
    chkspawn.select()
    return

def spawntest():
    for process in connection.Win32_Process ():   #DETECTE SPAWNER
        if process.name == "vrayspawner2017.exe":
#            stopspawner()
            chkspawn.select()
            return
#    startspawner()        
    chkspawn.deselect()

def toggleburn():
#    print("test")
    for process in connection.Win32_Process ():   #DETECTE SPAWNER
        if process.name == "server.exe" :
            stopburn()
            chkburn.deselect()
            return
    startburn()        
    chkburn.select()
    return
def burntest():
    #    print("test")
    for process in connection.Win32_Process ():   #DETECTE SPAWNER
        if process.name == "server.exe" :
            chkburn.select()
            return
    chkburn.deselect()
    return
    
    
def startspawner():    
    connection.Win32_Process.Create (CommandLine=r"C:\Program Files\Autodesk\3ds Max 2017\vrayspawner2017.exe")  #START SPAWNER 
def stopspawner(): 
    for process in connection.Win32_Process(name = "vrayspawner2017.exe"): process.Terminate ()  #STOP SPAWNER
def startburn():
    connection.Win32_Process.Create(CommandLine=r"C:\Program Files (x86)\Autodesk\Backburner\server.exe")
#    connection.Win32_Process.Create(CommandLine=r"C:\Program Files\Autodesk\3ds Max 2017\maxadapter.adp.exe")
def stopburn():
    for process in connection.Win32_Process(name = "server.exe"):  process.Terminate () 
    for process in connection.Win32_Process(name = "maxadapter.adp.exe"):  process.Terminate () #STOP BACKBURNER
   


    

#HOSTS. Toutes les machines du réseau sont stockées dans l'array hosts, qui est créé en 
#lisant le fichier LocalSource.csv
#
#with open('LocalSource.csv', newline='') as f:
#    reader = csv.reader(f)
#    for row in reader:
#        machinetemp =', '.join(row)
#



#CONNECTION RESEAU 

            
ip = 'poste-arte13'
username = r'artefactory\administrator'
password = r'/SoGoodToRemember2013_'


connection = wmi.WMI(ip, user=username, password=password)


labelmachine = Label(master, text = ip)
labelmachine.pack()
chkspawn = Checkbutton(master, text="VraySpawner", command = togglespawn)
spawntest()
chkburn = Checkbutton(master, text="backburner", command = toggleburn)
burntest()

#startup = connection.Win32_ProcessStartup.new()


chkspawn.pack()
chkburn.pack()








    










#PROCESS WATCHER

#process_watcher = connection.Win32_Process.watch_for("creation")
#while True:
#  new_process = process_watcher()
#  print (new_process.Caption)
#

#STOP SERVICE
  
#c = wmi.WMI()
#for service in c.Win32_Service(Name="seclogon"):
#  result, = service.StopService()
#  if result == 0:
#    print "Service", service.Name, "stopped"
#  else:
#    print "Some problem"
#  break
#else:
#  print "Service not found"





mainloop()