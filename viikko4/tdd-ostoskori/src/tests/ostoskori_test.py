import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(),0)
    
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote('Maito', 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(),1)
    
    def test_ostoskorin_hinta_oikea(self):
        maito = Tuote('Maito', 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.hinta(), 3)
    
    def test_kahden_eri_tuotteen_lisaaminen(self):
        maito = Tuote('Maito',3)
        kahvi = Tuote('Kahvi',8)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(kahvi)
        self.assertEqual(self.kori.tavaroita_korissa(),2)
    
    def test_korin_hinta_sama_ku_tuotteiden(self):
        maito = Tuote('Maito',3)
        kahvi = Tuote('Kahvi',8)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(kahvi)

        yht_hinta = maito.hinta() + kahvi.hinta()

        self.assertEqual(self.kori.hinta(), yht_hinta)
    
    def test_kahden_saman_tuotteen_lisaaminen(self):
        maito = Tuote('Maito',3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.tavaroita_korissa(),2)
    
    def test_kahden_saman_tuoteen_lisaaminen_korin_hinta_sama_ku_tuotteiden(self):
        maito = Tuote('Maito',3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        yht_hinta = maito.hinta() + maito.hinta()

        self.assertEqual(self.kori.hinta(), yht_hinta)