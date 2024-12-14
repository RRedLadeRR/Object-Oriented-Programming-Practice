class TriangleChecker:
    def __init__(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Всі сторони повинні бути позитивними числами.")
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            return "Ура, можна побудувати трикутник!"
        else:
            return "На жаль, з цього трикутник не зробити."

triangle = TriangleChecker(1, 1, 3)
print(triangle.is_triangle())  # Виведе: На жаль, з цього трикутник не зробити.

try:
    invalid_triangle = TriangleChecker(-3, 4, 5)
except ValueError as e:
    print(e)  # Виведе: Всі сторони повинні бути позитивними числами.

triangle = TriangleChecker(3, 4, 5)
print(triangle.is_triangle())  # Виведе: Ура, можна побудувати трикутник!
