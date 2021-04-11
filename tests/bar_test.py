import unittest
from src.bar import Bar
from src.guest import Guest
from src.song import Song

class TestBar(unittest.TestCase):
    def setUp(self):
        self.wine = Bar("Wine", 5, 100)
        self.beer = Bar("Beer", 4, 100)
        self.song_1 = Song("Nine Inch Nails", "Closer")
        self.song_2 = Song("Johny Cash", "Hurt")
        self.song_3 = Song("Julie London", "Cry Me a River")
        self.ann = Guest("Ann", 50, self.song_1)
        self.bob = Guest("Bob", 40, self.song_2)
        self.john = Guest("John", 10, self.song_3)

    def test_drink_has_name(self):
        self.assertEqual("Wine", self.wine.drink_name)

    def test_drink_has_price(self):
        self.assertEqual(4, self.beer.price)

    def test_add_money_to_till(self):
        self.beer.add_money_to_till(self.bob)
        self.assertEqual(108, self.beer.add_money_to_till(self.bob))
     
    def test_guest_can_buy_multiple_drinks(self):
        self.ann.remove_money_from_wallet(self.wine.price)
        self.ann.remove_money_from_wallet(self.wine.price)
        self.assertEqual(35, self.ann.remove_money_from_wallet(self.wine.price))