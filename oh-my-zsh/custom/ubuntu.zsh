run_backup() {
 USB=`mount | grep cryptusb | awk '{print $3}'`
 rsync -av --delete-after /local/ubuntu-backup $USB/
}

alias tz='sudo dpkg-reconfigure tzdata'
alias idg="id | tr ',' '\n'"
alias du-nc="du --exclude=.cache -h"
alias fix-perm="sudo chown -R `id -un`:`id -gn`"
alias ll="ls -alrth"
alias usb="cd `mount | grep cryptusb | awk '{print $3}'`"
