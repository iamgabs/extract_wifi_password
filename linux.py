from subprocess import getoutput as cmd
from colorama import Fore

def run_linux()-> str:
    data = cmd(['sudo', 'iwlist', 'scan']).decode('utf-8')
    lines = data.split('\n')
    wifis = []
    passwords = []
    for line in lines:
        if 'ESSID' in line:
            wifi = line.split('ESSID:')[1].strip().strip('"')
            wifis.append(wifi)
        if 'Encryption key' in line and 'off' not in line:
            password = '***'
            passwords.append(password)

    return '\n'.join(f'{wifi}:'+Fore.LIGHTGREEN_EX+f'{str(password[0])}'+Fore.RESET for wifi, password in zip(wifis, passwords))
