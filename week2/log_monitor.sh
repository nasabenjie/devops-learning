#!/bin/bash
mkdir -p logs

log_file="logs/activity.log"
timestamp=$(date)

echo "Script executed at $timestamp" >> $log_file

echo "Last 5 entries:"
tail -n 5 $log_file

echo "Total times script has run:"
wc -l < $log_file
