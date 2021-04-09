import unittest
from src.room import Room
from src.guest import Guest

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room = Room (2, 15, 100)
        self.ann = Guest("Ann", 350)

    def test_room_can_add_guest(self):
        self.room.add_guest(self.ann)

    def test_room_can_remove_guest(self):
        self.room.add_guest(self.ann)
        self.room.remove_guest(self.ann)