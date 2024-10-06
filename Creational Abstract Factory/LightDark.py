from abc import ABC, abstractmethod


class Button(ABC):
    @abstractmethod
    def paint(self):
        pass

class Window(ABC):
    @abstractmethod
    def paint(self):
        pass
    
    
class LightButton(Button):
    def paint(self):
        return "Light themed button"
    
class DarkButton(Button):
    def paint(self):
        return "Dark themed button"
    
class LightWindow(Window):
    def paint(self):
        return "Light themed window"

class DarkWindow(Window):
    def paint(self):
        return "Dark themed window"
    
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass
    
    @abstractmethod
    def create_window(self):
        pass
    
class LightThemeFactory(GUIFactory):
    
    def create_button(self):
        return LightButton()
    
    def create_window(self):
        return LightWindow()


class DarkThemeFactory(GUIFactory):
    
    def create_button(self):
        return DarkButton()
    
    def create_window(self):
        return DarkWindow()
    
    
#Client code

def get_theme_factory(theme):
    if theme == "Light":
        return LightThemeFactory()
    elif theme == "Dark":
        return DarkThemeFactory()
    else:
        raise ValueError("The theme is not supported")
    
    
#Test code
if __name__ == "__main__":
    theme = "Dark"
    factory = get_theme_factory(theme)
    button = factory.create_button()
    window = factory.create_window()
    print(button.paint())
    print(window.paint())


    