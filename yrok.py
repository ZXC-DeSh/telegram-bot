# Для скачивания pip (un)install    (и библиотека);    help('modules')
# import random

# rand_num = random.randint(1, 10)
# print(rand_num)

# list_num = [1, 4 , 23, 45 , 76]
# random_list = random.choice(list_num)
# print(random_list)

# import emoji
#  print(emoji.emojize(':red_heart:', variant = 'emoji_type'))

# x = 'hello'
# for i in x:
#     print(i)        #Всегда после цикла ставить пробел

# for i in range(0, 101, 2   ):     #Можно указать кол-во повторов;  3 число это шаг на который прибавляется у числу 
#     print(i)      

# me_list = []

# for i in me_list:








# salary = []

# for i in range(3):
#     your_salary = int(input('Ваша зп: '))
#     salary.append(your_salary)

# print(salary)
# result = sum(salary)* 0.3
# print ('Если ты копил бы 6 месяцев(30% от зп), то у вас было бы: ', result )











# import random

# rand_num = [random.randint(1, 10) for i in range(30)]
# print(rand_num)
# print(rand_num.count(5))









# magazin = {'milk':'молоко', 'shop':"магазин", 'key':'value', }       #ключ и значение
# print(magazin['shop'], magazin['key'])

# word = input('Слово ', )
# print(word, ' перевод ', magazin.get(word))

# if word in magazin:
#     print(word, ' перевод ', magazin[word])
# else:
#     print('Слова нема')













# cinema = {'Матрица':'Киана Ривс', 
#     'титаник':'Леонардо Дикаприо', 
#     'Смешарики':['Нюша','Крош'],
#     'Форсаж':'Дуэйн Джонсон',}


# actor_fav = 'Дуэйн Джонсон'
# film = input('Введите фильм ')
# if film in cinema:
#     actor = cinema.get(film)
#     if actor == actor_fav:
#         print('Буду смотреть ')
#     else:
#         print('Не буду смотреть')
# else:
#     print('Такого фильма нет в словаре')




# quest = [   
#     {   
#         'quest':'Сколько раз ёжик роявлялся в 1 сезоне', 
#         'variant':['100', '200', '150', '120'],
#         'otvet': 1
#     },

#     {
#         'quest':'Кто снимался в форсаже', 
#         'variant':['Леонардо Дикаприо', 'Дуэйн Джонсон', 'Киана Ривс', 'Нюша'],
#         'otvet': 2
#     },

#      {
#         'quest':'Когда вышел фильм Аватар', 
#         'variant':[2009, 2011, 2015, 2222],
#         'otvet': 1
#     }
# ]


# for i in quest:
#     print(i['quest'], i['variant'])
#     var_ans = int(input('Введите вариант ответа '))
#     if var_ans == i['otvet']:
#         print('Всё правильно')
#     else:
#         print('не правильно')











# temp = []
# for day in range(7):
#     day_t = int(input('Температура сегодня '))
#     temp.append(day_t)

# mean = sum(temp) / len(temp)
# print('-' * 50)
# print('cr. temp: ', mean)











# actor = input('Ваш любимый актёр ')
# rating = int(input('рейтинг фильма'))

# # and - и     or - или



# if actor == "Киана Ривс" and rating > 6: 
#     print('Буду смотреть ')

# elif actor == "Том Холланд" or rating > 8:
#     print('Буду смотреть с удовольствием')

# elif actor == "Том Круз":
#     print('Буду смотреть с удовольствием')

# else:
#     print('Не буду смотреть ')










# import random
# user = int(input('Ваше число  '))
# comp = random.randint(1,10)

# diff = user-comp

# if user == comp:
#     print("Поздравляем")
# elif diff == 1 or diff == -1:
#     print('Почти')
# else:
#     print('не получилось')

# if user != comp:
#     print(comp)








# temp = [1, 5, 9, 13, 17, 21]
# temp_now = int(input('Погода сегодня '))
# if temp_now == 1 or temp_now < 2:
#     print('Очень холодно')

# elif temp_now == 5 or temp_now < 9:
#     print('холодно')

# elif temp_now == 9 or temp_now < 13:
#     print('прохладно')

# elif temp_now == 13 or temp_now < 17:
#     print('тепло')

# elif temp_now == 17 or temp_now < 21:
#     print(' жарко')

# else:
#     temp_now == 21 or temp_now < 100
#     print('очень жарко')
 










# import random
# user = int(input('Орёл (1) или решка (0)? Ответ: '))
# comp = random.randint(0 , 1)

# if user == comp:
#     print("Поздравляем")
# else:
#     print('не получилось')

# if user != comp:
#     print(comp)











