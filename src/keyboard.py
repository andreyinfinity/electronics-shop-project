from src.item import Item


class MixinLanguage:
    """Класс для реализации раскладки клавиатуры и ее переключения"""
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        self.__language = 'EN'

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        """Метод переключения раскладки клавиатуры"""
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'
        return self


class Keyboard(MixinLanguage, Item):
    pass
