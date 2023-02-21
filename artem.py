class Car:
    color: str
    type: str
    year: int

    def start (self):
         print('Автомобиль заведен')

    def set_year(self, year: int):
         self.year = year

    def __init__(self, color: str, year: int):
        self.color = color
        self.year = year
        self.type = "Седан "

    def __str__(self):
        return f"Цвет = {self.color}, год выпуск = {self.year}, тип = {self.type}"

a = input("input color: ")
b = int(input("imput year: "))

car = Car(a, b)

print(car)



