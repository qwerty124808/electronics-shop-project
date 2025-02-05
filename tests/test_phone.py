from src.phone import Phone
import pytest

def tests_phone():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert str(phone1) == 'iPhone 14'
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"
    assert phone1.number_of_sim == 2
    with pytest.raises(ValueError):
        Phone("iPhone", 10000, 15, 0)