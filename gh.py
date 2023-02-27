class Car():

    """Присваивание к классу описания """
    def __init__ (self,color: str,type: str,year: int):
        self.color = color
        self.type = type
        self.year = year

    """Запуск авто"""
    def starcar(self):
        print("Запуск автомобиля " + self.type)

    """Выключение авто"""
    def offcar(self):
        print("Автомобиль заглушён " + self.type)

    """Присваивание типа,цвета,года"""
def __str__(self):
    return f"Цвет = {self.color}, год выпуск = {self.year}, тип = {self.type}"



car1 = Car("", "", "")
car1.offcar()
car2 = Car("", "", "")
car2.starcar()
print(car1,car2)
a = input("input color: ")
b = int(input("imput year: "))
s = input("input type: ")
car = Car(a, b, s)

print(car)

