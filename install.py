#!/usr/bin/python
import os
import sys
import shutil
import fnmatch
import subprocess

def print_menu_item(option,text):

    opt = '%02d' % option

    if sys.version_info[0] == 3:
        print(opt,text)
    else:
        print(opt + ' ' + text)

def get_input(msg):

    ret = ''

    if sys.version_info[0] == 3:
        ret = input(msg)
    else:
        ret = raw_input(msg)

    ret = str(ret)

    return ret

def pause():
    #Wait for user input.
    programPause = get_input("Press the <ENTER> key to continue...")

def run_script(value):

    cmd = None

    if sys.version_info[0] == 2:
        cmd = ''
        for i in value:
            cmd += i
            cmd += ' '
    else:
        cmd = value

    subprocess.call(cmd,shell=True)

def get_packages():

    #git
    pkg1 = ['git', 'git-gui', 'gitk' ]
    #shell & utilities
    pkg2 = ['zsh', 'vim', 'wget', 'curl', 'xz-utils']
    #editor
    pkg3 = ['geany', 'geany-plugins']
    #python
    pkg4 = ['python','python-pip']
    #python3
    pkg5 = ['python3-pip','python3-tk','python3-autopilot']
    #python qt support
    pkg6 = ['python-qt4', 'qt4-designer']
    # sqlite support
    pkg7 = ['sqlitebrowser']

    pkgs = pkg1 + pkg2 + pkg3 + pkg4 + pkg5 + pkg6 + pkg7

    return pkgs

def upgrade_pip():

    # Upgrade pip
    pip = ['sudo','-H','pip','install','--upgrade','pip']
    run_script(pip)
    pip3 = ['sudo','-H','pip3','install','--upgrade','pip']
    run_script(pip3)

def ubuntu():
    cmd = ['sudo','apt-get','update']
    run_script(cmd)
    cmd = ['sudo','apt-get','install','-y']
    # Get list of packages to install
    pkgs = get_packages()
    # Install packages
    run_script(cmd + pkgs)
    # Upgrade pip to latest version
    upgrade_pip()

def mainmenu():

    while True:
        menu = {}
        menu[1] = "Ubuntu"
        menu[2] = "Exit"
        options=menu.keys()
        _=os.system("clear")
        print("Linux Desktop Setup Utility")
        print('')
        for entry in options:
            print_menu_item(entry, menu[entry])
        print('')
        selection = get_input("Please Select: ")
        print (selection)
        if selection == '1':
            ubuntu()
            pause()
        elif selection == '2':
            break
        else:
            print("Unknown Option Selected!")
            pause()

def main():

    #Call Main Menu
    mainmenu()

if __name__ == "__main__":
    sys.exit(main())
