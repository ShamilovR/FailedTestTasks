class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    @property
    def get_name_items(self):
        return self.__name_items

    @property
    def get_number_items(self):
        return self.__number_items

    def add_item_to_cheque(self, name):
        if len(name) != 0 or len(name) < 40:
            raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')
        else:
            self.__name_items.append(name)
            self.__number_items += 1

    def delete_item_from_check(self, name):
        if name in self.__name_items:
            self.__name_items.remove(name)
            self.__number_items -= 1
        else:
            raise NameError('Позиция отсутствует в чеке')

    def check_amount(self):
        total = []
        for i in range(len(self.__name_items)):
            if self.__name_items[i] in self.__item_price:
                total.append(self.__item_price.get(self.__name_items[i]))
        if len(self.__name_items) > 10:
            return sum(total) - (sum(total) * 10) / 100
        else:
            return sum(total) * 0.9

    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = []
        for i in range(0, len(self.__name_items)):
            if self.__name_items[i] in self.__tax_rate:
                if self.__tax_rate.get(self.__name_items[i]) == 20:
                    twenty_percent_tax.append(self.__name_items[i])
        total = []
        for i in range(0, len(twenty_percent_tax)):
            if twenty_percent_tax[i] in self.__item_price:
                total.append(self.__item_price.get(twenty_percent_tax[i]))
        if len(twenty_percent_tax) > 10:
            return (sum(total) - (sum(total) * 10) / 100)
        else:
            return sum(total)

    def ten_percent_tax_calculation(self):
        ten_percent_tax = []
        for i in range(0, len(self.__name_items)):
            if self.__name_items[i] in self.__tax_rate:
                if self.__tax_rate.get(self.__name_items[i]) == 20:
                    ten_percent_tax.append(self.__name_items[i])
        total = []
        for i in range(0, len(ten_percent_tax)):
            if ten_percent_tax[i] in self.__item_price:
                total.append(self.__item_price.get(ten_percent_tax[i]))
        if len(ten_percent_tax) > 10:
            return (sum(total) - (sum(total) * 10) / 100)
        else:
            return sum(total)

    def total_tax(self):
        return OnlineSalesRegisterCollector.ten_percent_tax_calculation() + OnlineSalesRegisterCollector.twenty_percent_tax_calculation()

    @staticmethod
    def get_telephone_number(telephone_number):
        if len(str(telephone_number)) > 10:
            raise ValueError('Необходимо ввести 10 цифр после "+7"')
        try:
            float(telephone_number)
        except ValueError:
            raise ValueError('Необходимо ввести цифры') from None
        return f'+7{telephone_number}'
