#!/bin/bash

name="COG"
course="Devops"
university="ISBAT"
date_today=$(date)
time_today=$(date +%T)
files=$(ls)


echo "Name: $name"
echo "Course: $course"
echo "University: $university"
echo "Time: $time_today"
echo "Today: $date_today"
echo "Files in this folder"

echo "$files"

