from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote
        self.ostoskori = []
        self.tavarat = 0

    def tavaroita_korissa(self):
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 
        return self.tavarat

    def hinta(self):
        yht_hinta = 0

        for i in self.ostoskori:
            yht_hinta += i.hinta()
        
        return yht_hinta
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        self.tavarat += 1
        ostos = Ostos(lisattava)

        for i in self.ostoskori:
            if i.tuotteen_nimi() == ostos.tuotteen_nimi():
                i.muuta_lukumaaraa(1)
                return
        self.ostoskori.append(ostos)


    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        for i in self.ostoskori:
            if i.tuotteen_nimi() == poistettava.nimi():
                i.muuta_lukumaaraa(-1)
                if i.lukumaara() == 0:
                    self.ostoskori.remove(i)

    def tyhjenna(self):
        # tyhjentää ostoskorin
        self.ostoskori.clear()
        self.tavarat = 0

    def ostokset(self):
        return self.ostoskori
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
