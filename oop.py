# class Human:        #head
#     #атрибуты
#     name = 'Ivan'   #body
#     age = 18

# #обьект(экземпляр класса)
# human1 = Human()
# print(human1.age)






# class Human:        #head
#     def __init__(self,name,age) :#вызывается когда создаем обьект
#         #атрибуты
#         self.name = name   #body
#         self.age = age
#         #self - ссылка на обьект
#     def run(self):
#         print(f"{self.name} побежал")

# #обьект(экземпляр класса)
# human1 = Human("Pavel", 21)
# # print(human1.age)
# human1.run()

# human2 = Human("Egor", 33)
# human2.run()





# #родительский класс - он дает свои методы и атрибуты дочерним классам
# class A:
#     def __init__(self, name) :
#         self.name = name
#     def one(self):
#         print("method one class A")

#     def two(self):
#         print("method two class A")

# #дочерний класс - он берет методы и атрибуты родительского класса
# class B(A):
#     def __init__(self, name,age):
#         super().__init__(name)# вызываю родительский метод
#         self.age = age
#     #переделал метод two
#     def two(self):
#         super().two()
#         print("method two class B")

#     #добавил новый метод
#     def three(self):
#         print("method three class B")
# #15:45     -----     15:55

# a = A("a")
# # a.one()

# b = B("b")
# # b.one()
# b.two()
# # b.three()










# import random

# class Tank:
#     def __init__(self, model, armor, min_damage, max_damage, health) :
#         self.model  = model
#         self.armor = armor
#         self.damage  = random.randint(min_damage, max_damage)
#         self.health  = health


#     def info(self):
#         print(f"{self.model} имеет лобовую броню {self.armor}мм при {self.health}ед. здоровья и урон в {self.damage} единиц")

#     def shot(self,enemy):
#         #отнимаем здоровье и при этом снижаем урон
#         enemy.health -= (self.damage - self.damage * enemy.armor / 100)
#         print(f"\n{self.model}:")
#         print(f"Точно в цель, у противника {enemy.model} осталось {enemy.health} единиц здоровья")


# class SuperTank(Tank):
#     def __init__(self, model, armor, min_damage, max_damage, health, change_two_shot) :
#         super().__init__(model, armor, min_damage, max_damage, health)
#         self.change_two_shot = change_two_shot

#     def shot(self, enemy):
#         if random.randint(1,101) <= self.change_two_shot:
#             super().shot(enemy)
#             print("\nдвойной выстрел")
#             super().shot(enemy)
#         else:
#             super().shot(enemy)

# tank1 = Tank("T-34", 30, 98, 176, 300)
# tank2 = Tank("Tiger", 50, 50, 101, 400)
# tank_super = SuperTank("TigerSuper", 50, 50, 101, 400,30)

# tank1.info() 
# tank_super.info()
# while True:
#     #смотрю на исход по сдоровью
#     if tank1.health <= 0 and tank_super.health <= 0:
#         print("\nничья")
#         break #выход из цикла
#     elif tank1.health <= 0 :
#         print("\nвыиграл ", tank_super.model)
#         break
#     elif tank_super.health <= 0 :
#         print("\nвыиграл ", tank1.model)
#         break
#     tank1.shot(tank_super)
#     tank_super.shot(tank1)











import random

class User:
    def __init__(self, min_damage, max_damage, health, name) :
        self.damage  = random.randint(min_damage, max_damage)
        self.health  = health
        self.name = name
    
    def info(self):
        print(f"{self.name} имеет {self.health}ед. здоровья и урон в {self.damage} единиц")

    def attack(self,enemy):
        enemy.health -= self.damage
        print(f"\n{self.name}:")
        print(f"Точно в цель, у противника {enemy.name} осталось {enemy.health} единиц здоровья")

class Mag(User):
    def __init__(self, min_damage, max_damage, health, name, armor):
        super().__init__(min_damage, max_damage, health, name)
        self.armor = armor
    
    def attack(self,enemy):
        enemy.health -= (self.damage - self.damage * enemy.armor / 100)
        print(f"\n{self.name}:")
        print(f"Точно в цель, у противника {enemy.name} осталось {enemy.health} единиц здоровья")

class Warrior(User):
    def __init__(self, min_damage, max_damage, health, name, armor):
        super().__init__(min_damage, max_damage, health, name)
        self.armor = armor
    
    def attack(self,enemy):
        enemy.health -= (self.damage - self.damage * enemy.armor / 100)
        print(f"\n{self.name}:")
        print(f"Точно в цель, у противника {enemy.name} осталось {enemy.health} единиц здоровья")

class Archer(User):
    def __init__(self, min_damage, max_damage, health, name, armor):
        super().__init__(min_damage, max_damage, health, name)
        self.armor = armor
    
    def attack(self,enemy):
        enemy.health -= (self.damage - self.damage * enemy.armor / 100)
        print(f"\n{self.name}:")
        print(f"Точно в цель, у противника {enemy.name} осталось {enemy.health} единиц здоровья")


Bob = Warrior(10,20,100,'Bob',5)
Din = Archer(10,20,70,'Din',10)

Bob.info() 
Din.info()
while True:
    if Bob.health <= 0 and Din.health <= 0:
        print("\nничья")
        break 
    elif Bob.health <= 0 :
        print("\nвыиграл ", Din.name)
        break
    elif Din.health <= 0 :
        print("\nвыиграл ", Bob.name)
        break
    Bob.attack(Din)
    Din.attack(Bob)
