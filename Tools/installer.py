import subprocess

class Installer:
    def __init__(self):
        pass

    def install_package(self, package_name):
        """
        Installs a Python package using pip.
        """
        try:
            subprocess.check_call([subprocess.sys.executable, "-m", "pip", "install", package_name])
            print(f"Package {package_name} installed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to install package {package_name}: {e}")

    def install_tool(self, tool_name):
        """
        Installs a tool via system commands.
        """
        try:
            subprocess.run(["sudo", "apt-get", "install", "-y", tool_name], check=True)
            print(f"Tool {tool_name} installed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to install tool {tool_name}: {e}")

    def install_requirements(self, requirements_file):
        """
        Installs all packages from a requirements.txt file.
        """
        try:
            subprocess.check_call([subprocess.sys.executable, "-m", "pip", "install", "-r", requirements_file])
            print(f"All packages from {requirements_file} installed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to install packages from {requirements_file}: {e}")
