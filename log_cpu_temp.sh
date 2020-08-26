#!/bin/bash
time=${1:-1}
name=${2:-1}

_file="log/${name}_cpu_temp.txt"

rm $_file


SECONDS=0 
end=$((SECONDS+$time))

while [ $SECONDS -lt $end ]; do
	temp="$(sensors | grep 'Core ' | awk '{print $3}' | sed 's/^.//' | sed 's/..$//' | xargs)" 
	echo $temp | tee -a "$_file"
	sleep 1
done