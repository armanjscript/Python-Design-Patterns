class LegacyCode:
    def old_execute(self):
        print("Old Execution Method")
        

class NewSystem():
    def execute(self):
        print("New Execution method.")
        
        
#Adapter
class Adapter:
    def __init__(self, legacy_code):
        self.legacy_code = legacy_code
    def execute(self):
        self.legacy_code.old_execute()

#Client code
def client_code(operation):
    operation.execute()
    
#Create instances
new_system = NewSystem()
legacy_code = LegacyCode()

adapter = Adapter(legacy_code)


client_code(new_system)
client_code(adapter)


    