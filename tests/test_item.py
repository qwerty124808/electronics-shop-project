"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import *

def tests_calculate_total_price():
    price = 80
    quentity = 1000
    test_1 = Item("cola", price, quentity)
    assert test_1.calculate_total_price() == price * quentity

def tests_apply_discount():
    price = 100
    quentity = 10
    test_2 = Item("frutela", price, quentity)
    assert test_2.apply_discount() == price * 0.85