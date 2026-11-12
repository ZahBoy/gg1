def calculate_cost(minutes,is_electric):
    if is_electric:
        return minutes * 5
    else:
        return minutes * 2

class Network:
    def __init__(self,stations):
        self.stations = stations
    def rent(self,minutes, start_station, end_station, is_electric, client):
        if  not start_station.has_bike(is_electric):
            return "no_bike"
        cost = calculate_cost(minutes,is_electric)
        if not client.can_pay(cost):
            return "no_money"

        bike = start_station.take_bike(is_electric)
        end_station.return_bike(bike)

        client.pay(cost)
        end_station.add_money(cost)
        return cost
    def total_money(self):
        return sum(station.money for station in self.stations)

    def count_bikes(self):
        result = {}

        for station in self.stations:
            result[station.name] = station.count_bikes()
        return result



