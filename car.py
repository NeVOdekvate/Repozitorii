class Car:
    """Автомобиль с базовыми характеристиками."""

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        
    def print_car_info(self):
        print(f"{self.brand} {self.model}, {self.year}")        


if __name__ == "__main__":
    car1 = Car("Toyota", "Camry", 2020)
    car2 = Car("BMW", "X5", 2022)
    car3 = Car("Lada", "Vesta", 2021)

    car1.print_car_info()
    car2.print_car_info()
    car3.print_car_info()        