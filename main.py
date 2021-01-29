import subprocess
import os
import time

power_on_cmd = f'sudo uhubctl -l 1-1 -p 2 -a 1'
power_off_cmd = f'sudo uhubctl -l 1-1 -p 2 -a 0'


def pi_connect():
    subprocess.call(f"ssh pi@192.168.0.22 {power_on_cmd}", shell=True)
    print('powered on drive')
    time.sleep(30)
    print("started backup")
    backupprocess()
    print("trying errorcode")
    err = os.system("%ERRORLEVEL%")
    print(f'first {err}')

    while err != 1:
        cycle()
        print("cycle backup started")
        backupprocess()
        print("checking err again")
        err = os.system("%ERRORLEVEL%")
        print(f"new {err}")

    subprocess.call(f"ssh pi@192.168.0.22 {power_off_cmd}", shell=True)
    print("completed backup")

def backupprocess():
    print('beginning backup')
    os.chdir("C:\Program Files\Veeam\Endpoint Backup")
    os.system("Veeam.EndPoint.Manager.exe backup 55f08fb4-e942-47fd-846e-017acc750cf5")

def cycle():
    print("cycling..")
    subprocess.call(f"ssh pi@192.168.0.22 {power_off_cmd}", shell=True)
    time.sleep(60)
    print("cycle off compelete, turning on")
    subprocess.call(f"ssh pi@192.168.0.22 {power_on_cmd}", shell=True)
    time.sleep(60)
    print("turning on complete")


if __name__ == "__main__":
    pi_connect()


