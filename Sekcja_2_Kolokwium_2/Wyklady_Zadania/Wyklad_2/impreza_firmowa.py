from random import randint


class Pracownik:
    def __init__(self, imprezowosc, podwladni):
        self.imprezowosc = imprezowosc
        self.podwladni = podwladni
        self.g = 0
        self.f = 0

        self.oblicz_g()
        self.oblicz_f()

    def oblicz_g(self):
        if len(self.podwladni) == 0:
            self.g = 0
        else:
            for podwladny in self.podwladni:
                self.g += podwladny.f

    def oblicz_f(self):
        sum_jak_idzie = self.imprezowosc
        for podwladny in self.podwladni:
            sum_jak_idzie += podwladny.g
        self.f = max(self.g, sum_jak_idzie)


def generuj_pracownika(glebokosc):
    ilosc = randint(3,5)
    for i in range(ilosc):
        generuj_pracownika(glebokosc-1)


# garek = generuj_pracownika(5)
c = Pracownik(5, [Pracownik(3, [Pracownik(1, []), Pracownik(1, [])]),Pracownik(2, [])])
print(c.f)