# quest = [   
#     {   
#         'quest':'Сколько раз ёжик роявлялся в 1 сезоне', 
#         'variant':['100', '200', '150', '120'],
#         'otvet': 1
#     },

#     {
#         'quest':'Кто снимался в форсаже', 
#         'variant':['Леонардо Дикаприо', 'Дуэйн Джонсон', 'Киана Ривс', 'Нюша'],
#         'otvet': 2
#     },

#      {
#         'quest':'Когда вышел фильм Аватар', 
#         'variant':['2009', '2011', '2015', '2222'],
#         'otvet': 1
#     }
# ]


# for i in quest:
#     print(i['quest'], i['variant'])
#     var_ans = int(input('Введите вариант ответа '))
#     if var_ans == i['otvet']:
#         print('Всё правильно')
#     else: 
#         print('не правильно')
    
# otvet = [1, 2, 1] 
# a=otvet.count(True)
# print("Верных ответов:", a)
# if a >= 2:
#   print("Ты победил")
# else:
#   print("Ты проиграл")





    



# def list_sort(lst):
#         for i in range(len(lst) - 1):
#             for s in range(len(lst) - 1 - i):
#                 if lst[s] > lst[s + 1]:
#                     lst[s], lst[s + 1] = lst[s + 1], lst[s]
#         return lst
 
# def main():
#     numders = [5, 4, -9, 33, 21]
#     print('Изначальный список:', numders)
#     list_sort(numders)
#     print('Отсортированный список:', numders)
 
# if __name__ == '__main__':
#     main()













# from random import randint #извлекаю только 1 функцию


# from tkinter import *     #import tkinter     windows = tkinter.Tk() 

# windows = Tk()

# points = 0      # для счёта правельных ответов
# cqr = 0  

# fact = [
# {'text' : 'нюша-транc', 'right' : 1},
# {'text' : 'крош-бомж', 'right' : 0},
# {'text' : 'совунья-птица', 'right' : 1},
# {'text' : 'каркарыч-перекачаный качок', 'right' : 0},
# ]


# windows.title('Тесты по Марвел')
# windows.geometry('900x450')

# def check():
#     global points, cqr
#     ans = fact[cqr]['right']
#     my_ans = var.get()
    
#     if ans == my_ans:
#         points += 1
#     if cqr<len(fact)-1:
#         cqr += 1
#         mass['text'] = fact[cqr]['text']
#     else:
#         lebel_tesult = Label(text= points, bg='green')
#         lebel_tesult.place(x=0, y=300, width=900, height=30)

# label_titel = Label(text = 'Это омега супер пупер тест', bg = "green")
# label_titel.place(x = 0, y = 10, width = 900, height = 30)

# mass = Message(text = fact[cqr]['text'], fg = 'gold', bg = 'purple', width = 600)
# mass.place(x=0, y= 100)
# mass.configure(justify=CENTER)

# var = IntVar()

# true = Radiobutton(text = 'правда', variable=var, value= 1)
# true.place(x=0, y=200)

# false = Radiobutton(text = 'неправда', variable=var, value= 0)
# false.place(x=100, y=200)

# button = Button(text='ответить', fg='blue', command=check)
# button.place(x=150, y=250)


# windows.mainloop()











# songs = {
#     'World in My Eyes': 4.86,
#     'Sweetest Perfection': 4.43,
#     'Personal Jesus': 4.56,
#     'Halo': 4.9,
#     'Waiting for the Night': 6.07,
#     'Enjoy the Silence': 4.20,
#     'Policy of Truth': 4.76,
#     'Blue Dress': 4.29,
#     'Clean': 5.83
# }
 
# count = int(input('Сколько песен выбрать? '))
# time = 0.0
 
# for i in range(count):
#     query = f'Название {i + 1} песни: '
#     song_name = input(query)
#     time += songs.get(song_name, 0)
 
# print(f'Общее время звучания песен: {round(time, 2)} минут')











# goods = {
#     'Лампа': '12345',
#     'Стол': '23456',
#     'Диван': '34567',
#     'Стул': '45678',
# }
 
# store = {
#     '12345': [
#         {'quantity': 27, 'price': 42},
#     ],
#     '23456': [
#         {'quantity': 22, 'price': 510},
#         {'quantity': 32, 'price': 520},
#     ],
#     '34567': [
#         {'quantity': 2, 'price': 1200},
#         {'quantity': 1, 'price': 1150},
#     ],
#     '45678': [
#         {'quantity': 50, 'price': 100},
#         {'quantity': 12, 'price': 95},
#         {'quantity': 43, 'price': 97},
#     ],
# }

