#!/bin/bash
mkdir -p logs
timestamp=$(date)
echo "Script exected at $timestamp"
tail -n 5 logs
wc -l < logs

