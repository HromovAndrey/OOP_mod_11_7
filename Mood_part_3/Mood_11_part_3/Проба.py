class Computer:
    def __init__(self, cpu, ram, gpu):
        self.cpu = cpu
        self.ram = ram
        self.gpu = gpu

    @propetry
    def cpu(self):
       "Повнртає інформацію про процесор"
       return self.__cpu
    @propetry
    def ram(self):
       "Поверта інформацію про ОЗУ"
       return self.__ram
    @propetry
    def gpu(self):
        "Поверта єінформацію про відеокарту"

    def display_specs(self):
        "Виводить специфікації компютерів"
        print(f"Процесор: {self.cpu}")

        print(f"ОЗУ:{self.ram} GB")
        print(f"Відеокарта:{self.gpu}")
my_computer = Computer("AMD ryzen 5 7500x", 16, "NVIDIA GeForce RTX 4080")
my_computer.display_speces()


class User:
    "Реалізує клас Користувач з атрибутів імя вік  та емейл"
     def __init__(self, name: str, age: int, email: str):
         "Ініціалізація екземпляру класу Користувач "
         self.__name =name
         self.__age = age
         self.__email = email
     def get_name(self) -> str:
         "Повериає імя користувача"
         self.__name = new_name
     def get_age(self) -> int:
         "Повертає вік користувача"
         return self.__age
     def get_email(self) -> str:
         "Повертає емеіл фдресу користувача00"
         return self.__email
     def __str__(self):
         "Повертає рядок З інформаціею про користувача"
         return f""""""
     **Імя** {self.get_name()}

class Bank:

    count = 0
    exchange_rate_usd_ = 38
    def __init__(self):
        Bank.count += 1
        self.bank = 30

    def uah_to_usd(self, velua_uah):
        return velua_uah / 38
    def set_balance(self, balance):
        self.balance = balance

    @classmethod
    def get_count():
        return
object1 = Bank
print(object1.uah_to_usd(1000))
print(Bank.uah_to_usd(1000))



