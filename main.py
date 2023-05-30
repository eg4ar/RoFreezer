import keyboard
import psutil
import string
import os
import fade
from colorama import Fore



rofreezer = ("""
  _____       ______                          
 |  __ \     |  ____|                         
 | |__) |___ | |__ _ __ ___  ___ _______ _ __ 
 |  _  // _ \|  __| '__/ _ \/ _ \_  / _ \ '__|
 | | \ \ (_) | |  | | |  __/  __// /  __/ |   
 |_|  \_\___/|_|  |_|  \___|\___/___\___|       
                                                 by eg4ar
Press CapsLock to freeze roblox process
""")


os.system("title RoFreezer by egzre, from https://eg4ar.com/")
faded_text = fade.greenblue(rofreezer)
print(faded_text)
print(Fore.RED + "Enabled: False")

pid = None
while pid is None:
        while True:
            for process in psutil.process_iter():
                if process.name() == "RobloxPlayerBeta.exe":
                    pid = process.pid
                    break
            if pid is not None:
                break
            else:
                pass

suspended = False
def toggle_suspension(event):
    global suspended, pid
    try:
        if suspended:
            psutil.Process(pid).resume()
            suspended = False
            os.system("cls")
            print(faded_text)
            print(Fore.RED + "Enabled:", suspended)
        else:
            psutil.Process(pid).suspend()
            suspended = True
            os.system("cls")
            print(faded_text)
            print(Fore.GREEN + "Enabled:", suspended)
    except psutil.NoSuchProcess:
        while True:
            for process in psutil.process_iter():
                if process.name() == "RobloxPlayerBeta.exe":
                    pid = process.pid
                    break
            if pid is not None:
                break
            else:
                pass
keyboard.on_press_key("caps lock", toggle_suspension)
keyboard.wait()
