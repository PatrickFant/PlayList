from playlist import *
import tkinter as tk


class App(tk.Frame):
    def __init__(self, master = None):
        tk.Frame.__init__(self, master)
        self.playlists = loadPlaylistsFromFile()
        self.topEightText = tk.StringVar()
        self.pack()
        self.createWidgets()
        self.update()
    
    def createWidgets(self):
        self.topEightBox = tk.Label(
            self,
            textvariable = self.topEightText,
            justify = 'left'
        )
        self.newPlaylistFrame = tk.Frame(self, height = '10')
        self.newPlaylistLabel = tk.Label(
            self.newPlaylistFrame,
            text = 'Create playlist:  '
        )
        self.newPlaylistButton = tk.Button(
            self.newPlaylistFrame,
            text = 'Submit!',
            command = self.newPlaylistButtonPressed
        )
        self.newPlaylistBox = tk.Entry(
            self.newPlaylistFrame
        )
        
        self.topEightBox.pack(side = 'top')
        self.newPlaylistFrame.pack(side = 'bottom')
        self.newPlaylistLabel.pack(side = 'left')
        self.newPlaylistBox.pack(side = 'left')
        self.newPlaylistButton.pack(side = 'left')
    
    def update(self):
        self.topEightText.set(self.printTopEightPlaylists())
    
    def printTopEightPlaylists(self):
        result = ''.join(['{}.)  {}\n'.format(i, playlist.songs)
                          for i, playlist
                          in enumerate(self.playlists[:8], 1)])
        return result
    
    def newPlaylistButtonPressed(self):
        newPlaylist = lineToPlaylist(self.newPlaylistBox.get())
        self.playlists = addNewPlaylist(newPlaylist, self.playlists)
        print(self.playlists[0])
        self.update()


root = tk.Tk()
app = App(master = root)
app.mainloop()