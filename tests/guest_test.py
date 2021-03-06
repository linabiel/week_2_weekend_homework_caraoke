import unittest
from src.guest import Guest


class TestGuest(unittest.TestCase):
    def setUp(self):
        self.ann = Guest("Ann", 350, "Closer")

    def test_guest_has_name(self):
        self.assertEqual("Ann", self.ann.name)

    def test_guest_has_wallet(self):
        self.assertEqual(350, self.ann.wallet)

    def test_guest_has_favourite_song(self):
        self.assertEqual("Closer", self.ann.favourite_song)