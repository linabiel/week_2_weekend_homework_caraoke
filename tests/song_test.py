import unittest
from src.song import Song


class TestSong(unittest.TestCase):

    def setUp(self):
        self.song_1 = Song("Nine Inch Nails", "Closer")
        self.song_2 = Song("Johny Cash", "Hurt")
        self.song_3 = Song("Julie London", "Cry Me a River")
        self.songs = [self.song_1, self.song_2, self.song_3]

    def test_song_has_title(self):
        self.assertEqual("Closer", self.song_1.title)
