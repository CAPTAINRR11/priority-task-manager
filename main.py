from task_manager import TaskManager
from cli_interface import run_cli  

if __name__ == "__main__":
    task_manager = TaskManager()
    run_cli(task_manager) 
    