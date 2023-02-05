from subprocess import getoutput as cmd

def run_windows()-> str:
    data = cmd('netsh wlan show profiles').split('\n')
    wifis = [line.split(':')[1][1:] for line in data if "Todos os Perfis de Usu\xa0rios" in line]
    passwords = []
    for wifi in wifis:
        results = cmd(f'netsh wlan show profile {str(wifi)} key=clear').split('\n')
        password_lines = [line for line in results if "Conte£do da Chave" in line]
        if password_lines:
            password = password_lines[0].split(':')[1][1:-1]
            passwords.append(password)

    return '\n'.join(f'{wifi}:{password}' for wifi, password in zip(wifis, passwords))
