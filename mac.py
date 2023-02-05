from subprocess import getoutput as cmd
from colorama import Fore

def run_mac(lang: str = 'en_US')-> str:
    data = cmd(['system_profiler', 'SPAirPortDataType']).decode('utf-8')
    lines = data.split('\n')
    wifis = []
    passwords = []
    for line in lines:
        if 'SSID' in line:
            wifi = line.split(':')[1].strip()
        wifis.append(wifi)
    if(lang == 'en_US'):
        if 'Password' in line:
            password = line.split(':')[1].strip()
            passwords.append(password)
    elif(lang == 'pt_BR'):
        if 'Senha' in line:
            password = line.split(':')[1].strip()
            passwords.append(password)
    elif(lang == 'en_ES'):
        if 'Contraseña' in line:
            password = line.split(':')[1].strip()
            passwords.append(password)

    return '\n'.join(f'{wifi}:'+Fore.LIGHTGREEN_EX+f'{str(password[0])}'+Fore.RESET for wifi, password in zip(wifis, passwords))

