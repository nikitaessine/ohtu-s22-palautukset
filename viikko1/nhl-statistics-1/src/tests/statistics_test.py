import unittest
from statistics import Statistics
from player import Player
from enum import Enum

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_konstruktori_toimii(self):
        self.assertEqual(len(self.statistics._players), 5)
    
    def test_pelaajan_etsintä_toimii(self):
        tulos = self.statistics.search('Kurri')
        self.assertEqual(str(tulos), 'Kurri EDM 37 + 53 = 90')
        
        tulos1 = self.statistics.search('Nikita Kucherov')
        self.assertEqual(tulos1, None)
    
    def test_pelaajien_maara_oikein(self):
        self.assertEqual(len(self.statistics.team('DET')),1)
    
    def test_top_toimii(self):
        tulos = self.statistics.top(4)

        self.assertAlmostEqual(tulos[0].name, "Gretzky")
