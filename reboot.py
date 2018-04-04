# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 20:47:22 2018

@author: Mik
"""
import wmi
import csv
from tkinter import *
import os
import subprocess
import threading
ip2 = 'n042-b'
username = r'artefactory\administrator'
password = r'/SoGoodToRemember2013_'
c = wmi.WMI(ip2,  password=password, privileges=["RemoteShutdown"])

os = c.Win32_OperatingSystem (Primary=1)[0]
os.Reboot ()