import lotereya_data as ld

tickets = 0
balance = 100

print("""
Вы принимаете участие в лотерее. Купим билетики?
""")
ld.show_help()
while True:
    cmd = input("").lower()

    if cmd.startswith("buy"):
        buy_count = cmd.split()
        if (len(buy_count) == 2 and buy_count[1].isdigit() and 1 <= int(buy_count[1]) <= 1000):
            balance, tickets = ld.buy(balance, tickets, int(buy_count[1]))
        else: print("Введите корректное значение количества билетов")

    elif cmd.startswith("draw"):
        ticket_number = cmd.split()
        if (int(ticket_number[1]) > tickets):
            print("У вас нет такого билета")
            continue
        if (len(ticket_number) == 2 and ticket_number[1].isdigit() and 1 <= int(ticket_number[1]) <= 1000):
            ld.draw(int(ticket_number[1]))
        else: print("Введите корректное значение количества билетов")

    elif cmd == "help":
        ld.show_help()

    elif cmd == "tip":
        ld.random_tip()

    elif cmd == "report":
        print("Баланс:", balance)

    elif cmd == "exit":
        break

    else:
        print("Неизвестная команда")

print("До встречи!")