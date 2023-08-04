class Player:
    def __init__(self, name, old, score):
        self.name = name
        self.old = int(old)
        self.score = int(score)

    def __bool__(self):
        return self.score > 0


lst = "Балакирев; 34; 2048\nMediel; 27; 0\nВлад; 18; 9012\nNina P; 33; 0"

lst_in = list(map(str.strip, lst.split("\n")))
lst_in = [p.split("; ") for p in lst_in]
players = [Player(*p) for p in lst_in]
players_filtered = list(filter(lambda p: bool(p), players))
print(players_filtered)
