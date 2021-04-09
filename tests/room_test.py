import unittest
from src.room import Room
from src.guest import Guest

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room = Room (2, 15, 100)
        self.ann = Guest("Ann", 350)
        self.bob = Guest("Bob", 350)

    def test_room_can_add_guest(self):
        self.room.add_guest(self.ann)
        self.assertEqual(1, len(self.room.room_capacity))

    def test_room_can_remove_guest(self):
        self.room.add_guest(self.ann)
        self.room.add_guest(self.bob)
        self.room.remove_guest(self.ann)
        self.assertEqual(1, len(self.room.room_capacity))

    def test_if_can_clear_room(self):
        self.room.clear_room()
        self.assertEqual(0, len(self.room.room_capacity))
