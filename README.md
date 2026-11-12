# Система прокату велосипедів

## Іменники й дієслова

`( )` атрибути, `[ ]` методи

### Іменники

- **Мережа** — клас
  - (станції)
  - [загальна сума грошей]
  - [взяти на прокат (хвилини, початкова станція, кінцева станція, тип велосипеда, клієнт)]
  - [кількість велосипедів]
- **Станція** — клас
  - (список велосипедів)
  - (сума грошей на станції)
- **Велосипед** — клас
  - (тип: електричний / звичайний)
  - (номер)
- **Клієнт** — клас
  - (ім'я)
  - (баланс на рахунку)
- ~~Місто~~
- ~~Повернення~~
- ~~Адміністратор~~

### Дієслова

- ~~є~~
- ~~стояти~~
- ~~мати~~
- **взяти на прокат** — Мережа, [взяти на прокат]
- **покататися** — Мережа, параметр «хвилини»
- **повернути** — Мережа / Станція, кінцева станція
- **коштує** — Велосипед, [ціна за хвилину]
- **списується** — Клієнт, [списати гроші]
- **бачити** — Мережа, [кількість велосипедів] + звіт
- **заробила** — Мережа, [загальна сума грошей]

---

## Картки класів

### Bike

- `number`
- `is_electric`



- `price_per_minute()` → 5 або 2

### Station

- `name`
- `bikes`
- `money`



- `has_bike(is_electric)` → `bool`
- `take_bike(is_electric)` → `Bike` або `None`
- `return_bike(bike)`
- `add_money(amount)`
- `count_bikes()` → `int`

### Client

- `name`
- `balance`



- `can_pay(amount)` → `bool`
- `pay(amount)` → `bool`

### Network

- `stations`



- `rent(minutes, start_station, end_station, is_electric, client)` → вартість або `"no_bike"` / `"no_money"`
- `total_money()` → `int`
- `count_bikes()` → `{станція: кількість}`

### Функції

- `calculate_cost(minutes, is_electric)` → `int`
- `print_report(network)`
- `main()`

---

## Сценарій

1. `network.rent(20, station_a, station_b, True, olya)`
2. `station_a.has_bike(True)` → інакше `"no_bike"`
3. `calculate_cost(20, True)` → 100
4. `olya.can_pay(100)` → інакше `"no_money"`
5. `bike = station_a.take_bike(True)`
6. `station_b.return_bike(bike)`
7. `olya.pay(100)`
8. `station_b.add_money(100)`
9. `main()` друкує результат
