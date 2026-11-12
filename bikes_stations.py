class Bike:
    def __init__(self, number, is_electric):
        self.number = number
        self.is_electric = is_electric

    def price_per_minute(self):
        return 5 if self.is_electric else 2
