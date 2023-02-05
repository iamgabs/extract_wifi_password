import subprocess

def run_mac()-> str:
    data = subprocess.check_output(['system_profiler', 'SPAirPortDataType']).decode('utf-8')
    lines = data.split('\n')
    wifis = []
    passwords = []
    for line in lines:
        if 'SSID' in line:
            wifi = line.split(':')[1].strip()
        wifis.append(wifi)
    if 'Password' in line:
        password = line.split(':')[1].strip()
        passwords.append(password)

    return '\n'.join(f'{wifi}:{password}' for wifi, password in zip(wifis, passwords))
