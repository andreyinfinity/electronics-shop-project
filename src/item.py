import csv
import os.path


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

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
        src_file = os.path.join(os.path.dirname(__file__), 'items.csv')
        with open(src_file, newline='', encoding='windows-1251') as file:
            csv_file = csv.DictReader(file)
            cls.all.clear()
            for row in csv_file:
                cls(row.get('name'), cls.string_to_number(row.get('price')), cls.string_to_number(row.get('quantity')))

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
