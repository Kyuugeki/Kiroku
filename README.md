# Kiroku
Kiroku is a simple, but efficient keylogger for UNIX systems written in Python

It basically records evey keystroke and automatically write them into a file in Google Drive using the IFTTT API
This project's main goal was to understand the API by itself and keyboard events in Linux. This project is initially private, but i'll turn this public soon

# Usage

First of all, you should create an IFTTT and a Google account. Then next, you need to create a new applet. Follow the next steps to create a new applet:

1) Go to “My Applets”and create a new applet by clicking the “New Applet” button.
2) Click on the “this” word that is in a blue color
3) Search for the “Webhooks” service and select the Webhooks icon.
4) Choose the “Receive a web request” trigger.
5) Give a name to the event. Then, click the “Create trigger” button.
6) Click the “that” word to proceed.
7) Search for the “Google Docs” service, and select the Google Docs icon.
8) Select "Append to a document"
9) Now you need to change the Content field. Just paste this:
 
 <code> "{{OccurredAt}}
{{Value1}}"
  </code> <br>
  You can also add HTML line breaks <"br"> 
  
  The last step is to get your API key at <code> https://ifttt.com/maker_webhooks</code><br>
  You'll need to provide the event name you've created before, and your API key in the code
  
  After that, the keylogger is ready to go!
  You can test it in the terminal, and also run it in the background using the <code>/etc/rc.local</code> script
  
  A version for Windows using PyHook will be also released soon
  Hope you guys enjoy it and help the project to grow!