# for name, code in goods.items():
#     quantity = 0
#     cost = 0
#     for product in store[code]:
#         item_quantity = product['quantity']
#         item_cost = product['price']
#         cost += item_quantity * item_cost
#         quantity += item_quantity
#     print('{0} - {1} шт, общая стоимость {2} рублей'.format(name, quantity, cost))












# # #кликер
# from random import randint
# from tkinter import *
# window = Tk()
# window.title('clicker')
# window.geometry('500x500')

# point = 0
# def check():
#     global point
#     point+=1
#     but.place(x=randint(50,450), y=randint(50,390))
#     lab['text'] = point



# lab = Label(text=point, fg='gold', bg='green')
# lab.place(x=10,y=10)

# but = Button(text='click me', width=20, bg='purple', command=check)
# but.place(x=250, y=250)

# window.mainloop()











# from tkinter import *

# window = Tk()
# window.geometry('900x600')
# window.title('virus')
# window.resizable(width=False, height=False)

# window.configure(bg='black')

# lab_title = Label(text = 'Это очень вредоностная программа', bg = 'red', fg = 'black', font=('Ariel',30))
# lab_title.place(x=120,y=20)

# img = PhotoImage(file='skelet.gif')

# lab_img = Label(image=img, bg = 'black')
# lab_img.place(x=130,y=250)

# lab_time = Label(text='5', bg='black',fg='red', font=('Ariel', 15))

# def start():
#     namber = int(lab_time['text'])
#     if namber>0:
#         lab_time.place(x=430, y=300)
#         lab_time['text']=namber-1
#         window.after(3000,start)
#     else:
#         wd = window.winfo_screenwidth()
#         hg = window.winfo_screenheight()
#         window.geometry(f'{wd}x{hg}')
#         img_scr = PhotoImage(file='skelet.gif', bg='black')
#         img_lab_sc = Label(image=img_scr,)
#         img_lab_sc.image = img_scr
#         img_lab_sc.place(x=0, y=0, width=wd, height=hg)
        

# # def click():
# #     print('Privet')
# #     window.after(3000, click)      # 1 число это милисекунды 2 это название функции
# def click():
#     start()

# window.protocol('WM_DELETE_WINDOW', click)


# window,mainloop()











# # кликер
# from random import randint
# from tkinter import *
# window = Tk()
# window.title('clicker')
# window.geometry('500x500')

# point = 0

# def check():
#     global point
#     point+=1
#     but.place(x=randint(50,450), y=randint(50,390))
#     lab['text'] = point

# but = Button(text='click me', width=20, bg='purple', command=check)
# but.place(x=250, y=250)

# lab = Label(text=point, fg='gold', bg='green')
# lab.place(x=10,y=10)

# window.mainloop()













# from tkinter import *

# window = Tk()
# window.geometry('900x600')
# window.resizable(width=False, height=False)

# window.configure(bg='black')

# lab_title = Label(text = 'Это очень вредоностная программа', bg = 'red', fg = 'black', font=('Ariel',30))
# lab_title.place(x=120,y=20)

# img = PhotoImage(file='skelet.gif')

# lab_img = Label(image=img, bg = 'black')
# lab_img.place(x=130,y=250)

# lab_time = Label(text='6', bg='black',fg='red', font=('Ariel', 50))

# def start():
#     namber = int(lab_time['text'])
#     if namber>0:
#         lab_time.place(x=430, y=150)
#         lab_time['text']=namber-1
#         window.after(1000,start)
#     else:
#         wd = window.winfo_screenwidth()
#         hg = window.winfo_screenheight()
#         window.geometry(f'{wd}x{hg}')
#         img_scr = PhotoImage(file='skelet.gif')
#         img_lab_sc = Label(image=img_scr)
#         img_lab_sc.image = img_scr
#         img_lab_sc.place(x=0, y=0, width=wd, height=hg)
        

# # def click():
# #     print('Privet')
# #     window.after(3000, click)      # 1 число это милисекунды 2 это название функции



# def click():
#     start()

# window.protocol('WM_DELETE_WINDOW', click)
# window,mainloop()










# from tkinter import *
# import random
 
# window = Tk()
# window.geometry('700x500')
# window.title('Кликер')
# points = 0
 
# bg_values = [ 'red', 'lime']
# bg_index = 0
 
# def check():
#     global points, bg_index
#     b.place(x=random.randint(1, 550), y=random.randint(1, 350))
#     points += 1
#     label['text'] = points
 
#     if points % 20 == 0:
#         bg_index = 0 if bg_index == len(bg_values) else bg_index + 1
#         b['bg'] = bg_values[bg_index]
 
 
# b = Button(text='click me', font=('Arial', 20), fg='green', command=check)
# b.place(x=150, y=100)
# label = Label(text=points, font=('Arial', 15), fg='gold')
# label.place(x=10, y=10)
 
