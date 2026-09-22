"""
A class can have multiple methods that work together:

"""
class Playlist:
    def __init__(self,name):
        self.name=name
        self.songs=[]
    
    def add_song(self,title):
        self.songs.append(title)
        print(f"Song {title} added to playlist")
    
    def remove_song(self,title):
        self.songs.remove(title)
        print(f" Song {title} removed from playlist")
    
    def show_list(self):
        for song in self.songs:
            print(f"\n - {song}")

# main program
    
mylist=Playlist("My favourites")
mylist.add_song("Bohemian Rhapsody")
mylist.add_song("Billie Jean")
mylist.add_song("Stayin Alive")
mylist.show_list()
mylist.remove_song("Billie Jean")
mylist.show_list()

