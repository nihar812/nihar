#!/bin/bash

For $'@.txt' 

mv '@.txt' -p /home/ubuntu/practice/files/new

do

rename 's/*.txt/ACST_s1_2018_'$@'.txt/' *.txt

echo "Moved file to new directory"

done

 
