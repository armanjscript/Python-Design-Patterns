from typing import List


class FileSystemComponent:
    def show(self, indent=0) -> None:
        pass


class File(FileSystemComponent):
    def __init__(self, name:str):
        self.name = name
        
    def show(self, indent=0) -> None:
        print(" " * indent + f"- {self.name}")
        

class Folder(FileSystemComponent):
    def __init__(self, name:str):
        self.name = name
        self.children : List[FileSystemComponent] = []
    
    def add(self, component: FileSystemComponent):
        self.children.append(component)
        
    def remove(self, component: FileSystemComponent):
        self.children.remove(component)
        
    def show(self, indent=0) -> None:
       print(" " * indent + f"- {self.name}")
       for child in self.children:
           child.show(indent + 1)
           
           
#Client code
if __name__ == "__main__":
    root = Folder("root")
    home = Folder("home")
    
    root.add(home)
    
    user1 = Folder("user1")
    home.add(user1)
    
    file1 = File("file1.txt")
    user1.add(file1)
    
    file2 = File("file2.txt")
    user1.add(file2)
    
    var = Folder("var")
    user1.add(var)
    
    log = File("log.txt")
    var.add(log)
    
    root.show()
    
    