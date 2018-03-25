# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 22:10:31 2018

@author: Mik
"""
from datetime import datetime
import wmi
import csv
from tkinter import *
import os
from datetime import datetime, timedelta, timezone



import pytz

import subprocess
import time



ip = 'n036-d'
username = r'artefactory\administrator'
password = r'/SoGoodToRemember2013_'

c=wmi.WMI(ip, user=username, password=password)
os = c.Win32_OperatingSystem (Primary=1)[0]
os.Reboot ()

#d=c.query("SELECT * FROM Win32_PerfFormattedData_Counters_ProcessorInformation")                         
#print(d[0])

#watcher = c.Win32_Process.watch_for("modification")
#event = watcher()
#print "Modification occurred at", event.timestamp


#commanddelB = r'schtasks	/Delete /S {} /U artefactory\administrator /P /SoGoodToRemember2013_ /TN serverbackburner /F'.format(ip)
#commandB = r'schtasks /Create  /S {} /SD 24/03/2017 /ST 16:50 /SC ONCE /U artefactory\administrator /TN serverbackburner /P /SoGoodToRemember2013_ /TR "C:\Program Files (x86)\Autodesk\Backburner\server.exe"'.format(ip)
#commandrunB = r'schtasks /Run  /S {} /U artefactory\administrator /TN serverbackburner /P /SoGoodToRemember2013_ '.format(ip)
#
#subprocess.run(commanddelB)
#subprocess.run(commandB)
#subprocess.run(commandrunB)
    

#commanddelV = r'schtasks	/Delete /S {} /U artefactory\administrator /P /SoGoodToRemember2013_ /TN vrayspawner /F'.format(ip)
#commandV = r'schtasks /Create  /S {} /SD 24/03/2017 /ST 16:50 /SC ONCE /U artefactory\administrator /TN vrayspawner /P /SoGoodToRemember2013_ /TR "\"C:\Program Files\Autodesk\3ds Max 2017\vrayspawner2017.exe"\"'.format(ip)
#commandrunV = r'schtasks /Run  /S {} /U artefactory\administrator /TN vrayspawner /P /SoGoodToRemember2013_ '.format(ip)
#
#subprocess.run(commanddelV)
#subprocess.run(commandV)
#subprocess.run(commandrunV)


# =============================================================================
#schtasks /Create  /S poste-arte13 /SD 24/03/2018 /SC ONCE /U artefactory\administrator /TN serverbackburner /P /SoGoodToRemember2013_ /TR "C:\Program Files (x86)\Autodesk\Backburner\server.exe" /ST 17:10 
#
#schtasks	/Delete /S poste-arte13 /U artefactory\administrator /P /SoGoodToRemember2013_ /TN serverbackburner /F
# schtasks /Create  /S poste-arte13 /SD 24/03/2018 /SC ONCE /U artefactory\administrator /TN serverbackburner /P /SoGoodToRemember2013_ /TR "C:\Program Files\Autodesk\3ds Max 2017\vrayspawner2017.exe" /ST 16:50
# schtasks	/Run /S poste-arte13 /U artefactory\administrator /P /SoGoodToRemember2013_ /I /TN serverbackburner 
# =============================================================================

