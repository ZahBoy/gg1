from bikes_stations import Bike, Station
from clients import Client
from trips import Network, calculate_cost

ERRORS = {
    "no_bike": "на станції немає велосипеда потрібного типу",
    "no_money": "недостатньо грошей на балансі",
}


def print_report(network):
    print("\n=== Звіт адміністратора ===")
    for name, count in network.count_bikes().items():
        print(f"Станція {name}: {count} вел.")
    print(f"Загальна виручка мережі: {network.total_money()} грн")


def main():
    #stantsii
    station_A = Station("A")
    station_B = Station("B")

    #vilisipidu
    station_A.return_bike(Bike(1, False))
    station_A.return_bike(Bike(2, True))
    station_B.return_bike(Bike(3, False))
    station_B.return_bike(Bike(4, True))
    station_B.return_bike(Bike(5, False))

    network = Network([station_A, station_B])

    #klienty
    olya = Client("Оля", 500)
    petro = Client("Петро", 100)

    rides = [
        (20, station_A, station_B, True, olya),     # 100 грн
        (15, station_A, station_B, False, petro),   # 30 грн, станція A порожня
        (15, station_A, station_B, True, olya),     # відмова: на A немає велосипедів
        (5, station_A, station_B, False, olya),     # відмова: на A немає велосипедів
        (10, station_B, station_A, False, olya),    # 20 грн
        (30, station_B, station_A, True, petro),    # відмова: 150 грн > 70 грн
    ]

    print("=== Поїздки ===")
    for minutes, start, end, is_electric, client in rides:
        kind = "електричний" if is_electric else "звичайний"
        result = network.rent(minutes, start, end, is_electric, client)
        route = f"{client.name}: {start.name} -> {end.name}, {kind}, {minutes} хв"
        if result in ERRORS:
            print(f"{route} — відмова: {ERRORS[result]}")
        else:
            print(f"{route} — списано {result} грн")

    #balansy
    print("\n=== Баланси клієнтів ===")
    for client in (olya, petro):
        print(f"{client.name}: {client.balance} грн")

    #zvit
    print_report(network)

    #perevirky
    assert calculate_cost(20, True) == 100
    assert calculate_cost(15, False) == 30
    assert station_A.count_bikes() + station_B.count_bikes() == 5
    assert network.total_money() == 150
    assert olya.balance == 380 and petro.balance == 70
    print("\nУсі перевірки пройдено.")


if __name__ == "__main__":
    main()
