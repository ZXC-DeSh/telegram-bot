# import json
# import requests
# fast_ship = ""
# url='https://swapi.dev/api/'
# r = requests.get(url).json()
# # print(type(r))
# people_api = r.get('people')
# planet_api = r.get("planets")
# starships_api = r.get('starships')

# def check_people(url):
#     for i in range(1,6):    
#         response = requests.get(f'{url}{i}')
#         print(response.json()['name'])    #['results'][0]['name']

# check_people(people_api)

# def check_planet(url):
#     diam_pl = list()
#     for i in range(1,11):    
#         response = requests.get(f'{url}{i}').json()
#         diam_pl.append({response.get('name'):response.get('diameter')})
#     print(diam_pl)

# check_planet(planet_api)

# def check_max_atmosphering_speed_starships(url):
#     max_atmosphering_speed = list()
#     for i in range(1,11):    
#         response = requests.get(f'{url}{i}').json()
#         max_atmosphering_speed.append({response.get('name'):response.get('max_atmosphering_speed')})
    
#     print(max_atmosphering_speed)
    
# check_max_atmosphering_speed_starships(starships_api)

# def check_starships(url):

#   names = []
#   spedyy = []

#   for i in range(1, 11):
#     response = requests.get(f'{url}/{i}').json()
#     if response.get('detail') == 'Not found':
#       continue
#     if response.get('max_atmosphering_speed') == 'n/a':
#       continue

#     max_speed = response.get('max_atmosphering_speed')
#     namer = response.get('name')
#     names.append(namer)
#     spedyy.append(int(max_speed))
#   max_index = spedyy.index(max(spedyy))

#   print(names[max_index])

# check_starships(starships_api)






















# import requests  #pip install requests
# from bs4 import BeautifulSoup #pip install bs4
# from datetime import datetime
# import lxml

# url = "http://www.cbr.ru/scripts/XML_daily.asp?"
# today = datetime.today()#получаю дату
# today = today.strftime("%d/%m/%Y")#указываю дату в определенном формате

# payload = {"date_req":today}#доп параметры

# r = requests.get(url,params = payload )


# xml = BeautifulSoup(r.content,"xml")#pip install lxml



# def parse(fy,fm,fd,ly,lm,ld):#промежуток с fd/fm/fy - ld/lm/ly
#     # if fy>ly:
#     file = open("file.txt","a")

#     for y1 in range(fy,ly+1):#+1 чтобы было включительно
#         for m1 in range(fm, lm+1):

#             for d1 in range(fd,ld):
#                 m2 = m1 
#                 d2 = d1 
#                 if m1<10:
#                     m2 = f"0{m1}"
#                 if d1 < 10:
#                     d2 = f"0{d1}"    

#                 url = "http://www.cbr.ru/scripts/XML_daily.asp?"
#                 payload = {"date_req":f"{d2}/{m2}/{y1}"}#01/01/2020
#                 r = requests.get(url,params = payload )
#                 xml = BeautifulSoup(r.content,"xml")
#                 date = f"{d2}/{m2}/{y1}"
#                 res = xml.find("Valute",{"ID":"R01239"}).Value.text + " " + xml.find("Valute",{"ID":"R01239"}).CharCode.text
#                 res2 = xml.find("Valute",{"ID":"R01235"}).Value.text + " " + xml.find("Valute",{"ID":"R01235"}).CharCode.text
#                 res3 = xml.find("Valute",{"ID":"R01700J"}).Value.text + " " + xml.find("Valute",{"ID":"R01700J"}).CharCode.text
#                 print(date , res, res2, res3)
                
#                 file.write(f"{date} : {res}\n")
#     file.close()

# parse(2020,1,1,2022,12,25)










# from tkinter import *
# import requests  #pip install requests
# from bs4 import BeautifulSoup #pip install bs4
# from datetime import datetime
# import lxml

# root = Tk()

# root.configure(bg='yellow')
# root.resizable(width=False, height=False)
# root.title('Kurs')
# root.geometry('400x300+700+250')

# img = PhotoImage(file='logo.png')
# logo = Label(root,image=img)
# logo.place(x=0,y=0)

# lab = Label(root,text='Курс валют',bg='yellow',fg='blue',font='Arial 22')
# lab.place(x=160,y=25)

# url = "http://www.cbr.ru/scripts/XML_daily.asp?"

# today = datetime.today()#получаю дату
# today = today.strftime("%d/%m/%Y")#указываю дату в определенном формате
# payload = {"date_req":today}#доп параметры

# r = requests.get(url,params = payload )
# xml = BeautifulSoup(r.content,"xml")#pip install lxml

# def Course(id):
#     return xml.find("Valute",{"ID":id}).Value.text

# info_date = Label(root,text=f"Курс на {today.replace('/', '.')}",font='Arial 22',bg='yellow',fg='blue')
# info_date.place(x=100,y=160,)

# usd_course = Label(root,text=f'$ {Course("R01235")}',font='Arial 22',bg='yellow',fg='blue')
# usd_course.place(y=200,x=100) 

# eur_course = Label(root,text=f'курс юаня {Course("R01375")}',font='Arial 22',bg='yellow',fg='blue')
# eur_course.place(x=100,y=240) 

# print(Course('R01235'))

# root.mainloop()


















# import requests  #                  pip install requests
# from bs4 import BeautifulSoup #     pip install bs4
# from datetime import datetime
# import lxml   #                     pip install lxml 

# from tkinter import *

# root = Tk()

# root.title("KURS")
# root.geometry("400x700+250+250")

# #добавляю картинку
# img = PhotoImage(file = "logo.png")#загрузил картинку
# logo = Label(root, image = img )#создал надпись с картинкой
# logo.place(x = 0 , y = 0)#разместил ее

# #надпись
# lab = Label(root, text = "Курс валют", bg = "white", fg = "blue", font = "Arial 22")
# lab.place(y  = 25, x = 150)


# #создаю ссылку на текущую дату
# url = "http://www.cbr.ru/scripts/XML_daily.asp?"
# today = datetime.today()#получаю дату
# today = today.strftime("%d/%m/%Y")#указываю дату в определенном формате

# #делаю запрос
# payload = {"date_req":today}#доп параметры

# r = requests.get(url,params = payload )

# xml = BeautifulSoup(r.content,"xml")#pip install lxml

# #фукнция для получения курса
# def getCourse():
#     list_ui = []
#     list_valute = xml.find_all("Valute")#получаю все валюты
#     for i in list_valute:
#         list_ui.append(
#             Label(root, text=f"{i.Name.text} {i.Value.text}",font = "Arial 10")# записываю имя и значение валюты в виджет а сам виджет в список
#             )
#     for j in range(0,len(list_ui)):
#         list_ui[j].pack()

# getCourse()



# #цикл
# root.mainloop()