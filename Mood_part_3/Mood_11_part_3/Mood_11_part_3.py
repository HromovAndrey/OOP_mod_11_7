#Завдання 1
#Реалізуйте клас «Людина». Збережіть у класі: ПІБ,
#дату народження, контактний телефон, місто, країну,
#домашню адресу. Реалізуйте методи класу для введення-виведення даних та інших операцій.
class Person:
    def __init__(self, full_name, date_of_birth, phone_number, city, country, home_addres):
        self.full_name = full_name
        self.date_of_birth = date_of_birth
        self.phone_number = phone_number
        self.city = city
        self.country = country
        self.home_address = home_addres

    def display_info(self):
        print("ПІБ", self.full_name)
        print("Дата народження:", self.date_of_birth)
        print("Контактні телефони:", self.phone_number)
        print("Місто:", self.city)
        print("Країна:", self.country)
        print("Домашня адреса:", self.home_addres)

person1 = Person("Бобров, Сергій, Юрійович" "01.03.93", "+380667002389", "Миколаїв", "Україна")
person1.display_info()

#Завдання 2
#Створіть клас «Місто». Збережіть у класі: назву міста,
#назву регіону, назву країни, кількість жителів у місті,
#поштовий індекс міста, телефонний код міста. Реалізуйте
#методи класу для введення-виведення даних та інших
#операцій.

class City():
    def __init__(self, name, region, state, population, phone_code):
        self.name = name
        self.region = region
        self.state = state
        self.population = population
        self.phone_code = phone_code
    def info_output(self):
      print(f"City{self.name} located in region of {self.state}. Current population is:{self.population} and {self.phone_code}):
    def info_input(self):
      self.name = input("Input city name:")
      self.region = input("Input region name:")
      self.state = input("Input name of the state:")
      self.population = input("Input number of population:")
      self.phone_code = input("Input phone code")

      print(f"city{self.name} located in region of{self.region} in {self.state} Current population{self.population} and {self.phone_code}")
city = City("Mukolaiv", "North", "Ukreina", "2.5m", "+18067889")
city.info_output()


#Завдання 3
#Створіть клас «Країна». Збережіть у класі: назву країни,
#назву континенту, кількість жителів країни, телефонний
#код країни, назву столиці, назву міст країни. Реалізуйте
#методи класу для введення-виведення даних та інших
#операцій.

class Country:
    def __init__(self, name, continent, population, pnone_code, capital, cities - []):
         self.name = name
         self.continent = continent
         sef.populaion = population
         self.phone_CODE = phone_code
         self.capital = capital
         self.cities = cities
    def __str__(self)
         cities_str _ ",". join(self,cities)
         return(f"country^:{self.name}\nContinent:{self.continent} \nPopulation:{self.population} \nPhone_code:{self.code}\ncapital{self.capital}n\cities:{self.cities}")
    def add_city(self, city_name):
         self.cities.append()
         print(f"Added city{city_name} to the country.")

country = Country("Україна", "Європа", 44000000, "+380", "Київ", ["Київ", "Харків", "Одеса", "Львів"])
country.display_info()
