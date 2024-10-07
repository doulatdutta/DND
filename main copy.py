import os
import openai
import ast
import subprocess

from dotenv import load_dotenv
from Tools.pdf_reader import PDFReader  # Import your PDF reader tool
from Tools.websearch import WebSearch    # Import your web search tool
from Tools.chrome import ChromeTool  # Import your Chrome controller tool
from Tools.installer import Installer      # Import your installer tool
from Tools.agent import AgentManager       # Import your agent manager tool
from Tools.agent import Agent
from Stock_Analyzer.Stock_analyzer import StockAnalyzer  # Import your stock analyzer tool
from Tools.tool_maker import ToolMaker
from Tools.logger import Logger

# Load environment variables from .env file
load_dotenv(os.path.join("config", ".env"))

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")


class OpenAIAPI:
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")  # Replace with your OpenAI API key

    def ask(self, prompt):
        """
        Sends a prompt to OpenAI and returns the response.
        """
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use the appropriate model
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message['content'].strip()

class Chatbot:
    def __init__(self, openai_api):
        self.openai_api = openai_api
        self.past_inputs = []     # Initialize list to store past inputs
        self.past_workflows = []  # Initialize list to store past workflows

    def chat_with_user(self):
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'exit':
                print("Chatbot: Goodbye!")
                break
            
            workflow = self.create_workflow(user_input)
            if workflow in self.past_workflows:  # Check if the workflow was generated before
                print("Chatbot: I generated this workflow earlier. Let's try a different input.")
                continue  # Skip the confirmation and start over

            self.past_inputs.append(user_input)
            self.past_workflows.append(workflow)

            # Ask for confirmation
            confirmation = input(f"Chatbot: I generated the following workflow based on your input:\n{workflow}\nDo you want to proceed with this workflow? (yes/no): ")
            if confirmation.lower() == 'yes':
                self.execute_workflow(workflow)
            else:
                print("Chatbot: Let's try again.")

    def create_workflow(self, user_input):
        prompt = f"Create a workflow based on this user input: {user_input}"
        workflow = self.openai_api.ask(prompt)
        return workflow

    def execute_workflow(self, workflow):
        for step in workflow:
            print(f"Executing: {step}")

        def create_tool_with_openai(self, task):
            prompt = f"Create a Python function to download an image from a URL. Task: {task}."
            code = self.openai_api.ask(prompt)
        
            print("Generated code:", code)  # Debugging line
            self.execute_code(code)

    def execute_code(self, code):
        try:
            print("Executing the following code:\n", code)  # Debug print statement
            exec(code)
        except Exception as e:
            print(f"Error executing code: {e}")

