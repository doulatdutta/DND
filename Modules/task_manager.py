import os
import os
import subprocess
import importlib
import sys

import openai

from Modules.tool_maker import ToolMaker
from Modules.memory_manager import MemoryManager
from Stock_Analyzer import Stock_analyzer  # Import your stock analyzer module

class TaskManager:
    def __init__(self, openai_api_key):
        self.memory_manager = MemoryManager()  # Optional memory for storing known solutions
        self.tool_maker = ToolMaker(openai_api_key)

    def execute_task(self, task):
        """
        Executes the task by querying OpenAI, generating the code, and running it.
        """
        if self.memory_manager.is_task_known(task):
            print(f"Task found in memory: {task}")
            self.tool_maker.execute_tool_for_task(task)
        else:
            print(f"Task not recognized: {task}. Creating a new tool...")
            tool_path = self.tool_maker.create_tool_for_task(task)
            print(f"Executing new tool: {tool_path}")
            self.tool_maker.execute_tool_for_task(task)

    def install_package(self, package):
        """Install a package using pip."""
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"Successfully installed {package}.")
        except Exception as e:
            print(f"Failed to install {package}: {e}")

    def can_handle_task(self, task):
        """Check if the task can be handled by checking memory or available tools."""
        known_tasks = self.memory_manager.get_known_tasks()
        return task in known_tasks or self.tool_maker.has_tool_for_task(task)

    def execute_task(self, task):
        """Execute the given task by delegating it to the corresponding tool."""
        if task in self.memory_manager.get_known_tasks():
            print(f"Executing task from memory: {task}")
            result = self.memory_manager.execute_memory_task(task)
        else:
            print(f"Creating a new tool for task: {task}")
            solution = self.tool_maker.create_tool_for_task(task)

            # Attempt to install required packages
            required_packages = self.tool_maker.get_required_packages(task)
            for package in required_packages:
                self.install_package(package)

            # Generate code and save it to a file
            tool_file_path = self.tool_maker.generate_tool_code(task, solution)

            # Execute the generated tool
            success = False
            attempts = 0
            max_attempts = 5  # Set the maximum number of attempts
            while not success and attempts < max_attempts:
                print(f"Attempt {attempts + 1}: Executing the tool...")
                try:
                    # Import and execute the generated tool
                    tool_module = importlib.import_module(tool_file_path.replace('.py', '').replace('/', '.'))
                    tool_module.execute()  # Assuming the generated tool has an execute function
                    success = True
                    print("Task executed successfully!")
                except Exception as e:
                    print(f"Execution failed: {e}")
                    print("Attempting to resolve the issue...")
                    attempts += 1
                    self.tool_maker.solve_issue(task, e)  # Implement a method to resolve issues

            if not success:
                print(f"Task failed after {max_attempts} attempts.")
        return result

    def is_stock_analysis_task(self, task):
        """
        Determine if the task is related to stock analysis.
        """
        stock_related_tasks = [
            "Select Sector",
            "Select Company",
            "Overall for Next Day",
            "IPO Analysis",
            "Historical Analysis",
        ]
        return any(stock_task in task for stock_task in stock_related_tasks)

def execute_non_stock_task(self, task):
        """
        Executes non-stock-related tasks.
        """
        try:
            print(f"Executing non-stock task: {task}")
            self.create_tool_with_openai(task)
        except Exception as e:
            print(f"An error occurred during non-stock task execution: {e}")
            self.handle_error_with_openai(e)

def create_tool_with_openai(self, task):
        """
        Generates tool creation code using OpenAI and executes it.
        """
        # Generate code from OpenAI
        code = self.openai_api.ask(f"Generate a Python function for the task: {task}")
        
        # Validate and execute the code
        self.execute_code(code)

    # (Include the remaining methods from the previous implementation here...)

def handle_error_with_openai(self, error):
        """
        Handles errors by querying OpenAI for a potential fix.
        """
        print(f"An error occurred: {error}")
        prompt = f"Error: {error}. Provide a valid Python code fix for the above error."
        
        try:
            # Use OpenAI to get a fix for the error
            fix_code = self.openai_api.ask(prompt)
            
            # Log the output from OpenAI for debugging
            print("Proposed fix code from OpenAI:", fix_code)
            
            # Attempt to execute the proposed fix code
            self.execute_code(fix_code)
            
        except Exception as e:
            print(f"Failed to execute fix code: {e}")

