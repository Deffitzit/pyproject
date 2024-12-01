# Задание №1




# myname = input("Введите своё имя:")
# print("Здравствуйте,", myname)




# Задание №2




# a = int(input("Введите первое число:"))
# b = int(input("Введите второе число:"))

# print("Сложение: ", a + b)
# print("Вычитание: ", a - b)
# print("Умножение: ", a * b)
# print("Возведение в степень: ", a ** b)

# if b == 0:
#     print ("деление на 0 запрещено")
# else:
#     print("Деление: ", a / b)
#     print("Деление без остатка: ", a // b)
#     print("Остаток от деления: ", a % b)




# Задание №3




# import random
# from random import randint

# a = []

# for i in range(30):
#     a.append(randint(1,30))

# print(a)
# print(sorted(a))
# a = sorted(a)
# print("минимальное значение", a[0])
# print("максимальное значение", a[-1])




# Задание №4




# import random
# from random import randint
# from tkinter import filedialog

# def create(count):
#     i = 0
#     while i < count:
#         filename = "name" + str(i)
#         a = []
#         file = open(filename, "w+")
#         for c in range(10):
#             a_num = randint(1, 100)
#             a.append(a_num)
#         for k in range(len(a)):
#             file.write(str(a[k]) + " ")
#         file.close()
#         i += 1
# create(10)

# file = filedialog.askopenfilename()
# if file != "":
#     file_r = open(file, "r")
#     data = file_r.read()
#     print("\n", ">>>>>", data)
#     data_l = data.split(" ")
#     data_s = 0
#     for y in range(len(data_l)-1):
#         data_s = data_s + int(data_l[y])
#     data_arifmet = data_s / (len(data_l)-1)
#     print ("\n", "среднее арифметическое - ", data_arifmet, "\n")
#     file_r.close()


# Задание №5



# class Ork:
#     def __init__(self, level: int) -> None:
#         self.level = level
#         self.health_points = 100 * level
#         self.attack_power = 100 * level

#     def attack(self): 
#         print(f"Атакует с силой: {self.attack_power}")

#     def __str__(self) -> str:
#         return f"Ork (уровень: {self.level}, HP: {self.health_points})"

# ork = Ork(level = 2)
# ork.attack()
# print(ork)

# class Elf:
#     def __init__(self, level: int) -> None:
#         self.level = level
#         self.health_points = 50 * level
#         self.attack_power = 120 * level

#     def attack(self): 
#         print(f"Атакует с силой: {self.attack_power}")

#     def __str__(self) -> str:
#         return f"Elf (уровень: {self.level}, HP: {self.health_points})"

# elf = Elf(level = 5)
# elf.attack()
# print(elf)

class Storage:
    def __init__(self, *, level: int) -> None:
        self.level = level
        self.health_points = self.race_health_points * level 
        self.attack_power = self.race_attack_power * level 

    def attack(self, *, target: "Storage") -> None: 
        print( 
            f"{self.race_name} (HP: {self.health_points}) +-|=====- {target.race_name} (HP: {target.health_points})" 
        )
        target.health_points -= self.attack_power
        print(f"{target.race_name} (HP: {target.health_points})") 

    def is_alive(self) -> bool: 
        return self.health_points > 0

    def __str__(self) -> str: 
        return f"{self.race_name} >>> (уровень: {self.level}, HP: {self.health_points})"

class Ork(Storage):
    race_health_points = 100
    race_attack_power = 10
    race_name = "Орк"

class Elf(Storage):
    race_health_points = 40
    race_attack_power = 30
    race_name = "Эльф"

class Dwarf(Storage):
    race_health_points = 65
    race_attack_power = 20
    race_name = "Дворф"

def fight(*, race_1: Storage, race_2: Storage) -> None:
    while race_1.is_alive() and race_2.is_alive():
        race_1.attack(target=race_2)
        if race_2.is_alive():
            race_2.attack(target=race_1)

    print(f"{race_1}, {race_1.is_alive()}") 

elf = Elf(level=10)
dwarf = Dwarf(level=12)

# Начало боя
fight(race_1=elf, race_2=dwarf)