from subprocess import getoutput as cmd
from colorama import Fore

pt_BR = ['Todos os Perfis de Usuários', 'Conteúdo da Chave']
en_US = ['All User Profile', 'Key Content']
es_ES = ['Todo el perfil de usuario', 'Contenido Clave']

def run_windows_pt_cp1252()-> str:
    """The code bellow is to run with encode cp1252 
    for a pt_BR language
    """
    data = cmd('netsh wlan show profiles').split('\n')
    wifis = [line.split(':')[1][1:] for line in data if "Todos os Perfis de Usu\xa0rios" in line]
    passwords = []
    for wifi in wifis:
        results = cmd(f'netsh wlan show profile {str(wifi)} key=clear').split('\n')
        passwords.append([line.split(':')[1][:-1]for line in results if "Conte£do da Chave" in line])
        
    return '\n'.join(f'{wifi}:'+Fore.LIGHTGREEN_EX+f'{str(password[0])}'+Fore.RESET for wifi, password in zip(wifis, passwords) if password != [])


def run_windows(lang: str = 'en_US')-> str:
    data = cmd('netsh wlan show profiles').split('\n')
    if(lang == 'en_US'):
        wifis = [line.split(':')[1][1:] for line in data if f'{en_US[0]}' in line]
    elif(lang == 'pt_BR'):
        wifis = [line.split(':')[1][1:] for line in data if f'{pt_BR[0]}' in line]
    elif(lang == 'en_ES'):
        wifis = [line.split(':')[1][1:] for line in data if f'{es_ES[0]}' in line]
    passwords = []
    for wifi in wifis:
        results = cmd(f'netsh wlan show profile {str(wifi)} key=clear').split('\n')
        if(lang == 'en_US'):
            passwords.append([line.split(':')[1][:-1]for line in results if f'{en_US[1]}' in line])
        elif(lang == 'pt_BR'):
            passwords.append([line.split(':')[1][:-1]for line in results if f'{pt_BR[1]}' in line])
        elif(lang == 'en_ES'):
            passwords.append([line.split(':')[1][:-1]for line in results if f'{es_ES[1]}' in line])
        
    return '\n'.join(f'{wifi}:'+Fore.LIGHTGREEN_EX+f'{str(password[0])}' for wifi, password in zip(wifis, passwords) if password != [])


