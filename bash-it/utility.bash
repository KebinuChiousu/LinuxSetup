cert-to-json() {
    if [[ -n $1 ]]; then
        awk 'NF {sub(/\r/, ""); printf "%s\\n",$0;}' $1
    else
        echo "Please provide path to certificate!"
    fi
}

