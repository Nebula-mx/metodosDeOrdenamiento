import os

def createFile(name, content):
    directory = os.path.dirname(name)
    if directory and not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)
        
    with open(name, "w", encoding="utf-8") as file:
        file.write(str(content))