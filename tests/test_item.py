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

def tests_name():
    price = 100
    quentity = 10
    test_3 = Item("barny", price, quentity)
    assert test_3.name == "barny"
    test_3.name = "jack"
    assert test_3.name == "jack"

def tests_instantiate_from_csv():
    test_4 = Item("barny", 100, 10)
    test_4.instantiate_from_csv()
    assert len(test_4.all) == 5

def tests_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5

def tests_repr():
    test_5 = item1 = Item("Смартфон", 10000, 20)
    assert repr(test_5) == "Item('Смартфон', 10000, 20)"

def tests_str():
    test_6 = item1 = Item("Смартфон", 10000, 20)
    assert str(test_6) == 'Смартфон'





