import pytest
from src.keyboard import KeyBoard
from src.item import Item


@pytest.fixture
def item_1() -> KeyBoard:
    """
    Создание объекта Item
    """
    return KeyBoard('Keychron Q5', 15499, 5)


def test_add_method(item_1):
    """
    тест __add__
    """
    assert item_1 + Item("Смартфон", 10000, 20) == 25


def test_repr(item_1):
    """
    тест __repr__
    """
    assert repr(item_1) == "KeyBoard('Keychron Q5', 15499, 5)"


def test_default_language(item_1):
    """
    Проверка языка
    """
    assert item_1.language == "EN"


def test_change_lang(item_1):
    """
    Тест смена языка
    """
    item_1.change_lang()
    assert item_1.language == "RU"


def test_error_change_language(item_1):
    """
    Тест на ошибку присваивания языка
    """
    with pytest.raises(AttributeError):
        item_1.language = 'CH'
