#!/usr/bin/python
import os
import sys
import shutil
import fnmatch
import subprocess
import argparse

home = os.path.expanduser("~")
sfolder = os.getcwd()

def ensure_dir(path):
    path = os.path.abspath(path)
    if not os.path.exists(path):
        os.makedirs(path)

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

def get_files(path,value):
    matches = []
    for root, dirs, files in os.walk(path):
        for filename in fnmatch.filter(files,value):
            f = root+'/'+filename
            matches.append(f)

    # Sort files alphabetically
    matches.sort()

    return matches

def get_packages():

    #git
    pkg1 = ['git', 'git-gui', 'gitk' ]
    #shell & utilities
    pkg2 = ['zsh', 'vim', 'wget', 'curl', 'xz-utils', 'make']
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

def oh_my_zsh():

    gitdir = os.path.join(home,'git')
    ensure_dir(gitdir)
    omzdir = os.path.join(gitdir,'oh-my-zsh')
    if not os.path.exists(omzdir):
        omz = ['git','clone','https://github.com/robbyrussell/oh-my-zsh.git',omzdir]
        run_script(omz)

    omz = os.path.join(home,'.oh-my-zsh')
    if not os.path.exists(omz):
        cmd = [os.path.join(omzdir,'tools','install.sh')]
        run_script(cmd)

    fontdir = os.path.join(gitdir,'powerline-fonts')
    if not os.path.exists(fontdir):
        # Get powerline fonts
        cmd = ['git','clone','https://github.com/powerline/fonts.git',fontdir]
        run_script(cmd)
    # Install powerline fonts
    cmd = [os.path.join(fontdir,'install.sh')]
    run_script(cmd)

    themedir = os.path.join(omz,'custom','themes','powerlevel9k')
    if not os.path.exists(themedir):
        cmd = ['git', 'clone', 'https://github.com/bhilburn/powerlevel9k.git',themedir]
        run_script(cmd)

    themedir = os.path.join(gitdir,'geany-themes')
    if not os.path.exists(themedir):
	cmd = ['git', 'clone', 'https://github.com/codebrainz/geany-themes.git',themedir]
        run_script(cmd)
    # Install geany themes
    cmd = [os.path.join(themedir,'install.sh')]
    run_script(cmd)

def copy_files():

    zshrc = os.path.join(sfolder,'oh-my-zsh','.zshrc')
    custom = os.path.join(sfolder,'oh-my-zsh','custom')
    target = os.path.join(home,'.oh-my-zsh','custom')
    shutil.copy2(zshrc,os.path.join(home,'.zshrc'))
    zsh = get_files(custom,'*.zsh')
    for f in zsh:
        print(f)
        shutil.copy2(f,target)

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
    # Install oh-my-zsh
    oh_my_zsh()
    # Copy customizations for oh-my-zsh
    copy_files()

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

    parser = argparse.ArgumentParser(
        description=('Configure Linux Desktops: Ubuntu'))

    parser.add_argument('--ubuntu', required=False, action='store_true',
                        help='Configure Ubuntu')

    args = parser.parse_args()

    if args.ubuntu:
        ubuntu()
    else:
        # Call Main Menu
        mainmenu()

if __name__ == "__main__":
    sys.exit(main())
