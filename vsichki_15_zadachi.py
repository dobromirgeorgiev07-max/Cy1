"""15 задачи от предоставения PDF файл, събрани в една програма.
Изберете номер от менюто и въведете необходимите стойности.
"""

import math


def task1():
    price = float(input('Първоначална цена: '))
    discount1 = float(input('Първа отстъпка (%): '))
    discount2 = float(input('Втора отстъпка (%): '))
    final_price = price * (1 - discount1 / 100) * (1 - discount2 / 100)
    print(f'Крайна цена: {final_price:.2f}')


def task2():
    bus_km = float(input('Километри с автобус: '))
    taxi_km = float(input('Километри с такси: '))
    bus_price = float(input('Цена на км с автобус: '))
    taxi_price = float(input('Цена на км с такси: '))
    print(f'Общо разстояние: {bus_km + taxi_km:.2f}')
    print(f'Обща цена: {bus_km * bus_price + taxi_km * taxi_price:.2f}')


def task3():
    hours = float(input('Отработени часове: '))
    hourly_pay = float(input('Заплащане на час: '))
    bonus = float(input('Бонус (%): '))
    deduction = float(input('Удръжка (%): '))
    salary = hours * hourly_pay * (1 + bonus / 100) * (1 - deduction / 100)
    print(f'Крайно възнаграждение: {salary:.2f}')


def task4():
    food = float(input('Стойност на храната: '))
    drinks = float(input('Стойност на напитките: '))
    service = float(input('Такса обслужване (%): '))
    people = int(input('Брой хора: '))
    if people <= 0:
        print('Броят хора трябва да е положителен.')
        return
    total = (food + drinks) * (1 + service / 100)
    print(f'Обща сметка: {total:.2f}')
    print(f'На човек: {total / people:.2f}')


def task5():
    length = float(input('Дължина: '))
    width = float(input('Ширина: '))
    height = float(input('Височина: '))
    volume = length * width * height
    area = 2 * (length * width + length * height + width * height)
    print(f'Обем: {volume:.3f}')
    print(f'Пълна повърхнина: {area:.3f}')


def task6():
    liters1 = float(input('Литри от първия сок: '))
    price1 = float(input('Цена на литър от първия сок: '))
    liters2 = float(input('Литри от втория сок: '))
    price2 = float(input('Цена на литър от втория сок: '))
    total = liters1 + liters2
    if total <= 0:
        print('Общото количество трябва да е положително.')
        return
    average_price = (liters1 * price1 + liters2 * price2) / total
    print(f'Общо количество: {total:.2f}')
    print(f'Средна цена на литър: {average_price:.2f}')


def task7():
    distance = float(input('Разстояние (км): '))
    speed = float(input('Средна скорост (км/ч): '))
    rest = float(input('Почивка (минути): '))
    if speed <= 0:
        print('Скоростта трябва да е положителна.')
        return
    print(f'Общо време (минути): {distance / speed * 60 + rest:.2f}')


def task8():
    length = float(input('Дължина на стаята: '))
    width = float(input('Ширина на стаята: '))
    height = float(input('Височина на стаята: '))
    openings = float(input('Обща площ на прозорци и врати: '))
    coverage = float(input('Покривност (кв. м на литър): '))
    price = float(input('Цена на литър боя: '))
    area = 2 * (length + width) * height - openings
    if coverage <= 0 or area < 0:
        print('Невалидна покривност или площ за боядисване.')
        return
    liters = area / coverage
    print(f'Необходими литри: {liters:.2f}')
    print(f'Цена за боядисване: {liters * price:.2f}')


def task9():
    grade1 = float(input('Първа оценка: '))
    weight1 = float(input('Тежест на първа оценка (%): '))
    grade2 = float(input('Втора оценка: '))
    weight2 = float(input('Тежест на втора оценка (%): '))
    grade3 = float(input('Трета оценка: '))
    weight3 = float(input('Тежест на трета оценка (%): '))
    result = (grade1 * weight1 + grade2 * weight2 + grade3 * weight3) / 100
    print(f'Среднопретеглена оценка: {result:.2f}')


