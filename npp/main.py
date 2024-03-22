import os 
import subprocess
prog = "notepad++.exe"
install_command = "sudo apt install wine"
#opens the program
dbg = os.system(f"wine {prog }")
# Debug
if dbg == "sh: 1: wine: not found":
    print("[-]Error! you need to install wine ")
