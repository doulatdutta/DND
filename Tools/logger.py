# File: DND_Project/Tools/logger.py

import os

class Logger:
    def __init__(self):
        self.logs_folder = './Tools/Logs'
        if not os.path.exists(self.logs_folder):
            os.makedirs(self.logs_folder)

    def log_problem_and_solution(self, problem, solution, tool_path):
        # Create a log file for the new tool
        log_filename = os.path.join(self.logs_folder, f"{os.path.basename(tool_path)}.md")
        with open(log_filename, 'w') as log_file:
            log_file.write(f"# Problem\n{problem}\n\n# Solution\n{solution}\n\n")