def task10():
    principal = float(input('Начална сума: '))
    rate = float(input('Годишна лихва (%): '))
    years = float(input('Брой години: '))
    interest = principal * rate / 100 * years
    print(f'Проста лихва: {interest:.2f}')
    print(f'Обща сума: {principal + interest:.2f}')


def task11():
    seconds = int(input('Общо секунди: '))
    if seconds < 0:
        print('Секундите трябва да са неотрицателни.')
        return
    print(seconds // 3600)
    print((seconds % 3600) // 60)
    print(seconds % 60)


def task12():
    length = float(input('Дължина на пода (м): '))
    width = float(input('Ширина на пода (м): '))
    tile_area = float(input('Площ на една плочка (кв. м): '))
    reserve = float(input('Резерв (%): '))
    tile_price = float(input('Цена на една плочка: '))
    if tile_area <= 0:
        print('Площта на плочката трябва да е положителна.')
        return
    count = math.ceil(length * width * (1 + reserve / 100) / tile_area)
    print(f'Необходими плочки: {count}')
    print(f'Обща цена: {count * tile_price:.2f}')


def task13():
    watts = float(input('Мощност (W): '))
    hours = float(input('Часове на ден: '))
    days = int(input('Брой дни: '))
    price = float(input('Цена на kWh: '))
    kwh = watts / 1000 * hours * days
    print(f'Потребление (kWh): {kwh:.2f}')
    print(f'Цена: {kwh * price:.2f}')


def task14():
    distance1 = float(input('Разстояние на първия участък (км): '))
    speed1 = float(input('Скорост на първия участък (км/ч): '))
    distance2 = float(input('Разстояние на втория участък (км): '))
    speed2 = float(input('Скорост на втория участък (км/ч): '))
    if speed1 <= 0 or speed2 <= 0:
        print('Скоростите трябва да са положителни.')
        return
    time = distance1 / speed1 + distance2 / speed2
    average = (distance1 + distance2) / time if time > 0 else 0
    print(f'Общо време (часове): {time:.2f}')
    print(f'Средна скорост (км/ч): {average:.2f}')


def task15():
    count = int(input('Брой продадени продукти: '))
    sale_price = float(input('Продажна цена на продукт: '))
    purchase_price = float(input('Доставна цена на продукт: '))
    extra_costs = float(input('Допълнителни разходи: '))
    income = count * sale_price
    costs = count * purchase_price + extra_costs
    print(f'Общ приход: {income:.2f}')
    print(f'Общ разход: {costs:.2f}')
    print(f'Печалба/загуба: {income - costs:.2f}')


TASKS = [
    ('Цена след две отстъпки', task1),
    ('Пътуване с два вида транспорт', task2),
    ('Заплата с бонус и удръжка', task3),
    ('Сметка в ресторант', task4),
    ('Обем и повърхнина на паралелепипед', task5),
    ('Смесване на два сока', task6),
    ('Време за пътуване', task7),
    ('Боядисване на стая', task8),
    ('Среднопретеглена оценка', task9),
    ('Спестявания с проста лихва', task10),
    ('Преобразуване на секунди', task11),
    ('Поръчка на плочки', task12),
    ('Разход на електроенергия', task13),
    ('Средна скорост за два участъка', task14),
    ('Печалба от продажби', task15),
]


def main():
    while True:
        print('\n=== МЕНЮ: 15 ЗАДАЧИ ===')
        for number, (name, _) in enumerate(TASKS, start=1):
            print(f'{number:2}. {name}')
        print(' 0. Изход')
        try:
            choice = int(input('Избери задача (0-15): '))
            if choice == 0:
                print('Край на програмата.')
                break
            if 1 <= choice <= len(TASKS):
                print(f'\n--- Задача {choice}: {TASKS[choice-1][0]} ---')
                TASKS[choice-1][1]()
            else:
                print('Избери число от 0 до 15.')
        except ValueError:
            print('Въведи валидно число.')


if __name__ == '__main__':
    main()
