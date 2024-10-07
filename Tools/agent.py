import subprocess
import threading


class Agent:
    def __init__(self, name, task):
        self.name = name
        self.task = task

    def run(self, user_input):
        # Run the tool as a subprocess and capture the output
        try:
            result = subprocess.run(
                ["python", self.tool_path, user_input],
                capture_output=True, text=True
            )
            return result.stdout
        except Exception as e:
            return f"Error running tool: {str(e)}"

class AgentManager:
    def __init__(self):
        self.agents = []

    def create_agent(self, name, task):
        """
        Creates a new agent and assigns it a task.
        """
        agent = Agent(name, task)
        self.agents.append(agent)
        print(f"Agent {name} created.")

    def assign_task(self, name, task):
        """
        Assigns a task to an agent by name.
        """
        for agent in self.agents:
            if agent.name == name:
                agent.task = task
                print(f"Task reassigned to agent {name}.")
                return
        print(f"No agent found with name {name}.")

    def start_all_agents(self):
        """
        Starts all agents in parallel using threading.
        """
        print("Starting all agents...")
        threads = []
        for agent in self.agents:
            t = threading.Thread(target=agent.run)
            threads.append(t)
            t.start()

        for thread in threads:
            thread.join()
        print("All agents have completed their tasks.")
