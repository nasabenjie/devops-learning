#!/bin/bash
echo "Enter the folder name you want to backup"
read folder_name
if [ $folder_name ]
then
        echo "Thank you"
else
        
        echo "folder_name doesn't exit"
fi
echo "Enter the name of your backup"
read backup_name
mkdir -p $backup_name
if [ -d "backup_name" ]
then
	echo "backupname folder exists"
else
	mkdir -p $backupname
	echo "Backupname folder created"
fi
echo "This is what was backed up
ls-l $backupname


