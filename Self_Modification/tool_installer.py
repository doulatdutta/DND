import subprocess

class ToolInstaller:
    def install_tool(self, tool_name):
        """
        Installs a specified tool via system commands.
        """
        try:
            print(f"Installing {tool_name}...")
            subprocess.run(["sudo", "apt-get", "install", "-y", tool_name], check=True)
            print(f"Tool {tool_name} installed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to install tool {tool_name}: {e}")

    def install_requirements(self, requirements_file):
        """
        Installs all packages from a requirements.txt file.
        """
        try:
            print(f"Installing packages from {requirements_file}...")
            subprocess.check_call([subprocess.sys.executable, "-m", "pip", "install", "-r", requirements_file])
            print("All packages installed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to install packages from {requirements_file}: {e}")
