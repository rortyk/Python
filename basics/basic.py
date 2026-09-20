class Playlist:

    def __init__(self, songs):
        self.songs = songs

    def __len__(self):
        return len(self.songs)

    def __getitem__(self, index):
        return self.songs[index]

    def __contains__(self, song):
        return song.lower() in (s.lower() for s in self.songs)

p = Playlist(['Norwegian Wood', 'Blackbird', 'Yesterday'])

print(len(p))        # 3
print(p[0])          # Norwegian Wood
print(p[2])          # Yesterday
print(p[-1])         # Yesterday

print('Blackbird' in p)

for song in p:
    print(song)

print('Blackbird' in p)      # True
print('Hey Jude' in p)       # False

print('blackbird' in p)      # ← 今は False。これを True にしたい
print('BLACKBIRD' in p)      # ← 同上

print('Norwegian Wood' in p)   # True
print('norwegian wood' in p)   # True
print('NORWEGIAN WOOD' in p)   # True
print('Hey Jude' in p)         # False
