# Veeambackup
Veeam Agent for Windows Backup w/ Windows Task Scheduler

This is a python project which automates the backup to a NAS location once keyless SSH has been established with the destination. To install this project follow the following steps:

1. Set up NAS and share. Here is a simple guide. One call for windows users, make sure to enable SMB1.0. https://medium.com/@aallan/adding-an-external-disk-to-a-raspberry-pi-and-sharing-it-over-the-network-5b321efce86a

2. Download / Install Veeam Agent for Windows (This is a free service from Veeam). https://www.veeam.com/windows-endpoint-server-backup-free.html

3. Set up a backup job from the Veeam Agent for Windows GUI and backup for the first time. This will be a full backup, and subsequent backups will be incremental when the python script is triggered. 

4. Download both 'main.py' and 'VeeamBackupWindowsTaskScheduler.bat' file. Put them into a folder on your C: drive.

5. In the 'main.py' replace the following areas with your specifics. 

6. Put in the IP of the device you are SSH connecting to in file where "IP_OF_SSH_CONNECTION" is found

7. Line 41: Put the Veeam Backup Job Number here, this is found in the specific Veeam Backup Job.  

8. Inside the "VeeamBackupWindowsTaskScheduler.bat" place two paths enclosed in "". 
   
9. The first path should be the location of your python.exe for example:
        "C:\Users\USERNAME\AppData\Local\Programs\Python\Python37\python.exe" 
   
10. The second path should be to the "main.py" file:
        "C:\Users\USERNAME\LOCATION_OF_FILE\main.py"

11. Open Windows Task Scheduler and create a Task.
   Create a Trigger, i.e. - once a day at 5:00 AM
   On the Actions tab create a "New" action which "Start a Program" and point it to your "VeeamBackupWindowsTaskScheduler.bat" location.
   Create the task.
   
This will now run the "main.py" when the Windows Task Scheduler is triggered and backup your device.

Boom baby! You have free Enterprise-Grade Backups working for you!




