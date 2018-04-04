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
import threading

chkburn = []
chkspawn = []
conn = []
i = 0



master = Tk()
class Timeout():
    """Timeout class using ALARM signal."""
    class Timeout(Exception):
        pass

    def __init__(self, sec):
        self.sec = sec

    def __enter__(self):
        signal.signal(signal.SIGALRM, self.raise_timeout)
        signal.alarm(self.sec)

    def __exit__(self, *args):
        signal.alarm(0)    # disable alarm

    def raise_timeout(self, *args):
        raise Timeout.Timeout()
        
        

def togglespawn(connection,ip):
    if connection.Win32_Process (name = "vrayspawner2017.exe"): #DETECTE SPAWNER
        stopspawner(connection)
        return
    startspawner(ip)      
    return

def toggleburn(connection, ip):
    if connection.Win32_Process (name = "server.exe"):  #DETECTE SPAWNER
        stopburn(connection)
        return
    startburn(ip)  
    return

def spawntest(connection, button):
    if connection.Win32_Process (name = "vrayspawner2017.exe"):   #DETECTE SPAWNER
        button.select()
        return  
    return
    
def burntest(connection, button):
    if connection.Win32_Process (name="server.exe"):   #DETECTE SPAWNER
        button.select()
        return
    return
    
    
def startspawner(ip):    
#    commanddelV = r'schtasks	/Delete /S {} /U artefactory\administrator /P /SoGoodToRemember2013_ /TN vrayspawner /F'.format(ip)
    commandV = r'schtasks /Create  /S {} /SD 24/03/2017 /ST 16:50 /SC ONCE /U artefactory\administrator /TN vrayspawner /P /SoGoodToRemember2013_ /F /TR "\"C:\Program Files\Autodesk\3ds Max 2017\vrayspawner2017.exe"\"'.format(ip)
    commandrunV = r'schtasks /Run  /S {} /U artefactory\administrator /TN vrayspawner /P /SoGoodToRemember2013_ '.format(ip)
    
#    subprocess.run(commanddelV)
    subprocess.run(commandV)
    subprocess.run(commandrunV)
    
def stopspawner(connection): 
    for process in connection.Win32_Process(name = "vrayspawner2017.exe"): process.Terminate ()  #STOP SPAWNER
    
def startburn(ip):
#    commanddelB = r'schtasks	/Delete /S {} /U artefactory\administrator /P /SoGoodToRemember2013_ /TN serverbackburner /F'.format(ip)
    commandB = r'schtasks /Create  /S {} /SD 24/03/2017 /ST 16:50 /SC ONCE /U artefactory\administrator /TN serverbackburner /P /SoGoodToRemember2013_  /F /TR "\"C:\Program Files (x86)\Autodesk\Backburner\server.exe"\"'.format(ip)
    commandrunB = r'schtasks /Run  /S {} /U artefactory\administrator /TN serverbackburner /P /SoGoodToRemember2013_ '.format(ip)
    
#    subprocess.run(commanddelB)
    subprocess.run(commandB)
    subprocess.run(commandrunB)
    
def stopburn(connection):
    for process in connection.Win32_Process(name = "server.exe"):  process.Terminate ()  #STOP BACKBURNER
   

def refresh():
    
    for i in range(len(conn)):
            
        if conn[i].Win32_Process (name = "vrayspawner2017.exe"):   #DETECTE SPAWNER
            chkspawn[i].select()
        else:
            chkspawn[i].deselect()
              
        if conn[i].Win32_Process (name="server.exe"):   #DETECTE SPAWNER
            chkburn[i].select()
        else:
            chkburn[i].deselect()
            
    return
        



def pingOk(sHost):
    try:
        subprocess.check_output("ping -n 1 {} ".format(sHost), shell=False)

    except Exception as e:
        return 0

    return 1
    

    
with open('Local Data Source.csv', newline='') as f:
    reader = csv.reader(f)
    machinetemp =[', '.join(row) for row in reader]
    

for x in machinetemp:
    
    try:
             
    
        ip2 = x
        username = r'artefactory\administrator'
        password = r'/SoGoodToRemember2013_'
        
        conn.append(wmi.WMI(ip2, user=username, password=password))
    
    except :
        continue
                
 
    
    
    labelmachine = Label(master, text = ip2)
    labelmachine.grid(row=i)
    
    
    
    chkspawn.append(Checkbutton(master, text="VraySpawner", command = lambda i=i, x=x: togglespawn(conn[i],  x)))
    spawntest(conn[i], chkspawn[i])
    
    chkburn.append(Checkbutton(master, text="backburner", command = lambda i=i, x=x: toggleburn(conn[i],  x)))
    burntest(conn[i], chkburn[i])

    
    chkspawn[i].grid(row=i, column=2)
    chkburn[i].grid(row=i, column=3)
 
    
    
      
    i+=1

bb = Button(master, text="Refresh", command=refresh)
bb.grid(row=1,column=4)

      


mainloop()