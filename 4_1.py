class Pair:
    # Список допустимых номиналов
    VALID_DENOMINATIONS = {1, 2, 5, 10, 50, 100, 500, 1000, 5000}

    def __init__(self):
        """
        Инициализация объекта Pair без параметров.
        Поля first и second будут задаваться позже методом read.
        """
        self.first = 0
        self.second = 0

    def validate(self, first, second):
        """
        Проверка корректности значений.
        :param first: номинал купюры
        :param second: количество купюр
        """
        if first not in self.VALID_DENOMINATIONS:
            raise ValueError("Номинал купюры недопустим.")
        if not isinstance(second, int) or second <= 0:
            raise ValueError("Количество купюр должно быть положительным целым числом.")

    def read(self):
        """
        Ввод значений с клавиатуры с проверкой корректности.
        """
        while True:
            try:
                # Ввод номинала купюры
                first = int(input("Введите номинал купюры (1, 2, 5, 10, 50, 100, 500, 1000, 5000): "))

                # Ввод количества купюр
                second = int(input("Введите количество купюр (положительное целое число): "))

                # Проверка корректности введенных данных
                self.validate(first, second)

                # Присваивание полям объекта введенных значений
                self.first = first
                self.second = second
                break  # Прерываем цикл при успешном вводе данных

            except ValueError as e:
                print(f"Ошибка ввода: {e}")

    def display(self):
        """
        Вывод значений полей на экран.
        """
        print(f"Номинал купюры: {self.first}, Количество купюр: {self.second}")

    def summa(self):
        """
        Вычисление общей денежной суммы.
        :return: сумма денег (номинал умноженный на количество купюр)
        """
        return self.first * self.second


if __name__ == '__main__':
    # Создаем объект класса Pair
    pair = Pair()  # Создаем объект без параметров
    pair.read()  # Ввод данных пользователем
    pair.display()  # Вывод данных
    print(f"Общая сумма: {pair.summa()}")  # Вычисляем и выводим общую сумму
