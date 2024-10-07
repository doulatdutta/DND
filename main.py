import os
import openai
import ast
import subprocess

from dotenv import load_dotenv
from Tools.pdf_reader import PDFReader
from Tools.websearch import WebSearch
from Tools.chrome import ChromeTool
from Tools.installer import Installer
from Tools.agent import AgentManager, Agent
from Stock_Analyzer.Stock_analyzer import StockAnalyzer
from Tools.tool_maker import ToolMaker
from Tools.logger import Logger

# Load environment variables from .env file
load_dotenv(os.path.join("config", ".env"))

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")


class OpenAIAPI:
    def __init__(self):
        self.api_key = openai.api_key

    def ask(self, prompt):
        """
        Sends a prompt to OpenAI and returns the response.
        """
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", 
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message['content'].strip()


class Chatbot:
    def __init__(self, openai_api):
        self.openai_api = openai_api
        self.past_inputs = []
        self.past_workflows = []

    def chat_with_user(self):
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'exit':
                print("Chatbot: Goodbye!")
                break
            
            workflow = self.create_workflow(user_input)
            if workflow in self.past_workflows:
                print("Chatbot: I generated this workflow earlier. Let's try a different input.")
                continue

            self.past_inputs.append(user_input)
            self.past_workflows.append(workflow)

            confirmation = input(f"Chatbot: I generated the following workflow:\n{workflow}\nDo you want to proceed? (yes/no): ")
            if confirmation.lower() == 'yes':
                self.execute_workflow(workflow)
            else:
                print("Chatbot: Let's try again.")

    def create_workflow(self, user_input):
        prompt = f"Create a workflow based on this user input: {user_input}"
        return self.openai_api.ask(prompt)

    def execute_workflow(self, workflow):
        for step in workflow.split('\n'):
            print(f"Executing: {step}")

    def create_tool_with_openai(self, task):
        prompt = f"Create a Python function to perform the task: {task}."
        code = self.openai_api.ask(prompt)
        print("Generated code:", code)
        self.execute_code(code)

    def execute_code(self, code):
        try:
            exec(code)
        except Exception as e:
            print(f"Error executing code: {e}")


class DNDChat:
    def __init__(self):
        self.tools_folder = './Tools'
        self.tool_maker = ToolMaker()
        self.logger = Logger()

    def run(self, user_input):
        task = self.analyze_task(user_input)
        tool_path = self.find_tool(task)
        
        if tool_path:
            agent = Agent(tool_path)
            return agent.run(user_input)
        else:
            new_tool_path, problem, solution = self.create_new_tool(task)
            self.logger.log_problem_and_solution(problem, solution, new_tool_path)
            agent = Agent(new_tool_path)
            return agent.run(user_input)

    def analyze_task(self, user_input):
        return user_input

    def find_tool(self, task):
        for root, _, files in os.walk(self.tools_folder):
            for file in files:
                if task.lower() in file.lower():
                    return os.path.join(root, file)
        return None

    def create_new_tool(self, task):
        new_tool_code, required_libraries = self.tool_maker.create_tool(task)
        self.tool_maker.install_libraries(required_libraries)
        new_tool_path = self.save_tool(task, new_tool_code)
        problem = f"Create a tool for {task}"
        solution = f"Tool created using: {', '.join(required_libraries)}"
        return new_tool_path, problem, solution

    def save_tool(self, task, code):
        tool_name = task.replace(" ", "_").lower() + ".py"
        tool_path = os.path.join(self.tools_folder, tool_name)
        with open(tool_path, 'w') as tool_file:
            tool_file.write(code)
        return tool_path


class TaskManager:
    def __init__(self):
        self.stock_analyzer = StockAnalyzer()
        self.pdf_reader = PDFReader(pdf_folder="input/pdfs")
        self.websearch = WebSearch()
        self.chrome_controller = ChromeTool()
        self.installer = Installer()
        self.agent_manager = AgentManager()

    def execute_task(self, task):
        if self.is_stock_related(task):
            self.execute_stock_analysis_task(task)
        else:
            self.execute_non_stock_task(task)

    def is_stock_related(self, task):
        stock_keywords = ["stock", "price", "analysis", "prediction", "TATASTEEL"]
        return any(keyword in task.lower() for keyword in stock_keywords)

    def execute_stock_analysis_task(self, task):
        try:
            print(f"Analyzing stock prices for: {task}")
            company_name = self.extract_company_name(task)
            self.stock_analyzer.analyze_stock(company_name)
        except Exception as e:
            print(f"Error in stock analysis: {e}")
            self.handle_error_with_openai(e)

    def execute_non_stock_task(self, task):
        if self.tool_exists(task):
            self.run_existing_tool(task)
        else:
            self.create_tool_with_openai(task)

    def tool_exists(self, task):
        existing_tools = [
            "download a video",
            "read a pdf",
            "search the web",
            "use chrome"
        ]
        return any(tool in task for tool in existing_tools)

    def run_existing_tool(self, task):
        if "download a video" in task:
            topic = task.split("about")[-1].strip()
            print(f"Downloading video about: {topic}")
            # Assuming you have a download function in your downloader tool
            self.chrome_controller.download_video(topic)
        elif "read a pdf" in task:
            pdf_path = self.extract_pdf_path(task)
            print(f"Reading PDF: {pdf_path}")
            self.pdf_reader.read_and_analyze(pdf_path)
        elif "search the web" in task:
            query = task.split("about")[-1].strip()
            print(f"Searching the web for: {query}")
            self.websearch.search(query)
        elif "use chrome" in task:
            action = self.extract_chrome_action(task)
            print(f"Using Chrome for: {action}")
            self.chrome_controller.perform_action(action)

    def create_tool_with_openai(self, task):
        code = self.openai_api.ask(f"Generate a Python function for the task: {task}")
        self.execute_code(code)

    def execute_code(self, code):
        try:
            ast.parse(code)
            exec(code)
        except Exception as e:
            print(f"Error executing code: {e}")

    def handle_error_with_openai(self, error):
        prompt = f"Error: {error}. Provide a Python code fix for this error."
        try:
            fix_code = self.openai_api.ask(prompt)
            print("OpenAI fix code:", fix_code)
            exec(fix_code)
        except Exception as e:
            print(f"Failed to apply fix: {e}")

    def extract_company_name(self, task):
        return task.split("for")[-1].strip() if "for" in task else "TATASTEEL"

    def extract_pdf_path(self, task):
        return task.split("at")[-1].strip()

    def extract_chrome_action(self, task):
        return task.split("for")[-1].strip()


if __name__ == "__main__":
    openai_api = OpenAIAPI()
    chatbot = Chatbot(openai_api)
    dnd_chat = DNDChat()
    task_manager = TaskManager()

    user_input = input("Enter your command: ")
    task_manager.execute_task(user_input)
