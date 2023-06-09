import csv


class InstantiateCSVError(Exception):
    pass


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []
    file_name = 'items.csv'

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

        # assert repr(item1) == "Item('Смартфон', 10000, 20)"
        # assert str(item1) == 'Смартфон'

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.__name}"

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
        try:
            with open(PATH_TO_CSV, encoding='windows-1251') as file:
                reader = csv.DictReader(file)
                if len(list(csv.DictReader(file))[0]) != 3:
                    raise InstantiateCSVError(f'Файл {cls.file_name} поврежден')
                for data in reader:
                    cls.all.append((data['name'], float(data['price']), int(data['quantity'])))
        except FileNotFoundError:
            raise FileNotFoundError(f'Отсутствует файл {cls.file_name}')
        except PermissionError:
            print(f'Невозможно создать файл {cls.file_name}')


    @staticmethod
    def string_to_number(number: str) -> int:
        """Преобразование строки в число."""
        return int(number.split(".")[0])

    def __add__(self, other: 'Item') -> int:
        if not isinstance(other, Item):
            raise TypeError('Нельзя складывать разные классы')
        return self.quantity + other.quantity
