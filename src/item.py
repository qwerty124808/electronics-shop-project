import csv

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 0.85
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
        self.all.append(self)
    
    def __repr__(self):
            return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.__name}"

    def __add__(self, objeckt_2):
        if self.__class__.__name__ == "Item" or "Phone":
            return self.quantity + objeckt_2.quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, par_name):
        if len(par_name) <= 10:
            self.__name = par_name
        else:
            Exception: "Длина наименования товара превышает 10 символов"

    @classmethod
    def instantiate_from_csv(cls):
        cls.all = []
        with open("src/items.csv") as file:
            reader = csv.DictReader(file)
            for line in reader:
                Item(line["name"], line["price"], line["quantity"])

    @staticmethod
    def string_to_number(string):
        if "." in string:
            item = string.split(".")
            result = item[0]
            result = int(result)
        else:
            result = int(string)
        return result
        
    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        all_price = self.price * self.quantity
        return all_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.pay_rate * self.price
        return self.price
