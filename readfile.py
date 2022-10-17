class ReadFile:

    def __init__(self):
        self.a = "Hello"
    
    def read_file(self, filename):
        with open(filename,"r") as f:
            tasks_file_contents = f.read().strip()
            tasks_list = tasks_file_contents.split('\n')
            
            tasks_mother_list = []
            for task in tasks_list:
                task_item_list = task.split(', ')
                tasks_mother_list.append(task_item_list)
            # print(tasks_mother_list)
        return tasks_mother_list