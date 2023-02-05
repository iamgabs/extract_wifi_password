import platform
import locale
from colorama import Fore, just_fix_windows_console
from header import head
import windows, mac, linux

just_fix_windows_console()
lang, encode = locale.getlocale()
os_name = platform.system().lower()

try:
    print(head)
    if os_name == 'darwin':
        print(mac.run_mac(lang))
    elif os_name == 'linux':
        print(linux.run_linux())
    elif os_name == 'windows':
        if encode == 'cp1252' and lang == 'pt_BR':
            print(windows.run_windows_pt_cp1252())
        elif lang == 'en_US' or lang == 'pt_BR' or lang == 'es_ES':
            print(windows.run_windows(lang))
        else: 
            print(Fore.RED+"Your Operating System language is incompatible, Please use english, portuguese (BR) or spanish")
    else:
        print(Fore.RED+"You are using an incompatible Operating System")
except ModuleNotFoundError:
    if(os_name == 'windows'):
        print(Fore.RED+'Please, before running, you should install all dependencies by using:'+Fore.BLUE+'pyhton -m pip install -r requirements.txt')

