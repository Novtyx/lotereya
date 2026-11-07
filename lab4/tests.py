import lotereya_data as ld


def test_buy():
    tickets = []
    result = ld.buy(tickets, 5)
    assert result == [1, 2, 3, 4, 5]
    assert len(result) == 5


def test_draw():
    tickets = [1, 2, 303]
    wins = {303: 100}
    assert ld.draw(tickets, wins, 303) is True
    assert ld.draw(tickets, wins, 1) is False
    assert ld.draw(tickets, wins, 999) is False


def test_add_win():
    s = set()
    assert ld.add_win(s, 303) == {303}
    assert ld.add_win(s, 777) == {303, 777}


def test_even_tickets():
    assert ld.even_tickets([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
    assert ld.even_tickets([1, 3, 5]) == []


def test_plus_one():
    assert ld.plus_one([1, 2, 3]) == [2, 3, 4]
test_buy()