#!/bin/bash
current_user=$(whoami)
echo "$current_user: $current_user"
current_dir=$(pwd)
echo "Your in this folder: $current_dir"
current_date=$(date)
echo "Today is $current_date"

disk_space=$(df -h)
echo "The disk used is: $disk_space"

memory_usage=$(free -h)
echo "The memory used is: $memory_usage"