# window.mainloop()











# import time
# from tkinter import *
# window = Tk()
# window.title('clicker')
# window.geometry('500x500')

# point = 0
# def check():
#     global point
#     point+=1
#     lab['text'] = point

# but = Button(text='click me', width=20, bg='purple', command=check)
# but.place(x=250, y=250)

# lab = Label(text=point, fg='gold', bg='green')
# lab.place(x=10,y=10)

# window.mainloop()












# quest = [   
#     {   
#         'quest':'Сколько раз ёжик роявлялся в 1 сезоне', 
#         'variant':['100', '200', '150', '120'],
#         'otvet': 1
#     },

#     {
#         'quest':'Кто снимался в форсаже', 
#         'variant':['Леонардо Дикаприо', 'Дуэйн Джонсон', 'Киана Ривс', 'Нюша'],
#         'otvet': 2
#     },

#      {
#         'quest':'Когда вышел фильм Аватар', 
#         'variant':['2009', '2011', '2015', '2222'],
#         'otvet': 1
#     }
# ]

# name = input('Введите ваше имя:  ')
# pr=0
# nepr=0
# for i in quest:
#     print(i['quest'], i['variant'])
#     var_ans = int(input('Введите вариант ответа '))
#     if var_ans == i['otvet']:
#         print('Всё правильно')
#         pr+=1
#     else: 
#         print('не правильно')
#         nepr+=1
    
# file = open('result.txt', 'a', encoding='UTF-8')
# file.write(f'имя - {name} очки - {pr}\n')
# file.close()

# print('-'*50)
# file = open('result.txt', 'r', encoding='UTF-8')
# print(*file)   #1
# print(file.read())   #2

# for i in file.readlines():   #3
#     print('строка',i)
# file.close()

# otvet = [1, 2, 1] 
# a=otvet.count(True)
# print("Верных ответов:", a)
# if a == 3:
#     print("Ты победил")
# else:
#     print("Ты проиграл")










# def plus(a,b):
#     return a+b

# def minus(a,b):
#     return a-b

# num1 = int(input('Введите число: '))
# num2 = int(input('Введите число: '))

# qwst = input('+ or -  ')
# if qwst== "+":
#     print(plus(num1,num2))
# elif qwst=='-':
#     print(minus(num1, num2))











# def summa_n(a):
#   num = 0
#   for i in range (1, a+1):
#       num += i
#   print(f'\nЯ знаю, что сумма чисел от 1 до {a} равна {num}')

# sum = int(input('Введите число: '))
# summa_n(sum)


# def greeting():
#     print('Привет!')
#     print('Добро пожаловать!')
# for i in range(1):
#     a = input('Зайдёте? Да/Нет: ')

# if a == 'Да':
#     greeting()

# print('Следующий.\n')


# def ymn(a,b):
#     return a*b

# def dil(a,b):
#     return a/b

# num1 = int(input('Введите число: '))
# num2 = int(input('Введите число: '))

# qwst = input('/ or *  ')
# if qwst== "*":
#     print(ymn(num1,num2))
# elif qwst=='/':
#     print(dil(num1, num2))













# from tkinter import *
# from random import *

# points_b1 = 0
# points_b2 = 0
# points = 0

# def but_change(b):
#     b['text'] = 'Ну пожалуйста'
#     b['bg'] = 'blue'
#     b['fg'] = 'white'
#     global points_b1, points_b2
#     points_b1, points_b2 = 0, 0

# def points_update():
#     global points
#     points += 1
#     label['text'] = f'Ваши очки: {points}'

# def b1_func():
#     points_update()
#     b1.place(x=randint(1, 500), y=randint(1, 550))

#     global points_b1
#     global points_b2
#     points_b1 += 1
#     points_b2 -= points_b2

#     if points_b1 >= 10:
#         but_change(b2)
#     else:
#         b1['text'] = 'click me'
#         b1['bg'] = 'green'
#         b1['fg'] = 'black'

# def b2_func():
#     points_update()
#     b2.place(x=randint(1, 500), y=randint(1, 550))

#     global points_b1
#     global points_b2
#     points_b2 += 1
#     points_b1 -= points_b1

#     if points_b2 >= 10:
#         but_change(b1)
#     else:
#         b2['text'] = 'click me'
#         b2['bg'] = 'yellow'
#         b2['fg'] = 'black'











# win = Tk()
# win.geometry('800x600+250+80')
# win.title('Кликер :D')

# b1 = Button(text='click me', font=('Calibri', 15), bg='green', command=b1_func)
# b2 = Button(text='click me', font=('Calibri', 15), bg='yellow', command=b2_func)

# b1.place(x=150, y=200)
# b2.place(x=450, y=200)

