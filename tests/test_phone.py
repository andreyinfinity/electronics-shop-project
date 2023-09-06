import pytest
from src.phone import Phone
from src.item import Item


@pytest.fixture
def test_item1():
    return Item('Something', 10_000.0, 13)


@pytest.fixture
def test_item2():
    return Item('Anything', 30_000.0, 5)


@pytest.fixture
def test_item3():
    return Phone('iPhone 14', 50_000.0, 4, 2)


@pytest.fixture
def test_item4():
    return Phone('Phone', 20_000.0, 10, 1)


def test_name(test_item3):
    """Тест методов str и repr"""
    assert str(test_item3) == 'iPhone 14'
    assert repr(test_item3) == "Phone('iPhone 14', 50000, 4, 2)"
    assert test_item3.number_of_sim == 2


def test_add(test_item1, test_item3, test_item4):
    """Тест метода add"""
    assert test_item1 + test_item3 == 17
    assert test_item3 + test_item4 == 14


def test_number_of_sim(test_item4):
    """Тест геттера и сеттера с проверкой на корректность"""
    test_item4.number_of_sim = 3
    assert test_item4.number_of_sim == 3
    with pytest.raises(ValueError):
        test_item4.number_of_sim = 0
    with pytest.raises(ValueError):
        test_item4.number_of_sim = "2"
