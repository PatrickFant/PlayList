import bisect
from collections import namedtuple
import heapq
from trie import Trie


Playlist = namedtuple('Playlist', ('popularity', 'songs'), verbose = False)


def lineToPlaylist(line):
    tmp = [int(x) for x in line.split(' ')]
    return Playlist(tmp[-1], tmp[:-1])


def loadPlaylistsFromFile():
    playlists = [lineToPlaylist(line) for line in open('playlists.txt', 'r')]
    return heapq.nlargest(1024, playlists)


#def loadSongsFromFile():
#    t = Trie()
#    for line in open('song_list.txt'):
#        tmp = line.split('\t')
#        t.insert(tmp[1])
#    return t


# think about this
def mostPopularPlaylist(song, playlists):
    for playlist in playlists:
        if song in playlist.songs:
            return playlist


def addNewPlaylist(newPlaylist, playlists):
    return heapq.nlargest(1024, playlists + [newPlaylist])
    #bisect.insort(playlists, newPlaylist)
    #if len(playlists) > 1024:
    #    playlists = playlists[:1024]