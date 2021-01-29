# Veeambackup
Veeam Agent for Windows Backup w/ Windows Task Scheduler

This is a python project which automates the backup to a NAS location once keyless SSH has been established with the destination. To install this project follow the following steps:

1. Set up NAS and share. Here is a simple guide. One call for windows users, make sure to enable SMB1.0. https://medium.com/@aallan/adding-an-external-disk-to-a-raspberry-pi-and-sharing-it-over-the-network-5b321efce86a
2. Download / Install Veeam Agend for Windows (This is a free service from Veeam). https://www.veeam.com/windows-endpoint-server-backup-free.html
3. Set up a backup job from the Veeam Agent for Windows GUI and backup for the first time. This will be a full backup, and subsequent backups will be incremental when the python script is triggered. 
4. Download both 'main.py' and 'Window.bat' file. 
5. Set up a Windows Task Schedule referring to the 
