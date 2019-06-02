shuf() { python -c '
import sys, random, fileinput; from signal import signal, SIGPIPE, SIG_DFL;    
signal(SIGPIPE, SIG_DFL); lines=[line for line in fileinput.input()];   
random.shuffle(lines); sys.stdout.write("".join(lines))
' "$@"; }

alias shuffle="shuf"
