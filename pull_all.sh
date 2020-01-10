#!/bin/bash

apk_files=$(adb shell ls $1/*.apk)

for apk in $apk_files
do
    echo "Pulling $apk"
    adb pull $apk $2

    echo "Removing $apk"
    adb shell rm $apk
done

