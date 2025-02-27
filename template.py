import os
from pathlib import Path


list_of_files=[
        "Readme.md",
		"requirements.txt", # Dependencies
		"main.py",  # Entry point

        # models contains Data Strucutres & Classes
		"models/task.py",  
        "models/user.py",
        "models/graph.py",
        "models/stack.py",
        "models/queue.py",
		
        # Services contains Business Logic
		"services/task_service.py",
        "services/user_service.py",

        # Utils contains Helper Functions 
		"utils/helpers.py",

        # Sample Data
		"data/task.json",
        "data/user.json",
]

for path in list_of_files:
    filepath=Path(path)

    filedir,filename=os.path.split(path)
    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
