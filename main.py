import subprocess
import os
import time

power_on_cmd = f'sudo uhubctl -l 1-1 -p 2 -a 1'
power_off_cmd = f'sudo uhubctl -l 1-1 -p 2 -a 0'


def pi_connect():
    '''Connects over Keyless SSH to device. Below example is ssh connecting to a raspberry pi and issues power on
    command to external harddrive connected to raspberry pi. Feel free to remove "Power on / off Command" if your NAS
    is constantly running.
    '''
    subprocess.call(f"ssh pi@IP_OF_SSH_CONNECTION {power_on_cmd}", shell=True)
    print('powered on drive')
    time.sleep(30)
    print("started backup")

    backupprocess()

    print("trying errorcode")

    err = os.system("%ERRORLEVEL%")
    print(f'first {err}')

    # If there is an error, this power cycles the external harddrive.
    while err != 1:
        cycle()
        print("cycle backup started")
        backupprocess()
        print("checking err again")
        err = os.system("%ERRORLEVEL%")
        print(f"new {err}")

    subprocess.call(f"ssh pi@IP_OF_SSH_CONNECTION {power_off_cmd}", shell=True)
    print("completed backup")

def backupprocess():
    print('beginning backup')
    os.chdir("C:\Program Files\Veeam\Endpoint Backup") #change as needed for the location of your Veeam install
    os.system("Veeam.EndPoint.Manager.exe backup REPLACE_WITH_BACKUP_JOB_NUMBER") #put in backup job number.

def cycle():
    print("cycling..")
    subprocess.call(f"ssh pi@IP_OF_SSH_CONNECTION {power_off_cmd}", shell=True)
    time.sleep(60)
    print("cycle off complete, turning on")
    subprocess.call(f"ssh pi@IP_OF_SSH_CONNECTION {power_on_cmd}", shell=True)
    time.sleep(60)
    print("turning on complete")


if __name__ == "__main__":
    pi_connect()


