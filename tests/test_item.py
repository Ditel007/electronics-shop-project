"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest as pytest

from src.item import Item
from src.phone import Phone


@pytest.fixture
def item():
    return Item("item1", 10.0, 5)


def test__repr__(item):
    assert repr(item) == "Item('item1', 10.0, 5)"


def test__str__(item):
    assert str(item) == 'item1'


def test_calculate_total_price(item):
    assert item.calculate_total_price() == 50.0


def test_apply_discount(item):
    Item.pay_rate = 0.9
    item.apply_discount()
    assert item.price == 9.0


def test_all_items():
    if __name__ == "__main__":
        item1 = Item("item1", 10, 5)
        item2 = Item("item2", 20, 3)
        assert Item.all == [item1, item2]


def test_name_setter(item):
    item.name = "Эппл"
    assert item.name == "Эппл"


def test_long_name_setter(item):
    """Тестирует сеттер  self.__name."""
    with pytest.raises(ValueError):
        item.name = 'Самсунгусоптимапроплюс'


def test_string_to_number(item):
    """Тестирует метод string_to_number."""
    assert item.string_to_number("10000") == 10000
    assert item.string_to_number("2.034") == 2


item1 = Item("Patifon", 10000, 20)
phone1 = Phone("Pixel 3XL", 120_000, 16, 2)


def test__add__classes():
    assert item1 + phone1 == 36
    assert phone1 + phone1 == 32
