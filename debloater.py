#!/usr/bin/env python3

import sys 
import os 
import time
import subprocess
import webbrowser


RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
END = '\033[0m'

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
    
        else:
            print("ADB is installed but there is an issue with the version command.")
            print(f"Error: {result.stderr}")
    
    except FileNotFoundError:
        print("ADB is not installed or not found in PATH.")
        print("Trying to install...")
        required_pkg()


def check_device():

    try :
        print("checking for connected devices...")
        subprocess.run(['adb','devices'],)
    except:
        print("Device not found. Try reconnecting again..")
        sys.exit(1)

def package_uninstall():
    package=input("Type the app you want to uninsatll: ")
    package_list=subprocess.run(['adb','shell','pm','list','packages','|','grep',package],stdout=subprocess.PIPE,text=True).stdout.splitlines()
    time.sleep(1)
    print(f"Printing the package names with {package}")
    
    for print_package in package_list :
        print(print_package)
    global pkg_uninstall
    pkg_uninstall = input("please type the package name you want to uninsatll: ")
    subprocess.run(['adb','shell','pm','uninstall','--user','0',pkg_uninstall])

check_adb_installed()
check_device()
package_uninstall()