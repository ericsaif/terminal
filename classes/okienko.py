from classes import dzwig


class okienko():
    def __init__(self):
        self.wolne=True
        self.dzwigi = [dzwig(3) for _ in range(3)]
    def zwolnic(self):
        self.wolne = True
    def zajac(self):
        self.wolne = False
    def sprawdz(self):
        return self.wolne
    
