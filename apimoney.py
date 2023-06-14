import requests  #pip install requests
from bs4 import BeautifulSoup #pip install bs4
from datetime import datetime
import lxml

url = "http://www.cbr.ru/scripts/XML_daily.asp?"
today = datetime.today()#получаю дату
today = today.strftime("%d/%m/%Y")#указываю дату в определенном формате

payload = {"date_req":today}#доп параметры

r = requests.get(url,params = payload )


xml = BeautifulSoup(r.content,"xml")#pip install lxml



def parse(fy,fm,fd,ly,lm,ld):#промежуток с fd/fm/fy - ld/lm/ly
    # if fy>ly:
    file = open("file.txt","a")

    for y1 in range(fy,ly+1):#+1 чтобы было включительно
        for m1 in range(fm, lm+1):

            for d1 in range(fd,ld):
                m2 = m1 
                d2 = d1 
                if m1<10:
                    m2 = f"0{m1}"
                if d1 < 10:
                    d2 = f"0{d1}"    

                url = "http://www.cbr.ru/scripts/XML_daily.asp?"
                payload = {"date_req":f"{d2}/{m2}/{y1}"}#01/01/2020
                r = requests.get(url,params = payload )
                xml = BeautifulSoup(r.content,"xml")
                date = f"{d2}/{m2}/{y1}"
                res = xml.find("Valute",{"ID":"R01239"}).Value.text + " " + xml.find("Valute",{"ID":"R01239"}).CharCode.text
                print(date , res)
                
                file.write(f"{date} : {res}\n")
    file.close()

parse(2021,1,1,2022,12,25)




# def getCourse(id):
#     print(xml.find("Valute",{"ID":id}).Value.text)

# getCourse("R01235")

# x = {
#     "a":"A",
#     "b":"B"
#     }
# print(x.get("ads","Netu"))

