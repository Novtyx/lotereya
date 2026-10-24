tickets = 0
balance = 100
win_ticket = 7

print("""
Вы принимаете участие в лотерее. Купим билетики?
buy {количество} - купить билеты
draw {номер билета} - проверить билет на выигрыш
report - узнать баланс
""")
while True:
    cmd = input("").lower()

    if cmd[:4] == "buy ":
        try:
            buy_count = int(cmd[4:])
            if not (1 <= buy_count <= 1000):
                raise ValueError
            if buy_count * 2 <= balance:
                tickets += buy_count
                balance -= buy_count * 2
                print(f"Вы купили билеты в количестве {buy_count} шт.")
            else:
                print("Недостаточно денег на балансе для покупки билетов")
        except:
            print("Введите корректное значение количества билетов")

    elif cmd[:5] == "draw ":
        try:
            ticket_number = int(cmd[5:])
            if not (1 <= ticket_number <= 1000):
                raise ValueError
            if ticket_number > tickets:
                print("Вы не владеете этим билетом")
                continue
            if ticket_number == win_ticket:
                balance += 100
                print("Да, этот билет выигрышный!")
            else:
                print("К сожалению, этот билет невыигрышный")
        except:
            print("Введите корректное значение номера билета")

    elif cmd == "report":
        print("Баланс:", balance)

    elif cmd == "exit":
        break

    else:
        print("Неизвестная команда")

print("До встречи!")