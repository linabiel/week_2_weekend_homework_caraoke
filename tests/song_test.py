import unittest
from src.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.closer = Song("Closer")
        self.hurt = Song("Hurt")

    def test_song_has_name(self):
        self.assertEqual("Closer", self.closer.name)