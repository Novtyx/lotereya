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

# Блок тестов
# import lotereya_data as ld
#
#
# def test_buy():
#     tickets = []
#     result = ld.buy(tickets, 5)
#     assert result == [1, 2, 3, 4, 6]
#     assert len(result) == 5
#
#
# def test_draw():
#     tickets = [1, 2, 303]
#     wins = {303: 100}
#     assert ld.draw(tickets, wins, 303) is True
#     assert ld.draw(tickets, wins, 1) is False
#     assert ld.draw(tickets, wins, 999) is False
#
#
# def test_add_win():
#     s = set()
#     assert ld.add_win(s, 303) == {303}
#     assert ld.add_win(s, 777) == {303, 777}
#
#
# def test_even_tickets():
#     assert ld.even_tickets([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
#     assert ld.even_tickets([1, 3, 5]) == []
#
#
# def test_plus_one():
#     assert ld.plus_one([1, 2, 3]) == [2, 3, 4]
# test_buy()