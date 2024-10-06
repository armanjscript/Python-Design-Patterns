from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass
    
    @abstractmethod
    def undo(self) -> None:
        pass
    

class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light
    
    def execute(self) -> None:
        self.light.turn_on()
        
    def undo(self):
        self.light.turn_off()
        

class LightOffCommand(Command):
    def __init__(self, light) -> None:
        self.light = light
    
    def execute(self) -> None:
        self.light.turn_off()
        
    def undo(self) -> None:
        self.light.turn_on()
        
class Light:
    def turn_on(self):
        print("Light is on")
    
    def turn_off(self):
        print("Light is off")
        

class RemoteControl:
    def __init__(self):
        self.command = None
    
    def set_command(self, command: Command):
        self.command = command

    def press_button(self):
        self.command.execute()
        
    def press_undo(self):
        self.command.undo()
        
        
#Client code
if __name__ == "__main__":
    light = Light()
    
    light_on = LightOnCommand(light)
    light_off = LightOffCommand(light)
    
    remote = RemoteControl()
    remote.set_command(light_on)
    remote.press_button()
    
    remote.set_command(light_off)
    remote.press_button()
    
    remote.press_undo()