class DNDChat:
    def __init__(self):
        self.tools_folder = './Tools'
        self.tool_maker = ToolMaker()
        self.logger = Logger()

    def run(self, user_input):
        # Analyze the task from user input
        task = self.analyze_task(user_input)
        
        # Check if tool exists for the task
        tool_path = self.find_tool(task)
        if tool_path:
            # Tool exists, create an agent and assign the task
            agent = Agent(tool_path)
            result = agent.run(user_input)
            return result
        else:
            # Tool doesn't exist, create a new tool
            new_tool_path, problem, solution = self.create_new_tool(task)
            
            # Log the problem and solution in .md file
            self.logger.log_problem_and_solution(problem, solution, new_tool_path)
            
            # Create agent with the new tool and assign the task
            agent = Agent(new_tool_path)
            result = agent.run(user_input)
            return result

    def analyze_task(self, user_input):
        # Simplified task analysis (e.g., "download YouTube video")
        # You can enhance this to make more detailed analysis
        return user_input

    def find_tool(self, task):
        # Search for a tool in the Tools folder
        for root, dirs, files in os.walk(self.tools_folder):
            for file in files:
                if task.lower() in file.lower():
                    return os.path.join(root, file)
        return None

    def create_new_tool(self, task):
        # Ask OpenAI to create the tool
        new_tool_code, required_libraries = self.tool_maker.create_tool(task)
        
        # Install required libraries
        self.tool_maker.install_libraries(required_libraries)
        
        # Save the new tool in the Tools folder
        new_tool_path = self.save_tool(task, new_tool_code)
        
        # Return the problem and solution description
        problem = f"Create a tool for {task}"
        solution = f"Tool created with the following libraries: {', '.join(required_libraries)}"
        return new_tool_path, problem, solution

    def save_tool(self, task, code):
        # Define the file path for the new tool
        tool_name = task.replace(" ", "_").lower() + ".py"
        tool_path = os.path.join(self.tools_folder, tool_name)
        
        # Write the generated code to the tool file
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
            print(f"Analyzing stock prices for task: {task}")
            company_name = self.extract_company_name(task)
            self.stock_analyzer.analyze_stock(company_name)
        except Exception as e:
            print(f"Error in stock analysis: {e}")
            self.handle_error_with_openai(e)
  
    def create_tool_with_openai(self, task):
        """
        Generates tool creation code using OpenAI and executes it.
        """
        # Generate code from OpenAI (you need to implement this)
        code = self.openai_api.ask(f"Generate a Python function for the task: {task}")
        
        # Validate and execute the code
        self.execute_code(code)
  
    def execute_code(self, code):
        """
        Executes the provided code if it's valid Python code.
        """
        try:
            # Check if the code is a valid statement
            ast.parse(code)
            exec(code)
        except SyntaxError as e:
            print(f"Invalid code encountered: {e}. Code: {code}")
        except Exception as e:
            print(f"An error occurred while executing code: {e}")


    def handle_error_with_openai(self, error):
        """
        Handles errors by querying OpenAI for a potential fix.
        """
        print(f"An error occurred: {error}")
        prompt = f"Error: {error}. Provide a valid Python code fix for the above error."
        
        try:
            # Use OpenAI to get a fix for the error
            fix_code = self.openai_api.ask(prompt)  # Adjust this line to call your OpenAI API
            
            # Log the output from OpenAI for debugging
            print("Proposed fix code from OpenAI:", fix_code)
            
            # Execute the proposed fix code
            exec(fix_code)
            
        except Exception as e:
            print(f"Failed to execute fix code: {e}")


    def extract_company_name(self, task):
        return task.split("for")[-1].strip() if "for" in task else "TATASTEEL"

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
            topic = task.split("about")[-1].strip() if "about" in task else ""
            print(f"Downloading video about: {topic}")
            # Assuming you have a download function in your downloader tool
            self.youtube_downloader.download_video(topic)
        elif "read a pdf" in task:
            pdf_path = self.extract_pdf_path(task)
            print(f"Reading PDF at: {pdf_path}")
            self.pdf_reader.read_and_analyze(pdf_path)
        elif "search the web" in task:
            query = task.split("about")[-1].strip() if "about" in task else ""
            print(f"Searching the web for: {query}")
            self.websearch.search(query)
        elif "use chrome" in task:
            action = self.extract_chrome_action(task)
            print(f"Executing Chrome action: {action}")
            self.chrome_controller.perform_action(action)

    def extract_pdf_path(self, task):
        # Extract PDF path logic
        return task.split("at")[-1].strip() if "at" in task else ""

    def extract_chrome_action(self, task):
        # Basic logic to extract action for Chrome
        return task.split("to")[-1].strip() if "to" in task else ""

    def create_tool_with_openai(self, task):
        print(f"No existing tool found for task: {task}. Creating a new tool with OpenAI.")
        prompt = f"Create a Python function to perform the following task: {task}"
        code = self.get_code_from_openai(prompt)
        self.execute_code(code)

    def get_code_from_openai(self, prompt):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content']

    def execute_code(self, code):
        print("Executing generated code...")
        # Caution: Be careful with executing arbitrary code
        exec(code)

    def handle_error_with_openai(self, error):
        print(f"Handling error: {error}")
        prompt = f"Fix this error in the stock analysis code: {error}"
        fix_code = self.get_code_from_openai(prompt)
        print("Executing fixed code...")
        exec(fix_code)




def main():
    
    openai_api = OpenAIAPI()  # Initialize OpenAI API
    chatbot = Chatbot(openai_api)  # Create an instance of the chatbot
    chatbot.chat_with_user()  # Start chatting with the user
    
    task_manager = TaskManager()
    while True:
        task = input("Please enter a task (or type 'exit' to quit): ")
        if task.lower() == 'exit':
            break
        task_manager.execute_task(task)

if __name__ == "__main__":
    main()
