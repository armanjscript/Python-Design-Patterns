class MusicPlayer:
    _instance = None
    
    def __new__(cls):
        if not cls._instance:
            cls._instance = super(MusicPlayer, cls).__new__(cls)
            cls._instance.init_player()
            
        return cls._instance
    
    def init_player(self):
        self.song = None
        
    def play(self, song_name):
        
        if self.song:
            self.stop()
        self.song = song_name
        print(f"Playing {self.song} ...")
    
    def stop(self):
        if self.song:
            print(f"Stopping {self.song} ...")
            self.song = None
        else:
            print("No song is playing")
            

#Client code
if __name__ == "__main__":
    player1 = MusicPlayer()
    player2 = MusicPlayer()
    
    print(player1 == player2)
    
    player1.play("Song A")
    player2.play("Song B")
    player1.stop()

        