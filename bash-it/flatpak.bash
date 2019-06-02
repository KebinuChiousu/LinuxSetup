kill_steam() {
    for i in $(ps aux | grep steam | grep -v grep | awk '{print $2}')
    do
      kill -9 $i
    done
}

alias kill-steam=kill_steam
