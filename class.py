# 1
# class Point3D:
#
#     def __init__(self, x=0, y=0, z=0):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def pos(self):
#         print(f'x = {self.x}, y = {self.y}, z = {self.z}')
#
#     def dist(self,a , b):
#         return b - a
#
#     def dist2(self):
#         return f'расстояние от x до y = {self.dist(self.x, self.y)}. \nРасстояние от y до z = {self.dist(self.y, self.z)}'
#
#
# first = Point3D(2,5,8)
# second = Point3D(5,3,7)
# third = Point3D(1,8,9)
# first.pos()
# print(first.dist2())

# 2
# class cube:
#     def __init__(self, a):
#         self.a = a
#
#     def sq(self, a):
#         return a * a
#
#     def per(self, a):
#         return a * 4
#
#     def ret(self):
#         return f'Площадь квадрата = {self.sq(self.a)}. \nПериметр квадрата = {self.per(self.a)}.'
#
# a = cube(6)
# print(a.ret())

# 3
# class triangle:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def s(self):
#         s_answer = 0.5 * self.a * self.b
#         return s_answer
#
#     def per(self):
#         per_answer = (self.a ** 2 + self.b ** 2) ** 0.5
#         per_answer = self.a + self.b + per_answer
#         return per_answer
#
# a = 5
# b = 8
#
# nums = triangle(a, b)
#
# s_answer = nums.s()
# per_answer = nums.per()
#
# print(f'Площадь треугольника с катетами {a} и {b} равна {s_answer}.\nПериметр треугольника с катетами {a} и {b} равен {per_answer}.')

#4
# class distance:
#
#     def __init__(self, x=0, y=0, c=0):
#         self.x = x
#         self.y = y
#         self.c = c
#
#     def dist(self,a , b):
#         return b - a
#
#     def dist2(self):
#         return f'расстояние от x до y = {self.dist(self.x, self.y)}. \nРасстояние от y до c = {self.dist(self.y, self.c)}'
#
#
# first = distance(2,4,12)
# print(first.dist2())

#5
# class CPerson:
#
#     def __init__(self, name, second_name, surname, day, mounth, years, gender):
#         self.name = name
#         self.second_name = second_name
#         self.surname = surname
#         self.day = day
#         self.mounth = mounth
#         self.years = years
#         self.gender = gender
#
#     def say(self, message):
#         print(message)
#
#     def info(self):
#         self.say(f'Фамилия: {self.second_name}\nИмя: {self.name}\nОтчество: {self.surname}\nДата роджение: День: {self.day} Месяц: {self.mounth} Год: {self.years}\nПол: {self.gender}\n')
#
# alexander = CPerson('Александ', 'Рамшов', 'Темофеевич', 9, 6, 2000, 'Man')
# anatoli = CPerson('Анатолий', 'Топов', 'Витальевич', 17, 6, 2003, 'Man')
# artemi = CPerson('Артемий', 'Зернов', 'Елесеевич', 27, 6, 1992, 'Man')
#
# alexander.info()
# anatoli.info()
# artemi.info()

#6
# class phone:
#     def __init__(self, number, model, weight):
#         self.number = number
#         self.model = model
#         self.weight = weight
#
#     def Call(self, name):
#             print('Звонит', name)
#
#     def Number(self):
#         return self.number
#
# phone_1 = phone('742562458', 'HARs6', '180g')
# phone_2 = phone('457246846', 'HSTS26', '180g')
# phone_3 = phone('145135846', 'JSSTRss', '175g')
#
# print('1 телефон')
# print('Номер:', phone_1.number)
# print('Модель:', phone_1.model)
# print('Вес:', phone_1.weight)
# phone_1.Call('Джон')
# print('Номер телефона:', phone_1.Number())
#
# print('2 телефон')
# print('Номер:', phone_2.number)
# print('Модель:', phone_2.model)
# print('Вес:', phone_2.weight)
# phone_2.Call('Алиса')
# print('Номер телефона:', phone_2.Number())
#
# print('3 телефон')
# print('Номер:', phone_3.number)
# print('Модель:', phone_3.model)
# print('Вес:', phone_3.weight)
# phone_3.Call('Питер')
# print('Номер телефона:', phone_3.Number())

#7
# class Reader:
#     def __init__(self, name, num, book, date, phone):
#         self.name = name
#         self.num = num
#         self.book = book
#         self.date = date
#         self.phone = phone
#
#     def takebook(self, numbs):
#         print(f"{self.name} взял {numbs} книги")
#
#     def returnbook(self, numbs):
#         print(f"{self.name} вернул {numbs} книги")
#
# reader = Reader("Петров В. В.", 5373, "Физика", "15.27.2023", "+7767368356")
# reader.takebook(3)
# reader.returnbook(3)
