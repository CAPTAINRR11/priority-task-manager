import heapq  

class Task:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority  

    def __lt__(self, other):  
        return self.priority < other.priority

class TaskManager:
    def __init__(self):
        self.tasks = []  

    def add_task(self, description, priority):
        task = Task(description, priority)
        heapq.heappush(self.tasks, task)

    def get_next_task(self):
        if self.tasks:
            return heapq.heappop(self.tasks)
        return None

    def list_tasks(self):
        return sorted([(task.description, task.priority) for task in self.tasks], key=lambda x: x[1]) 

#Example Usage
tm = TaskManager()
tm.add_task("Grocery Shopping", 1)
tm.add_task("Pay Bills", 2)
tm.add_task("Doctor Appointment", 1)

next_task = tm.get_next_task()
if next_task:
    print(f"Next task: {next_task.description} (Priority: {next_task.priority})")

tasks = tm.list_tasks()
print("Remaining tasks:")
for description, priority in tasks:
  print(f"- {description} (Priority: {priority})")