# label = Label(text=f'Ваши очки: {points}', fg='gold', bg='green', font=('Calibri', 17))
# label.place(x=10, y=10)


# win.mainloop()














# from tkinter import *
# import random
# import time
# window = Tk()
# window.geometry('800x600')
# window.title('Кликер')
# points = 0

 
# def check():
#     global points
#     b.place(x=random.randint(1, 550), y=random.randint(1, 500))
#     points += 1
#     label['text'] = points
 
#     if points % 20 == 0:
#         time.sleep(2)

 
# b = Button(text='click me', font=('Arial', 16), fg='black', bg='red', command=check)
# b.place(x=150, y=100)
# label = Label(text=points, font=('Arial', 16), fg='black', bg='red')
# label.place(x=10, y=10)


# window.mainloop()












# from tkinter import *
 
# def lot():
#     lbl.config(text = 'Чтобы забрать выйгрыш необходимо внести 1000руб.',font=("Arial", 30))
#     btn.destroy() 
    
# window = Tk()
# window.geometry('400x250')
# window.columnconfigure(index=1, weight=3)
# lbl = Label(window, text="ВЫ ВЫЙГРАЛИ В ЛОТЕРЕЕ!", font=("Arial", 50))
# lbl.grid(column = 1, row = 2)
# btn = Button(window, text="ПОЛУЧИТЬ ВЫЙГРЫШ!", font=("Arial", 50), command = lot)
# btn.grid(column=1, row=3)
# window.overrideredirect(1)
# window.state('zoomed')
# window.mainloop()








# N = int(input())
# lst = list()
# for i in range(N): lst.append(int(input()))
# print(lst)
# _min = min(lst)
# ind_min = lst.index(_min)
# _max = max(lst)
# ind_max = lst.index(_max)
# lst[ind_min] = _max
# lst[ind_max] = _min
# print(lst) 








# N = int(input('Введите кол-во собак и их очки: '))
# lst = list()
# for i in range(N): lst.append(int(input()))
# print(lst)
# min = min(lst)
# ind_min = lst.index(min)
# max = max(lst)
# ind_max = lst.index(max)
# lst[ind_min] = max
# lst[ind_max] = min
# print(lst)








# import random
# import requests
# from bs4 import BeautifulSoup
# # response = requests.get('https://i-fakt.ru/')
# # print(response)                                     # Запрос статуса страницы

# def fact():
#     response = requests.get('https://i-fakt.ru/')
#     response = response.content

#     html = BeautifulSoup(response, 'html.parser')
#     cont = html.find_all(class_ = 'p-2 clearfix')
#     fact_main = random.choice(cont)
#     print(fact_main.text)
#     print(fact_main.a.attrs['href'])
# fact()

# def festival():
#     response = requests.get('https://kudago.com/msk/festival/')
#     response = response.content

#     html = BeautifulSoup(response, 'html.parser')
#     cont = html.find_all(class_ = 'post-header')
#     fact = random.choice(cont)
#     print(fact.text)
#     print(fact.a.attrs['href'])

# festival()










# import requests
# from re import findall
 
 
# response = requests.get(input('Вставьте ссылку: ')).text
# result = findall(r'>.+</h3>', response)
# release = list(map(lambda x: x[1:-5], result))
# print(release)











# import requests
# from bs4 import BeautifulSoup

# html = 'https://webscraper.io/test-sites/e-commerce/ajax/computers/tablets'
 
# soup = BeautifulSoup(requests.get(html).text, "html.parser")
# list = soup.select_one("div.ecomerce-items-ajax")['data-items']
# print(list)










# import random 
# import requests
# from bs4 import BeautifulSoup
# response = requests.get('https://store.steampowered.com/?l=russian')
# print(response)                                     

# def ecshon():
#     response = requests.get('https://store.steampowered.com/?l=russian')
    
#     html = BeautifulSoup(response.content, 'html.parser')
#     cont = html.find_all(class_ = 'popup_menu_subheader reduced_vspace')
#     print(cont.text)
    

# def sport():
#     response = requests.get('https://store.steampowered.com/?l=russian')
#     response = response.content

#     html = BeautifulSoup(response, 'html.parser')
#     cont = html.find_all(class_ = 'popup_genre_expand_content responsive_hidden')
#     fact = random.choice(cont)
#     print(fact.text)


# def simulator():
#     response = requests.get('https://store.steampowered.com/?l=russian')
#     response = response.content

#     html = BeautifulSoup(response, 'html.parser')
#     cont = html.find_all(class_ = 'popup_genre_expand_content responsive_hidden')
#     fact = random.choice(cont)
#     print(fact.text)

# ecshon()












# import math
# x = 1

