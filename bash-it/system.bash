function get_distro() {
	cat /etc/os-release | grep ^ID= | awk -F'=' '{print $2}'
}

function list_groups() {
	id | tr ',' '\n'
}

alias distro=get_distro
alias idg=list_groups
alias du-nc='du --exclude=.cache -h'
alias fix-perm='sudo chown -R $(id -un):$(id -gn)'
alias ll='ls -alrth'
alias disk-free="df -h | grep -v tmpfs | grep -v loop"
