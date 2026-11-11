class element_kolejki():
    def __init__(self):
        self.czas_oczekiwania=0
        
    def zwieksz_czas_oczekiwania(self):
        self.czas_oczekiwania+=1

    def zwroc_czas_oczekiwania(self):
        return self.czas_oczekiwania