#!/bin/bash

for line in  `awk '{print $1}' students_list.txt`
do
name=$(echo $line|cut -f1 -d#)
password=$(echo $line|cut -f2 -d#)
echo $name
echo $password
done
