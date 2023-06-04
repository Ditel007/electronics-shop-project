from src.item import Item


class MixinKeyboardLayout:
    def __init__(self, name: str, price: float, quantity: int):
        self.__language = 'EN'
        super().__init__(name, price, quantity)

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'


class KeyBoard(MixinKeyboardLayout, Item):
    def __repr__(self) -> str:
        return super().__repr__().replace('Item', 'KeyBoard')
