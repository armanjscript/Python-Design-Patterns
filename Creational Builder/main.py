class Computer:
    def __init__(self):
        self.components = []
    
    def add(self, component):
        self.components.append(component)
        
    def show(self):
        print("Computer Configuration")
        for component in self.components:
            print(f" - {component}")
            

class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()
        
    def build_base(self):
        self.computer.add("Basic Motherboard")
        self.computer.add("Basic CPU")
        
    def build(self):
        return self.computer
    
class GamingComputerBuilder(ComputerBuilder):
    def add_graphics_card(self):
        self.computer.add("High-end Graphics Card")
    
    def add_ram(self):
        self.computer.add("16GB RAM")

class WorkComputerBuilder(ComputerBuilder):
    def add_ram(self):
        self.computer.add("8GB RAM")
    
    def add_storage(self):
        self.computer.add("256GB SSD")
        

class ComputerShop:
    def construct_computer(self, builder):
        builder.build_base()
        return builder.build()
    

if __name__ == "__main__":
    shop = ComputerShop()
    
    gaming_builder = GamingComputerBuilder()
    gaming_builder.add_graphics_card()
    gaming_builder.add_ram()
    
    gaming_computer = shop.construct_computer(gaming_builder)
    gaming_computer.show()
    
    work_builder = WorkComputerBuilder()
    work_builder.add_storage()
    work_builder.add_ram()
    
    working_computer = shop.construct_computer(work_builder)
    working_computer.show()