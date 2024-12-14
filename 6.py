class Human:
    default_name = "No name"
    default_age = 0

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self._money = 0
        self._house = None
    
    def info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Money: {self._money}")
        print(f"House: {self._house}")
    
    @staticmethod
    def default_info():
        print(f"Default Name: {Human.default_name}")
        print(f"Default Age: {Human.default_age}")
    
    def _make_deal(self, house, price):
        self._money -= price
        self._house = house
    
    def earn_money(self, amount):
        self._money += amount
        print(f"Earned {amount} money! Current value: {self._money}")
    
    def buy_house(self, house, discount):
        final_price = house.final_price(discount)
        if self._money >= final_price:
            self._make_deal(house, final_price)
            print(f"House bought! Final price: {final_price}")
        else:
            print(f"Not enough money! Final price: {final_price}")

class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price
    
    def final_price(self, discount):
        return self._price * (1 - discount)

class SmallHouse(House):
    def __init__(self):
        super().__init__(40, 10000)

# Виклик довідки для класу Human
Human.default_info()

# Створення об'єкта класу Human
person = Human(name="Sasha", age=27)
person.info()

# Створення об'єкта класу SmallHouse
small_house = SmallHouse()
print(f"Final price: {small_house.final_price(0.2)}")  # Знижка 20%

# Спроба купити будинок
person.buy_house(small_house, 0.2)

# Викликаємо метод earn_money для збільшення грошей
person.earn_money(5000)
person.buy_house(small_house, 0.2)

# Оновлення фінансового стану
person.earn_money(20000)
person.buy_house(small_house, 0.2)

# Виведення оновленої інформації
person.info()
