class Tomato:
    states = ["flower", "green_tomato", "red_tomato"]  # Стадії дозрівання

    def __init__(self, index):
        self._index = index
        self._state = self.states[0]  # Початковий стан - цвітіння

    def grow(self):
        # Переходить на наступну стадію дозрівання
        if self._state != self.states[-1]:  # Якщо не на останній стадії
            current_state_index = self.states.index(self._state)
            self._state = self.states[current_state_index + 1]

    def is_ripe(self):
        # Перевіряє, чи дозрів томат
        return self._state == self.states[-1]

    def __str__(self):
        return f"Tomato {self._index} is {self._state}"

class TomatoBush:
    def __init__(self, number_of_tomatoes):
        self.tomatoes = [Tomato(i) for i in range(number_of_tomatoes)]  # Створення списку томатів

    def grow_all(self):
        # Зростаємо усі томати
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        # Перевіряємо, чи всі томати дозріли
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    def give_away_all(self):
        # Після збору врожаю очищуємо список томатів
        self.tomatoes.clear()

class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        # Садівник працює і томати ростуть
        print(f"Gardener {self.name} is working...")
        self._plant.grow_all()
        for tomato in self._plant.tomatoes:
            print(tomato)
        print("Gardener finished")

    def harvest(self):
        # Перевіряємо чи всі томати дозріли, якщо дозріли, збираємо врожай
        print(f"Gardener {self.name} is harvesting...")
        if self._plant.all_are_ripe():
            print("Harvesting is finished")
            self._plant.give_away_all()  # Очищаємо список після збору
        else:
            print("Too early! Your plant is green and not ripe.")

    @staticmethod
    def knowledge_base():
        # Довідка для садівників
        print("Harvest time for tomatoes should ideally occur "
              "when the fruit is a mature green and "
              "then allowed to ripen off the vine. "
              "This prevents splitting or bruising "
              "and allows for a measure of control over the ripening process.")

# Створюємо кущ з 3 томатами
tomato_bush = TomatoBush(3)

# Створюємо садівника
gardener = Gardener("Alex", tomato_bush)

# Викликаємо довідку з садівництва
Gardener.knowledge_base()

# Садівник працює
gardener.work()

# Садівник працює ще раз
gardener.work()

# Садівник намагається зібрати врожай, але томати ще не дозріли
gardener.harvest()

# Садівник працює знову
gardener.work()

# Збираємо врожай, тому що всі томати дозріли
gardener.harvest()
