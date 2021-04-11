import unittest
from src.room import Room
from src.song import Song
from src.guest import Guest


class TestRoom(unittest.TestCase):

    def setUp(self):
        self.song_1 = Song("Nine Inch Nails", "Closer")
        self.song_2 = Song("Johny Cash", "Hurt")
        self.song_3 = Song("Julie London", "Cry Me a River")
        self.room_small = Room(2, 15, 100)
        self.room_large = Room(5, 25, 150)
        self.ann = Guest("Ann", 350, self.song_1)
        self.bob = Guest("Bob", 350, self.song_2)
        self.john = Guest("John", 10, self.song_3)

    def test_room_can_add_guest(self):
        self.room_small.add_guest(self.ann)
        self.assertEqual(1, len(self.room_small.room_capacity))

    def test_room_can_remove_guest(self):
        self.room_small.add_guest(self.ann)
        self.room_small.add_guest(self.bob)
        self.room_small.remove_guest(self.ann)
        self.assertEqual(1, len(self.room_small.room_capacity))

    def test_if_can_clear_room(self):
        self.room_small.clear_room()
        self.assertEqual(0, len(self.room_small.room_capacity))

    def test_can_add_song(self):
        self.room_small.add_song(self.song_1)
        self.assertEqual(1, len(self.room_small.playlist))

    def test_check_spaces_taken(self):
        self.room_large.add_guest(self.ann)
        self.room_large.add_guest(self.bob)
        self.assertEqual(2, self.room_large.get_spaces_taken())

    def test_check_is_free_space(self):
        self.room_large.add_guest(self.ann)
        self.room_large.add_guest(self.bob)
        self.assertEqual(3, self.room_large.get_free_space_count())

    def test_not_add_if_no_free_space(self):
        self.room_small.add_guest(self.ann)
        self.room_small.add_guest(self.bob)
        self.assertEqual("Room is full.", self.room_small.add_guest(self.john))

    def test_guest_can_pay_entree_fee(self):
        self.assertEqual
        (335, self.ann.remove_money_from_wallet(self.room_small.entry_fee))
        self.assertEqual
        ("You don't have enough money", self.john.remove_money_from_wallet
            (self.room_small.entry_fee))

    def test_check_if_playlist_has_fav_song(self):
        self.room_small.add_song(self.song_2)
        self.assertEqual("Whoo!", self.bob.find_favourite_song(self.room_small.playlist))

    def test_check_if_playlist_no_fav_song(self):
        self.room_small.add_song(self.song_1)
        self.assertEqual("Search for fav song failed.", self.bob.find_favourite_song(self.room_small.playlist))

    def test_check_money_added_to_till(self):
        self.assertEqual(175, self.room_large.pay_entry_fee(self.bob))