#!/usr/bin/python
"""Simple wrapper script for squeezeslave.exe

Can be run without a window"""

import getmac
#import subprocess
import os
#
#find existing process
import wmi
c = wmi.WMI ()
for process in c.Win32_Process ():
    if process.name == "squeezeslave.exe":
        print process.name, "already running"
        quit()
#launch a new one
#print getmac.maclist()
#subprocess.call(["squeezeslave.exe", "-F", "--retry", "--mac", getmac.maclist()[0]])
#import win32api
#win32api.WinExec('
print "launch!"
os.popen("squeezeslave.exe -F --retry --mac %s" % (getmac.maclist()[0],))
