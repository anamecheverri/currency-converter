from currency_converter import *

rates = [("USD", "EUR", 0.74), ("EUR", "JPY", 145.949)]

def test_convert():
    assert convert(rates,1,"USD","USD")  == 1
