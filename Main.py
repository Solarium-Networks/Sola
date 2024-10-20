import platform
import os
import subprocess

base_dir = os.path.dirname(__file__)

if platform.system() == "Windows":
  cmd_location = os.path.join(base_dir, "commandline.py")
else:
  cmd_location = os.path.join(base_dir, "commandline.py")

if platform.system() == "Windows":
  ui_location = os.path.join(base_dir, "ui.py")
else:
  ui_location = os.path.join(base_dir, "ui.py")

option = input("Welcome to Sola! would you like to use the simple command line player or the UI player? [cmd/ui]: ")
if option == "cmd":
  subprocess.run(['python3', cmd_location])
if option == "ui":
  subprocess.run(['python3', ui_location])
