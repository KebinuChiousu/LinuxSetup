#!/usr/bin/python
import os
import sys
import shutil
import fnmatch
import subprocess

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

def ubuntu():
    cmd = ['sudo','apt-get','update']
    run_script(cmd)
    cmd = ['sudo','apt-get','install','-y']
    #git
    pkg1 = ['git', 'git-gui', 'gitk' ]
    #shell
    pkg2 = ['zsh']
    #editor
    pkg3 = ['geany', 'geany-plugins']
    #python
    pkg4 = ['python-pip','python3-pip']
    #install packages
    run_script(cmd + pkg1 + pkg2 + pkg3 + pkg4)


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
            opt = '%02d' % entry
            print opt, menu[entry]
        print('')
        selection = get_input("Please Select: ")
        print selection
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
