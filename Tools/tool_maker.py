# File: DND_Project/Tools/tool_maker.py

import subprocess
import openai

class ToolMaker:
    def __init__(self):
        # Initialize OpenAI API key from environment
        self.api_key = "YOUR_OPENAI_API_KEY"
        openai.api_key = self.api_key

    def create_tool(self, task):
        # Connect with OpenAI to create tool code based on the task
        prompt = f"Create a tool in Python to {task}. Provide necessary code and library requirements."
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=500
        )
        generated_code = response.choices[0].text.strip()
        
        # Parse libraries from response (you can customize this part)
        required_libraries = self.extract_libraries(generated_code)
        return generated_code, required_libraries

    def extract_libraries(self, code):
        # Extract required libraries from the code (simple approach)
        libraries = []
        if "import " in code:
            for line in code.split('\n'):
                if "import" in line:
                    lib = line.split("import")[-1].strip()
                    libraries.append(lib)
        return libraries

    def install_libraries(self, libraries):
        # Install libraries using terminal commands
        for library in libraries:
            try:
                subprocess.run(f"pip install {library}", shell=True, check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error installing {library}: {e}")

