import platform
import os
import subprocess

def get_username():
  if platform.system() == "Windows":
    return os.getlogin()  # or os.environ['USERNAME']
  else:
    return os.getenv('USER')

username = get_username()

if platform.system() == "Windows":
  cmd_location = rf'C:\Users\{username}\downloads\Sola-1.1\commandline.py'
else:
  cmd_location = f'/home/{username}/downloads/Sola-1.1/commandline.py'

if platform.system() == "Windows":
  ui_location = rf'C:\Users\{username}\downloads\Sola-1.1\ui.py'
else:
  ui_location = f'/home/{username}/downloads/Sola-1.1/ui.py'

option = input("Welcome to Sola! would you like to use the simple command line player or the UI player? [cmd/ui]: ")
if option == "cmd":
  subprocess.run(['python3', cmd_location])
if option == "ui":
  subprocess.run(['python3', ui_location])
