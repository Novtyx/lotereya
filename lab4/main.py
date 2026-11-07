import lotereya_data as ld

tickets = []
balance = 100

print("""
Вы принимаете участие в лотерее. Купим билетики?
""")
ld.show_help()

while True:
    cmd = input("> ").strip().lower()

    if cmd == "help":
        ld.show_help()

    elif cmd.startswith("buy"):
        parts = cmd.split()
        if len(parts) == 2 and parts[1].isdigit() and 1 <= int(parts[1]) <= 1000:
            qty = int(parts[1])
            cost = qty * ld.ticket_price
            if cost > balance:
                print(f"Недостаточно средств. Нужно {cost}, у вас {balance}")
                continue
            balance -= cost
            ld.buy(tickets, qty)
            print(f"Куплено {qty} билетов. Баланс: {balance}")
        else:
            print("Введите корректное значение количества билетов")

    elif cmd.startswith("draw"):
        parts = cmd.split()
        if len(parts) == 2 and parts[1].isdigit():
            number = int(parts[1])
            if number not in tickets:
                print("У вас нет такого билета")
                continue
            if ld.draw(tickets, ld.wins, number):
                ld.add_win(ld.wins_set, number)
                balance += ld.wins[number]
                print(f"Баланс после выигрыша: {balance}")
        else:
            print("Введите корректный номер билета")

    elif cmd == "tip":
        print(ld.random_tip())

    elif cmd == "report":
        print(f"Баланс: {balance}")
        print(f"Билеты: {tickets}")
        print(f"Выигрышные билеты: {ld.wins_set or 'нет'}")
        print(f"Чётные билеты: {ld.even_tickets(tickets)}")
        print(f"Билеты+1: {ld.plus_one(tickets)}")

    elif cmd == "exit":
        break

    else:
        print("Неизвестная команда")

print("До встречи!")