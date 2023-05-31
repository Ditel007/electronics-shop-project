# смартфон iPhone 14, цена 120_000, количество товара 5, симкарт 2
import pytest

from src.phone import Phone


@pytest.fixture
def phone_fixture1():
    return Phone("iPhone 20", 120_000, 5, 2)


def test_phone(phone_fixture1):
    assert str(phone_fixture1) == 'iPhone 20'
    assert repr(phone_fixture1) == "Phone('iPhone 20', 120000, 5, 2)"
    assert phone_fixture1.number_of_sim == 2
