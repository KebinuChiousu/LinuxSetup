export SSH_AUTH_SOCK=$HOME/.ssh/ssh_auth_sock

# export SSH_AUTH_SOCK=/run/user/$(id -u)/keyring/ssh

kill-agents()
{
    for i in $(ps -ef | grep ssh-agent | grep ssh_auth_sock | grep -v grep | awk '{print $2}')
    do
        kill -9 $i
    done
}

reset_ssh()
{
    kill-agents
}

get_opensc_path()
{
    DISTRO=$(cat /etc/os-release | grep ^ID= | awk -F'=' '{print $2}')

    echo $DISTRO

    if [ "$DISTRO" == "ubuntu" ]
    then
        OPENSC_LIB="/usr/lib/x86_64-linux-gnu/opensc-pkcs11.so"
    else
        OPENSC_LIB="/usr/lib/opensc-pkcs11.so"
    fi
}

init_ssh()
{

    get_opensc_path

    AGENT=$(ps aux | grep "ssh-agent -a" | grep -v grep | wc -l)
    if [ $AGENT -eq 0 ]
    then
      rm $HOME/.ssh/ssh_auth_sock
      ssh-agent -a $HOME/.ssh/ssh_auth_sock
    fi

    # ssh-add -D

    KEY=$(ssh-add -l | grep opensc-pkcs11.so | wc -l)
    if [ $KEY -eq 0 ]
    then
      # Yubikey PIV Setup (YubiKey5 or NEO)
      TOKEN=$(lsusb | grep "1050:" | grep -v "1050:0403" | wc -l)
      if [ $TOKEN -eq 1 ]
      then
        echo "PIV Token"
        ssh-add -s $OPENSC_LIB
      else
        echo "Unable to find YubiKey5 or Yubikey NEO."
      fi
    fi

    ssh-add -l
}

alias ssh-init=init_ssh
alias ssh-reset=reset_ssh
