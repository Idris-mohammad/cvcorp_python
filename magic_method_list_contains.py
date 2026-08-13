class Playlist:
    def __init__(self, l=[]):
        self.l=l
    def __len__(self):
        return len(self.l)
    def __add__(self, other):
        if isinstance(other, Playlist):
            if other.endswith(".mp3"):
                l=self.l+other.l
                return Playlist(l)
        else:
            self.l.append(other)
            return self
    def __contains__(self, other):
        return other in self.l
    def __str__(self):
        return str(self.l)
p1=Playlist()
p2=Playlist()
p1=p1+"Fear.mp3"
p1=p1+"Sunflower.mp3"
p2=p2+"Hello.mp3"
p2=p2+"vikram ost"
print(p1)
print(p2)