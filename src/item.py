import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price

    def apply_discount(self) -> float:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= Item.pay_rate

    @property
    def name(self) -> str:
        """
        Геттер для названия товара.
        """
        return self.__name

    @name.setter
    def name(self, str_line: str) -> None:
        """Сеттер для названия товара."""
        if len(str_line) > 10:
            raise ValueError("Название должно быть не более 10 символов.")
        self.__name = str_line

    @classmethod
    def instantiate_from_csv(cls, PATH_TO_CSV='../src/items.csv'):
        with open(PATH_TO_CSV, encoding='windows-1251') as file:
            reader = csv.DictReader(file)
            for data in reader:
                cls.all.append((data['name'], float(data['price']), int(data['quantity'])))

    @staticmethod
    def string_to_number(number: str) -> int:
        """Преобразование строки в число."""
        return int(number.split(".")[0])
