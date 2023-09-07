import pytest
from src.keyboard import Keyboard


@pytest.fixture
def test_item1():
    return Keyboard('Something', 10_000.0, 13)


@pytest.fixture
def test_item2():
    return Keyboard('Anything', 30_000.0, 5)


def test_str(test_item1, test_item2):
    """Тест метода __str__"""
    assert test_item1.__str__() == "Something"
    assert test_item2.__str__() == "Anything"


def test_lang(test_item1, test_item2):
    """Тест для проверки языка по умолчанию"""
    assert test_item1.language == 'EN'
    assert test_item2.language == 'EN'
    with pytest.raises(AttributeError):
        test_item1.language = "CH"


def test_change_lang(test_item1):
    """Тест метода смены раскладки клавиатуры"""
    assert test_item1.change_lang().language == 'RU'
    assert test_item1.change_lang().language == 'EN'
    assert test_item1.change_lang().change_lang().language == 'EN'
    assert test_item1.change_lang().change_lang().change_lang().language == 'RU'
