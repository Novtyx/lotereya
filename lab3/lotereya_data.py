import random

ticket_price = 1
tips = ["Совет: тратьте больше денег на билеты - один из них точно выигрышый",
        "Совет: лудомания - пугалка социалистов",
        "Совет: баланс не бесконечен"]

def show_help():
    print("""help - помощь по командам
buy {количество} - купить билеты
draw {номер билета} - посмотреть, выигрышный ли билет
tip - выдает случайную подсказку
    """)

def random_tip():
    print(random.choice(tips))

def buy(balance, tickets, qty):
    global ticket_price

    if qty * ticket_price <= balance:
        tickets += qty
        balance -= qty * ticket_price
        print(f"Вы купили билеты в количестве {qty} шт.")
    else:
        print("Недостаточно денег на балансе для покупки билетов")
    return balance, tickets

def draw(ticket, win_ticket = 7):
    if ticket == win_ticket:
        print("Да, этот билет выигрышный!")
    else:
        print("К сожалению, этот билет невыигрышный")

