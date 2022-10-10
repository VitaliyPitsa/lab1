#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import datetime

if __name__ == '__main__':
    trains = []
    while True:
        command = input(">>> ").lower()
        if command == 'exit':
            break
        elif command == 'add':
            punkt_nazn = input("Пункт назначения ")
            nomer = input("Номер поезда? ")
            time_str = input("время отправления? (hh/mm)\n ")
            time = datetime.datetime.strptime(time_str, '%H/%M').time()
            train = {
                'punkt_nazn': punkt_nazn,
                'nomer': nomer,
                'time': time,
            }
            trains.append(train)
            if len(trains) > 1:
                trains.sort(key=lambda item: item.get('nomer')[::-1])
        elif command == 'list':
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 20
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^20} | {:^20} |'.format(
                    "No",
                    "Пункт назначиния",
                    "Номер поезда",
                    "время отправления"
                )
            )
            print(line)
            for idx, train in enumerate(trains, 1):
                time = train.get('time', '')
                print(
                    '| {:>4} | {:<30} | {:<20} | {}{} |'.format(
                        idx,
                        train.get('punkt_nazn', ''),
                        train.get('nomer', ''),
                        time,
                        ' ' * 5
                    )
                )
            print(line)

        elif command.startswith('select'):
            print("Введите номер поезда: ")
            number = input()
            count = 0
            for train in trains:
                if train.get('nomer') == number:
                    count += 1
                    print('Номер поезда:', train.get('nomer', ''))
                    print('Пункт назначения:', train.get('punkt_nazn', ''))
                    print('Время отправления:', train.get('time', ''))

            if count == 0:
                print("Таких поездов нет!")
        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить поезд;")
            print("list - вывести список поездов;")
            print("select найти информацию о поезде по номеру")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)