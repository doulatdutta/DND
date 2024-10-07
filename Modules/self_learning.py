from Modules.memory_manager import MemoryManager
from Modules.failure_handler import FailureHandler

class SelfLearning:
    def __init__(self):
        self.memory_manager = MemoryManager()
        self.failure_handler = FailureHandler()

    def learn_from_failure(self, task):
        """
        Learn from task failure by reviewing logs and searching for solutions.
        """
        print(f"Learning from failure for task: {task}")
        
        # Search for a solution online
        solution = self.failure_handler.search_solution(task)
        
        if solution:
            # If solution found, create a new tool or code
            print(f"Solution found for {task}: {solution}")
            self.failure_handler.create_new_tool_or_code(task, solution)
            
            # Save task and solution to memory for future reference
            self.memory_manager.save_task_solution(task, solution)
            print(f"Memory updated with the solution for task: {task}")
        else:
            print(f"Unable to find a solution for task: {task}, manual intervention needed.")

    def review_log_and_update(self, task, success=True):
        """
        Review the log of a completed task and update the learning system.
        """
        if success:
            print(f"Task {task} was completed successfully.")
        else:
            print(f"Task {task} failed. Attempting to learn and improve.")
            self.learn_from_failure(task)
