# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import wmi
import csv
from tkinter import *
import os
import subprocess

chkburn = []
chkspawn = []
conn = []
i = 0



master = Tk()


def togglespawn(connection, button, ip):
    if connection.Win32_Process (name = "vrayspawner2017.exe"): #DETECTE SPAWNER
        stopspawner(connection)
        return
    startspawner(connection, ip)      
    return

def toggleburn(connection, button, ip):
    if connection.Win32_Process (name = "server.exe"):  #DETECTE SPAWNER
        stopburn(connection)
        return
    startburn(connection, ip)  
    return

def spawntest(connection, button):
    if connection.Win32_Process (name = "vrayspawner2017.exe"):   #DETECTE SPAWNER
        chkspawn[button].select()
        return  
    return
    
def burntest(connection, button):
    if connection.Win32_Process (name="server.exe"):   #DETECTE SPAWNER
        chkburn[button].select()
        return
    return
    
    
def startspawner(connection, ip):    
    commanddelV = r'schtasks	/Delete /S {} /U artefactory\administrator /P /SoGoodToRemember2013_ /TN vrayspawner /F'.format(ip)
    commandV = r'schtasks /Create  /S {} /SD 24/03/2017 /ST 16:50 /SC ONCE /U artefactory\administrator /TN vrayspawner /P /SoGoodToRemember2013_ /TR "\"C:\Program Files\Autodesk\3ds Max 2017\vrayspawner2017.exe"\"'.format(ip)
    commandrunV = r'schtasks /Run  /S {} /U artefactory\administrator /TN vrayspawner /P /SoGoodToRemember2013_ '.format(ip)
    
    subprocess.run(commanddelV)
    subprocess.run(commandV)
    subprocess.run(commandrunV)
    
def stopspawner(connection): 
    for process in connection.Win32_Process(name = "vrayspawner2017.exe"): process.Terminate ()  #STOP SPAWNER
    
def startburn(connection, ip):
    commanddelB = r'schtasks	/Delete /S {} /U artefactory\administrator /P /SoGoodToRemember2013_ /TN serverbackburner /F'.format(ip)
    commandB = r'schtasks /Create  /S {} /SD 24/03/2017 /ST 16:50 /SC ONCE /U artefactory\administrator /TN serverbackburner /P /SoGoodToRemember2013_ /TR "\"C:\Program Files (x86)\Autodesk\Backburner\server.exe"\"'.format(ip)
    commandrunB = r'schtasks /Run  /S {} /U artefactory\administrator /TN serverbackburner /P /SoGoodToRemember2013_ '.format(ip)
    
    subprocess.run(commanddelB)
    subprocess.run(commandB)
    subprocess.run(commandrunB)
    
def stopburn(connection):
    for process in connection.Win32_Process(name = "server.exe"):  process.Terminate ()  #STOP BACKBURNER
   




    
with open('Local Data Sourcebig.csv', newline='') as f:
    reader = csv.reader(f)
    machinetemp =[', '.join(row) for row in reader]
    

for x in machinetemp:

    ip2 = x
    username = r'artefactory\administrator'
    password = r'/SoGoodToRemember2013_'
    
    conn.append(wmi.WMI(ip2, user=username, password=password))
    
    
    labelmachine = Label(master, text = ip2)
    labelmachine.grid(row=i)
    
    
    
    chkspawn.append(Checkbutton(master, text="VraySpawner", command = lambda i=i: togglespawn(conn[i], i, machinetemp[i])))
    spawntest(conn[i], i)
    
    chkburn.append(Checkbutton(master, text="backburner", command = lambda i=i: toggleburn(conn[i], i, machinetemp[i])))
    burntest(conn[i], i)

    
    chkspawn[i].grid(row=i, column=2)
    chkburn[i].grid(row=i, column=3)

      
      
    i+=1

mainloop()