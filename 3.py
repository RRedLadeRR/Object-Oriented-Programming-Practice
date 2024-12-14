class KgToPounds:

    def __init__(self, kg):
        self.__kg = kg

    @property
    def kg(self):
        return self.__kg

    @kg.setter
    def kg(self, new_kg):
        if isinstance(new_kg, (int, float)):
            self.__kg = new_kg
        else:
            print('Кілограми задаються лише числами')

    def to_pounds(self):
        return self.__kg * 2.205

kg_to_pounds = KgToPounds(10)

print(kg_to_pounds.kg)  # Виведе: 10

kg_to_pounds.kg = 20  # Тепер можна просто присвоїти значення через атрибут
print(kg_to_pounds.kg)  # Виведе: 20

print(kg_to_pounds.to_pounds())  # Виведе: 44.1 (20 * 2.205)

kg_to_pounds.kg = "десять"  # Виведе: Кілограми задаються лише числами
