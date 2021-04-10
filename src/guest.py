class Guest:

    def __init__(self, name, wallet, favourite_song):
        self.name = name
        self.wallet = wallet
        self.favourite_song = favourite_song

    def remove_money_from_wallet(self, amount):
        if self.wallet >= amount:
            self.wallet -= amount
            return self.wallet
        return "You don't have enough money"

    def find_favourite_song(self, songs):
        for song in songs:
            if song.title == self.favourite_song.title:
                return "Whoo!"
        return "Search for fav song failed."
