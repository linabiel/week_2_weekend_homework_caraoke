class Room:

    def __init__(self, capacity, entry_fee, till):
        self.capacity = capacity
        self.entry_fee = entry_fee
        self.till = till
        self.room_capacity = []
        self.playlist = []

    def add_guest(self, guest):
        self.room_capacity.append(guest)

    def remove_guest(self, guest):
        self.room_capacity.remove(guest)

    def clear_room(self):
        self.room_capacity.clear()

    def add_song(self, song):
        self.playlist.append(song)
        #  return is not needed because 

    def get_spaces_taken(self):
        return len(self.room_capacity)
        # return is needed because I am returning a value, not changing a value
        # without the return the len is not used (redundant)

    def get_free_space_count(self):
        return self.capacity - self.get_spaces_taken()