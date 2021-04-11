class Bar:

    def __init__(self, drink_name, price, till):
        self.drink_name = drink_name
        self.price = price
        self.till = till

    def add_money_to_till(self, guest):
        if guest.wallet >= self.price:
            guest.remove_money_from_wallet(self.price)
            self.till += self.price
        return self.till

    def guest_buy_drink(self, guest, drink):
        guest.remove_money_from_wallet(drink.price)
        self.add_money_to_till(guest)
