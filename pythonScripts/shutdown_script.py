import os
import platform

def shutdown_computer():
    system_platform = platform.system().lower()

    if system_platform == "windows":
        os.system("shutdown /s /t 1")
    elif system_platform == "linux" or system_platform == "darwin":
        os.system("sudo shutdown now")
    else:
        print("Unsupported operating system for shutdown.")

if __name__ == "__main__":
    shutdown_computer()