# while x<10:       #ПРОВЕРЯЮ КАК УСЛОВИЕ if mnogo raz
#     print(x**3)
#     print(math.sqrt(x))
#     x+=2
# else:
#     print('Konec')





# x = 10
# while x>=0:
#     print(x)
#     x-=1









# import random
# import requests
# from bs4 import BeautifulSoup
# # response = requests.get('https://i-fakt.ru/')
# # print(response)                                     # Запрос статуса страницы

# def get_interesting_fact():
#     response = requests.get('https://i-fakt.ru')
#     response = response.content
#     html = BeautifulSoup(response, 'html.parser')
#     fact = random.choice(html.find_all(class_='p-2 clearfix'))
#     print(fact.text)
#     print(fact.a.attrs['href'])

# def get_event():
#     response = requests.get('https://kudago.com/msk/festival/')
#     response = response.content
#     html = BeautifulSoup(response, 'html.parser')
#     event = random.choice(html.find_all(class_='post-title'))
#     print(event.text)
#     print(event.a.attrs['href'])

# def get_concert():
#     response = requests.get('https://kudago.com/msk/concerts/')
#     response = response.content
#     html = BeautifulSoup(response, 'html.parser')
#     concert = random.choice(html.find_all(class_='post-title'))
#     print(concert.text)
#     print(concert.a.attrs['href'])

# user_wish = ""
# while user_wish != 'выйти':
#     user_wish = input('Выберите тему: ').lower()   #Привожу к нижнему регистру
#     if "фестиваль" in user_wish:
#         get_event()
#     if "фестиваль" in user_wish:
#         get_concert()
#     if "фестиваль" in user_wish:
#         get_interesting_fact()










# sum = int(input("ckoka nakopit: "))
# day_m = int(input("ckoka otkladvat: "))
# bank = 0
# moth = 0
# while bank < sum:
#     bank+=day_m
#     moth+=1
# print(moth)








# from fpdf import FPDF

# pdf = FPDF(orientation="p", unit="cm", format=(10,15))

# pdf.add_page()
# pdf.add_font('courier',"",'C:\WINDOWS\FONTS\COUR.ttf', uni=True)
# pdf.set_font('courier', size=16)

# pdf.set_fill_color(0,223,0)
# pdf.set_draw_color(150,50,42)
# pdf.set_text_color(224,4,64)

# pdf.cell(align='C', fill=True, txt='dflkhgvadojhf', w=5, h=5, border=1)

# pdf.image('saske.jpg', x=7, y=1, w=3, h=3)

# pdf.output('chafir.pdf')









# number = int(input('Введите число: '))
# summa = 0
# while number != 0:
#     summa += number
#     number = int(input('Введите следующее число или 0 для завершеня программы: '))
# print(summa)






# password = int(input('Введите пароль: '))
# while password != 235:
#     print('Пароль не верен! ')
#     password = int(input('Введите пароль еще раз: '))
# print('Пароль верный! Добро пожаловать.')





# try:
#     age = int(input('Введите возраст '))

# except:    
#     print('Вы сделали что-то не так')

# else:
#     print('Вам: ', age)

# finally:
#     print('GOOD')











# def calculator():
#     try:
#         num1 = int(input('Введите первое число: '))
#         num2 = int(input('Введите первое число: '))
#     except:
#         print('неправильно')
#         calculator()
        
#     method = input('Выберите знак - + * /: ')
#     if method in "- + * /":
#         print()
#     else:
#         print('неправильно выбран знак')
#         calculator()
#     if method == '+':
#         print(num1 + num2)
#     elif method == '-':
#         print(num1 - num2)
#     elif method == '*':
#         print(num1 * num2)
#     elif method == '/':
#         print(num1 / num2)

# calculator()








# def deskriminant():
#     try:
#         a = int(input('Введите первое число a: '))
#         b = int(input('Введите первое число b: '))
#         c = int(input('Введите первое число c: '))
#     except:
#         print('неправильно')
#         deskriminant()
    
#     disktim = b*b-4*a*c
#     print('Ваш дискриминант: ', disktim)

# deskriminant()









# from random import randint
# lst = [randint(2, 8) for i in range(30)]
# print(lst)
# print('Чисел 2: ',lst.count(2))
# print('Чисел 3: ',lst.count(3))
# print('Чисел 4: ',lst.count(4))
# print('Чисел 5: ',lst.count(5))
# print('Чисел 6: ',lst.count(6))
# print('Чисел 7: ',lst.count(7))
# print('Чисел 8: ',lst.count(8))








# from tkinter import *

# window = Tk()
# window.geometry('')

# canvas = Canvas(window,width=800,height=600,bg='white')
# canvas.pack()

# # # canvas.create_rectangle(10,10,120,120,fill='red',outline='')

