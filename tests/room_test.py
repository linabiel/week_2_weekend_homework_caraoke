import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room_small = Room (2, 15, 100)
        self.room_large = Room (5, 25, 150)
        self.ann = Guest("Ann", 350)
        self.bob = Guest("Bob", 350)
        self.john = Guest("John", 10)
        self.closer = Song("Closer")
        self.hurt = Song("Hurt")

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
        self.room_small.add_song(self.hurt)
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
        self.assertEqual(335, self.ann.remove_money_from_wallet(self.room_small.entry_fee))
        self.assertEqual("You don't have enough money", self.john.remove_money_from_wallet(self.room_small.entry_fee))