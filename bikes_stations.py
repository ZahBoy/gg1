class Bike:
    def __init__(self, number, is_electric):
        self.number = number
        self.is_electric = is_electric

    def price_per_minute(self):
        return 5 if self.is_electric else 2


class Station:
    def __init__(self, name):
        self.name = name
        self.bikes = []
        self.money = 0

    def has_bike(self, is_electric):
        for bike in self.bikes:
            if bike.is_electric == is_electric:
                return True
        return False

    def add_money(self, amount):
        self.money += amount

    def count_bikes(self):
        return len(self.bikes)
