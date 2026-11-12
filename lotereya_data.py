import random

ticket_price = 1

wins = {7: 100, 15: 500, 42: 50, 50: 1000}
wins_set = set()

tips = [
    "Совет: тратьте больше денег на билеты - один из них точно выигрышный",
    "Совет: лудомания - пугалка социалистов",
    "Совет: баланс не бесконечен",
]


def show_help():
    print("""
help - помощь по командам
buy {количество} - купить билеты
draw {номер билета} - посмотреть, выигрышный ли билет

tip - выдает случайную подсказку
report - показать баланс и билеты
exit - выход
""")


def random_tip():
    return random.choice(tips)


def buy(tickets, qty):
    start = len(tickets) + 1
    tickets.extend(range(start, start + qty))
    return tickets


def draw(tickets, wins, number):
    if number in tickets and number in wins:
        print(f"Да! Билет {number} выигрышный. Приз: {wins[number]}")
        return True
    print("К сожалению, этот билет невыигрышный")
    return False


def add_win(wins_set, n):
    wins_set.add(n)
    return wins_set


def even_tickets(tickets):
    return [t for t in tickets if t % 2 == 0]


def plus_one(tickets):
    return [t + 1 for t in tickets]