# # # canvas.create_rectangle(10,10,70,70,fill='yellow',outline='black')

# # canvas.create_rectangle(50,50,150,150,fill='yellow',outline='black')
# # canvas.create_polygon(50,50,100,0,150,50,fill='yellow',outline='black')
# # canvas.create_rectangle(75,75,125,125,fill='blue',outline='black')

# class Home:
#     def __init__(self,roof_color,wall_color,number) -> None:
#         self.roof_color = roof_color
#         self.wall_color = wall_color
#         self.number = number
#         self.height = 130
#         self.width = 140
#         self.wall = None
#         self.roof = None

#     def build(self,x,y):
#         w = self.width
#         h = self.height

#         self.roof = canvas.create_polygon(x,y,
#                             x+w,y,
#                             x+w/2,h-100,
#                             fill=self.roof_color,
#                             outline='black')
#         self.wall = canvas.create_rectangle(x+20,y,
#                                             x+120,y+100,
#                                             fill=self.wall_color,
#                                             outline='black')
#     def info_home(self):
#         print(f'цвет крыши {self.roof_color} \nцвет стен {self.wall_color} \nномер дома {self.number}  ')

# home_1 = Home('yellow','red',1)
# home_1.build(100,100)
# home_1.info_home()

# window.mainloop()












# from random import randint 
 
# x = ["Привет","Прииивеет","Hi"] 
# y = ["Мстители","Железный человек","Тор"] 
 
# while(True): 
#     temp = input() 
#     if(temp.lower() == "привет"): 
#         print(x[randint(0, len(x) - 1)]) 
#     elif(temp.lower() == "фильм"): 
#         print(y[randint(0, len(y) - 1)])










# #кортеж
# def func (a,b,*args, **kwargs):
#     print(a)
#     print(b)
#     print(args)
#     print(type(args))
#     print(kwargs)

# func(1,2,23,34,45,56,76, c = 1, d = 2)








# #list
# x = [1,2,3]
# x[0] = 2
# print(x)
# #tuple
# y = (1,2,3)
# y[0] = 2













# age = 18

# if age < 18:
#     is_allow = False
# else:
#     is_allow = True

# is_allow = 'yes' if age >= 18 else 'no'
# print(is_allow)










# val = None

# if val is None:
#     res = []
# else:
#     res = val
# res =[] if val is None else val

# res = val or 1

# print(res)




# a = 'hello'
# b = 123
# c = [1,2,3]
# for i in a:
#     print(i)






# div_2 = []
# for i in range(0,250):
#     if i != 0 and (i % 30 == 0 or i % 31 == 0):
#         div_2.append(i)

# div_2 = [i**3 if i > 50 else i for i in range(0,100) if i % 5 == 0]

# print(div_2)










# a = {x: len(x for x in ['apple', 'orange', 'dfgfghsfgh', 'banana'])}
# print(a)






# x = tuple()
# y = (1,2,3,4)
# print(y[0])
# y = {(1,2)}







# def func(*args):
#     a = list(args)
#     b = [i for i in a if i % 2 == 0 ]
#     c = [i for i in a if not i % 2 == 0 ]
#     print(b,c)
    
# print(func(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))






# a = (5, 3, 2, 1, 4)
# a = tuple(sorted(a))
# print(a)












# print(id(1), type(1))









# class A:
#     def pyblic(self):
#         print('pyblic')
#     def _private(self):
#         print('_private')
#     def __protect(self):
#         print('__protect')

# a = A()
# a.pyblic()
# a._private()
# a._A__protect()













# class Singleton:
#     def __new__(cls):
#         if not hasattr(cls,'instance'):
#             cls.instance = super().__new__(cls)
#         return cls.instance
    
#     def __init__(self, a=1,b=2):
#         self.a = a
#         self.b = b

#     def info(self):
#         print(self.a,self.b)

# print(dir(Singleton))

# s = Singleton()
# print('Object created', s, id(s))
# print(dir(Singleton))
# sl = Singleton()
# print('Object created', sl, id(sl))














# def a(func): #декоратор
#     def c(): #новая функция
#         print('new')
#         func()
#     return c

# @a
# def b():
#     print('old')

# b()









# import time

# def timeit(func):
#     def wrapper(val):
#         start = time.time()
#         res = func(val)
#         end = time.time()
#         print('time=', end - start)
#         return res
#     return wrapper

# @timeit
# def get_list(val):
#      return [x for x in range(val) if x % 2 == 0]
    
# a = get_list(10000000)














# class Cerdce:
#     pass
# class Zeiudoc:
#     pass
# class Brain:
#     pass

# class PeopleКомпозиция:
#     def __init__(self) -> None:
#         self.cerdce = Cerdce()
#         self.zeiudoc = Zeiudoc()
#         self.brain = Brain()

