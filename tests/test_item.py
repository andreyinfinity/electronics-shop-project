"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def test_item1():
    return Item('Something', 10_000.0, 13)


@pytest.fixture
def test_item2():
    return Item('Anything', 30_000.0, 5)


def test_calculate_total_price(test_item1, test_item2):
    assert test_item1.calculate_total_price() == 130_000
    assert test_item2.calculate_total_price() == 150_000


def test_apply_discount(test_item1, test_item2):
    test_item1.apply_discount()
    test_item1.apply_discount()
    assert test_item1.price == 10_000
    assert test_item2.price == 30_000
    test_item1.pay_rate = 0.5
    test_item1.apply_discount()
    test_item2.apply_discount()
    assert test_item1.price == 5_000
    assert test_item2.price == 30_000
