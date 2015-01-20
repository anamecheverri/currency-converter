from currency_converter import *


rates = [("USD", "EUR", 0.74), ("EUR", "JPY", 145.949)]


def test_get_exchange_rate():
    assert get_exchange_rate(rates, "USD", "EUR") == 0.74
    assert get_exchange_rate(rates, "EUR", "JPY") == 145.949
    assert get_exchange_rate(rates, "USD", "JPY") == 0
    assert get_exchange_rate(rates, "JPY", "EUR") == 1 / 145.949
    assert get_exchange_rate(rates, "EUR", "USD") == 1 / 0.74


def test_convert():
    assert convert(rates, 1, "USD", "USD") == 1
    assert convert(rates, 1, "USD", "EUR") == 0.74
    assert convert(rates, 1, "POU", "EUR") == 0
    assert convert(rates, 2, "USD", "EUR") == 1.48
    assert convert(rates, 2, "EUR", "JPY") == 291.898
    assert convert(rates, 2, "EUR", "USD") == 2 * 1 / 0.74
    assert convert(rates, 2, "JPY", "EUR") == 2 * 1 / 145.949
