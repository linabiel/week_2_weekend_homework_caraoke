class Room:

    def __init__(self, capacity, entry_fee, till):
        self.capacity = capacity
        self.entry_fee = entry_fee
        self.till = till
        self.room_capacity = []

    def add_guest(self, guest):
        return self.room_capacity.append(guest)

    def remove_guest(self, guest):
        return self.room_capacity.remove(guest)

    def clear_room(self):
        return self.room_capacity.clear()

    