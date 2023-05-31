from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, amount_of_sim: int):
        super().__init__(name, price, quantity)
        self.__amount_of_sim = amount_of_sim

    @property
    def amount_of_sim(self):
        return self.__amount_of_sim

    @amount_of_sim.setter
    def number_of_sim(self, value):
        if value <= 0:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
        self.__amount_of_sim = value

    def __repr__(self):
        data = super().__repr__()
        return data.replace(')', f', {self.number_of_sim})')
