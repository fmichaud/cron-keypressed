import win32com.client
from time import sleep

while True:
  shell = win32com.client.Dispatch("WScript.Shell")
  shell.SendKeys("+")
  print("LSHIFT keypressed")
  sleep(60)


