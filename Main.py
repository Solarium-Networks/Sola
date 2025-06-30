import platform
import os
import subprocess

base_dir = os.path.dirname(__file__)

if platform.system() == "Windows":
  ui_location = os.path.join(base_dir, "ui.py")
else:
  ui_location = os.path.join(base_dir, "ui.py")

subprocess.run(['python3', ui_location])
