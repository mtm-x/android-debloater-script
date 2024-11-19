#!/usr/bin/env python3

import sys 
import time
import subprocess
import webbrowser


RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
END = '\033[0m'

class adb():
    def __init__(self):
         print(rf"""{RED}

          
                            _           _     _   _____       _     _             _            
            /\             | |         (_)   | | |  __ \     | |   | |           | |           
           /  \   _ __   __| |_ __ ___  _  __| | | |  | | ___| |__ | | ___   __ _| |_ ___ _ __ 
          / /\ \ | '_ \ / _` | '__/ _ \| |/ _` | | |  | |/ _ \ '_ \| |/ _ \ / _` | __/ _ \ '__|
         / ____ \| | | | (_| | | | (_) | | (_| | | |__| |  __/ |_) | | (_) | (_| | ||  __/ |   
        /_/    \_\_| |_|\__,_|_|  \___/|_|\__,_| |_____/ \___|_.__/|_|\___/ \__,_|\__\___|_|      
          




                                            WRITTEN BY                                 
 
 
                                        ,d                                             
                                        88                                             
                   88,dPYba,,adPYba, MM88MMM 88,dPYba,,adPYba,         8b,    ,d8  
                  88P     88      8a  88     88P   88      8a  aaaaaaaa Y8, ,8P   
                  88      88      88  88     88    88      88  aaaaaaaa  )888(    
                  88      88      88  88,    88    88      88          ,d8   8b,  
                  88      88      88   Y888  88    88      88         8P       Y8 
    
                                              (GitHub)                                

     {END}""")    
    def adb_device(self):
        try :
            print(f"{GREEN}Checking for connected devices...{END}")
            {YELLOW}
            process =subprocess.run(['adb','devices'],stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
            {END}
            if "device" not in process.stdout:
                print(f"{RED}NO DEVICE FOUND TRY AGAIN..{END}")
                sys.exit(1)
        except:
            print(f"{RED}Device not found. Try reconnecting again..{END}")
            sys.exit(1)
    def adb_uninstall(self,app_name):
        self.app_name=app_name
        package_list=subprocess.run(['adb','shell','pm','list','packages','|','grep',self.app_name],stdout=subprocess.PIPE,text=True).stdout.splitlines()
        time.sleep(1)
        print(f"{YELLOW}Printing the package names with {self.app_name}{END}")
        {GREEN}
        for print_package in package_list :
            print(print_package)
        {END}
        self.package = input(f"{YELLOW}Please type the package name you want to uninsatll: {END}")
        subprocess.run(['adb','shell','pm','uninstall','--user','0',self.package])
    def github(self,git):
        self.git=git
        if self.git == "y" or "Y":
            webbrowser.open_new("https://github.com/mtm-x")
        else:
            subprocess.run(['clear'])
            print(f"{RED}BYE BYE{END}")
            time.sleep(1)
            sys.exit(0)  

adbdevice = adb()
adbdevice.adb_device()
adbdevice.adb_uninstall(input(f"{GREEN}Type the app you want to uninsatll: {END}"))
adbdevice.github(input(f"{GREEN}Wanna visit my GitHub?(y/n):"))

