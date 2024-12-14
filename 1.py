class Soda:
    def __init__(self, addition=None):
        self.addition = addition

    def show_my_drink(self):
        if self.addition:
            print(f"Газована вода та {self.addition}")
        else:
            print("Звичайна газована вода")

drink_with_addition = Soda("лимон")
drink_with_addition.show_my_drink()  # Виведе: Газована вода та лимон

drink_without_addition = Soda()
drink_without_addition.show_my_drink()  # Виведе: Звичайна газована вода
