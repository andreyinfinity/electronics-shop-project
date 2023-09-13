import csv
import os.path
from src.errors import InstantiateCSVError


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []
    filename = 'items.csv'

    def __init__(self, name: str, price: float | int | str, quantity: int | str) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = self.string_to_number(price)
        self.quantity = self.string_to_number(quantity)
        Item.all.append(self)

    def __repr__(self):
        return f"Item('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.__name}"

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        raise TypeError("Складывать можно только объекты класса Item и его дочерние")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) <= 10:
            self.__name = name
        else:
            self.__name = name[:10]

    @staticmethod
    def string_to_number(number: str | float) -> int:
        return int(float(number))

    @classmethod
    def instantiate_from_csv(cls):
        """
        Метод для получения экземпляров класса из табличного файла csv.
        """
        src_file = os.path.join(os.path.dirname(__file__), cls.filename)
        cls.all.clear()
        try:
            with open(src_file, newline='', encoding='windows-1251') as file:
                csv_file = csv.DictReader(file)
                for row in csv_file:
                    cls.check_table(row)
                    cls(row['name'],
                        cls.string_to_number(row['price']),
                        cls.string_to_number(row['quantity']))
        except FileNotFoundError as er:
            print(f'{er.__class__.__name__}: Отсутствует файл {cls.filename}')
            return f'{er.__class__.__name__}: Отсутствует файл {cls.filename}'
        except InstantiateCSVError as er:
            print(f'{er.__class__.__name__}: {er.message}')
            return f'{er.__class__.__name__}: {er.message}'

    @classmethod
    def check_table(cls, row):
        """
        Метод для проверки названий столбцов.
        Вызывает пользовательское исключение InstantiateCSVError, если один из столбцов отсутствует.
        """
        if not ('name' in row and 'price' in row and 'quantity' in row):
            raise InstantiateCSVError(cls.filename)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.pay_rate * self.price
