import platform
import windows, mac, linux

os_name = platform.system().lower()

if os_name == 'darwin':
    print(mac.run_mac())
elif os_name == 'linux':
    print(linux.run_linux())
elif os_name == 'windows':
    print(windows.run_windows())
else:
    print("You are using an incompatible Operating System")
