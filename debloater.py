#!/usr/bin/env python3

import sys 
import time
import subprocess
import webbrowser


RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
END = '\033[0m'

def intro():
    print(f"""{RED}

          
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

    {END}    """)         

pkg_uninstall = None

def required_pkg():

    print("Installing required packages...")
    time.sleep(1)
    distro = subprocess.run(['lsb_release','-is'],stdout=subprocess.PIPE,text=True).stdout.strip().lower()
    if "ubuntu" in distro or "kali" in distro or "debian" in distro :
        subprocess.run(['sudo', 'apt', 'update'], check=True)
        subprocess.run(['sudo', 'apt', 'install', 'adb', '-y'], check=True)
    
    elif "arch" in distro or "manjaro" in distro :
        subprocess.run(['sudo', 'pacman', '-S', 'android-tools', '--noconfirm'], check=True)
    else:
        print(f"Unknown or unsupported Linux distribution: {distro}")
        print("Please install ADB manually.")
        
def check_adb_installed():

    try:
        result = subprocess.run(['adb', 'version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if result.returncode == 0:
            print("ADB is installed.")
            time.sleep(1)
    
        else:
            print("ADB is installed but there is an issue with the version command.")
            print(f"Error: {result.stderr}")
    
    except FileNotFoundError:
        print("ADB is not installed or not found in PATH.")
        print("Trying to install...")
        required_pkg()

def check_device():

    try :
        print(f"{GREEN}Checking for connected devices...{END}")
        {YELLOW}
        process =subprocess.run(['adb','devices'],stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
        {END}
        if "device" not in process.stdout():
            print(f"{RED}NO DEVICE FOUND TRY AGAIN..{END}")
            sys.exit(1)
    except:
        print(f"{RED}Device not found. Try reconnecting again..{END}")
        sys.exit(1)

def package_uninstall():

    package=input(f"{GREEN}Type the app you want to uninsatll: {END}")
    package_list=subprocess.run(['adb','shell','pm','list','packages','|','grep',package],stdout=subprocess.PIPE,text=True).stdout.splitlines()
    time.sleep(1)
    print(f"{YELLOW}Printing the package names with {package}{END}")
    {GREEN}
    for print_package in package_list :
        print(print_package)
    {END}    
    global pkg_uninstall

    pkg_uninstall = input(f"{YELLOW}Please type the package name you want to uninsatll: {END}")
    subprocess.run(['adb','shell','pm','uninstall','--user','0',pkg_uninstall])

def github():
    git=input(f"{GREEN}Wanna visit my GitHub?(y/n):")
    if git == 'y':
        webbrowser.open_new("https://github.com/mtm-x")
    else:
        subprocess.run(['clear'])
        print(f"{RED}BYE BYE{END}")
        time.sleep(1)
        sys.exit(0)    

intro()
check_adb_installed()
check_device()
package_uninstall()
github()