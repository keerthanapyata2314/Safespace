import subprocess
import sys
import pkg_resources


def install_requirements(requirements_file):
    try:
        with open(requirements_file, 'r') as f:
            required_packages = f.read().splitlines()
    except FileNotFoundError:
        print(f"Requirements file '{requirements_file}' not found.")
        return

    installed_packages = {pkg.key for pkg in pkg_resources.working_set}

    for package in required_packages:
        if package not in installed_packages:
            print(f"Installing package '{package}'...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        else:
            print(f"Package '{package}' is already installed.")
