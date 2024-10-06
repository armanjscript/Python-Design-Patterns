class DJ:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            print("A new DJ is in the house.")
            cls._instance = super(DJ, cls).__new__(cls)
            cls._instance.song = "No music yet"
        return cls._instance
    
    def change_song(self, song):
        self.song = song
        print(f"Now playing {self.song}")
        


dj1 = DJ()
dj1.change_song("Despacito")

dj2 = DJ()
dj2.change_song("Shape of you")

print(dj1.song)


        
            