"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item
from src.errors import InstantiateCSVError


@pytest.fixture
def test_item1():
    return Item('Something', 10_000.0, 13)


@pytest.fixture
def test_item2():
    return Item('Anything', 30_000.0, 5)


def test_add(test_item1, test_item2):
    assert test_item1 + test_item2 == 18
    assert test_item2 + test_item1 == 18
    with pytest.raises(TypeError):
        test_item1 + 12


def test_repr(test_item1, test_item2):
    """Тест метода __repr__"""
    assert test_item1.__repr__() == "Item('Something', 10000, 13)"
    assert test_item2.__repr__() == "Item('Anything', 30000, 5)"


def test_str(test_item1, test_item2):
    """Тест метода __str__"""
    assert test_item1.__str__() == "Something"
    assert test_item2.__str__() == "Anything"


def test_name():
    """
    Тест сеттера класса, проверяющий длину наименования товара (не более 10 символов).
    """
    item = Item('Телефон', 10000, 5)
    assert item.name == 'Телефон'
    item.name = '012345'
    assert item.name == '012345'
    item.name = '0123456789остальное обрезается'
    assert item.name == '0123456789'


def test_instantiate_from_csv():
    """
    Тест на метод класса, создающий объекты из файла *.csv
    """
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    item1 = Item.all[0]
    assert item1.name == 'Смартфон'
    assert item1.price == 100
    assert item1.quantity == 1
    Item.filename = 'bad.csv'
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv()
    Item.filename = 'not_found.csv'
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv()


def test_string_to_number():
    """
    Тест на статический метод класса, преобразующий строку в целое число.
    """
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_calculate_total_price(test_item1, test_item2):
    """
    Тест на метод класса, рассчитывающий общую стоимость товара.
    """
    assert test_item1.calculate_total_price() == 130_000
    assert test_item2.calculate_total_price() == 150_000


def test_apply_discount(test_item1, test_item2):
    """
    Тест на метод класса, рассчитывающий цену со скидкой.
    """
    test_item1.apply_discount()
    test_item1.apply_discount()
    assert test_item1.price == 10_000
    assert test_item2.price == 30_000
    test_item1.pay_rate = 0.5
    test_item1.apply_discount()
    test_item2.apply_discount()
    assert test_item1.price == 5_000
    assert test_item2.price == 30_000
