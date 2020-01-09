#!/bin/bash

# Kill all process with specified name

PIDS=$(ps aux | grep $1 | awk '{print $2}')

for pid in $PIDS
do
    echo "Killing $pid now"
    kill $pid
done