# people1 = People()



# class PeopleАссоциация:
#     def __init__(self,cerdce,zeiudoc,brain) -> None:
#         self.cerdce = cerdce
#         self.zeiudoc = zeiudoc
#         self.brain = brain

# cerdce1 = Cerdce()
# zeiudoc1 = Zeiudoc()
# brain1 =  Brain()

# people2 = PeopleАссоциация(cerdce1,zeiudoc1,brain1)










# # Простая реализация работника 
# name = input('Введите имя сотрудника: ')
# salary = int(input('Введите ЗП сотрудника: '))

# print(f'У {name} зарплата в месяц = {salary}')
# print(f'Тогда в год он получает {salary * 12}')



# Реализация сотрудников через словарь

# employees_list = [
#     {
#         'name': 'Данил',
#         'salary': 500_000
#     },
#     {
#         'name': 'Дарья',
#         'salary': 555_000
#     },
#     {
#         'name': 'Юрий',
#         'salary': 600_000
#     }
# ]
# print(employees_list)

# for employee in employees_list:
#     if employee['name'] == 'Данил':
#         employees_list.remove(employee)
#         break

# print(employees_list)
# print(len(employees_list))


# class Employee:
#     def __init__(self, name, salary,on_vacation,is_good_employee):
#         self.name = name
#         self.salary = salary
#         self.on_vacation = on_vacation
#         self.is_good_employee = is_good_employee
    
#     def get_info(self):
#         print(f'У {self.name} ЗП в месяц = {self.salary}. В отпуске? - {self.on_vacation}; Это хороший работник? - {self.is_good_employee}')
    
#     def year_salary(self):
#         print(f'Годовая зп = {self.salary * 12}')



# employees_list = [Employee('Анна', 270_000, True,True), Employee('Василий', 158_000,False,True), Employee('Антон', 100_000,True,True),Employee('Egor', 120_000,True,True),Employee('Gena', 10_000,True,False)]

# # for employee in employees_list:
# #     employee.get_info()
# #     employee.year_salary()

# for employee in employees_list:
#     if  employee.is_good_employee == False:
#         employees_list.remove(employee)
#         break

# for employee in employees_list:
#     employee.get_info()
#     employee.year_salary()

















# class MyFile: 
#     def __init__(self, name, mode, encoding='utf-8'): 
#         self.name = name 
#         self.mode = mode 
#         self.encoding = encoding 
 
#     def __enter__(self): 
#         self.file = open(self.name, self.mode, encoding=self.encoding) 
#         return self.file 
 
#     def __exit__(self, exc_type, exc_val, exc_tb): 
#         self.file.close()

# with MyFile('file.txt', 'r', encoding='utf-8') as file: 
#     # Выполняем операции с файлом 
#     content = file.read() 
#     print(content) 















# class EndlessIterator: 
#     def __init__(self, start): 
#         self.start = start 
 
#     def __iter__(self): 
#         return self 
 
#     def __next__(self): 
#         self.start += 1 
#         return self.start - 1

# my_iterator = EndlessIterator(0)

# for i in my_iterator: 
#     print(i) 














# class Item:
#     def __init__(self, price,brand) -> None:
#         self.price = price
#         self.brand = brand

#     def __repr__(self) -> str:
#         return self.brand
    
# Items_list = [
#     Item(1000, 'Apple'),
#     Item(1200,'Apple'),
#     Item(900,'Sumsung'),
#     Item(700,'Sumsung'),
#     Item(660,'Xiaomi'),
# ]

# result = list(filter(lambda item: item.brand == 'Xiaomi', Items_list))
# print(result)














# names_list = ['данил', 'артём', 'никита', 'влад']
# result = list(map(lambda x:x.title(),names_list))
# print(result)







# s = '1' + '0'* 33
# while '1' in s or '100' in s:
#     if '100' in s:
#         s = s.replace('100','0001', 1)
#     else:
#         s = s.replace('1','00',1)
# print (s)












# def strcounter(string):
#     for symbol in string:
#         counter = 0
#         for sub_symbol in string:
#             if symbol == sub_symbol:
#                 counter += 1
#         print(symbol, counter)

# strcounter('fdsadfgadfg')

# def strcounter(string):
#     for symbol in set(string):
#         counter = 0
#         for sub_symbol in string:
#             if symbol == sub_symbol:
#                 counter += 1
#         print(symbol, counter)

# strcounter('fdsadfgadfg')

def strcounter(string):
    syms_counter = {}
    for symbol in string:
        syms_counter[symbol] = syms_counter.get(symbol, 0) + 1
    print(syms_counter)

strcounter('dfhgsdhsfgjh')






