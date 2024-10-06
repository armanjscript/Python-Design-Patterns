#Subsystem1
class CPU:
    def freeze(self):
        print("CPU is frozen")
    
    def jump(self, position):
        print(f"Jumping to position {position}")
        
    def execute(self):
        print("Instructions")
        
#Subsystem2
class Memory:
    def load(self, position, data):
        print(f"Loading data {data} at position {position}")
        

#Subsystem3
class HardDrive:
    def read(self, Iba, size):
        return f"Data from sector {Iba} with size {size}"
    
    
#Fascade
class ComputerFacade:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hard_drive = HardDrive() 
    
    def start(self):
        self.cpu.freeze()
        self.memory.load("0x00", self.hard_drive.read("0x00", "512"))
        self.cpu.jump("0x00")
        self.cpu.execute()
        
        
#Client code
if __name__ == "__main__":
    computer = ComputerFacade()
    computer.start()
        
        
