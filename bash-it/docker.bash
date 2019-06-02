export DOCKER_HOST=unix:///var/run/docker.sock

dockervol() {
 for i in $(docker volume ls | grep local | awk '{print $2}')
 do
   VOL=$(docker inspect $i | grep Mountpoint | awk -F ':' '{print $2}' | sed 's|"||g' | sed 's|,||g')
   echo "Name: " $i
   echo "Type: local"
   echo "Vol:  " $VOL
   echo "---"
 done
}

alias docker-files=dockervol
