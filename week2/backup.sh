#!/bin/bash
echo "Enter the folder name you want to backup"
read folder_name

if [ -d  "$folder_name" ]
then
        echo "folder found. Proceeding with backup."
	echo "Enter the name of your backup"
	read backup_name
	mkdir -p ~/backups
	cp -r $folder_name ~/backups/${backup_name}_$(date +%Y%m%d)
	echo "Backed up $folder_name to ~/backups/${backup_name}_$(date +%Y%m%d)"
	echo "This is what was backed up:",
	ls -l ~/backups
else
	echo "Folder $folder_name does not exist. Please check the name."
fi
