from tkinter import *
from random import randint

window = Tk()
window.geometry('600x600')

SOURCE = r'C:/Users/serg/Desktop/работа Егора Коробкина/хранилище файлов с питона/elements'

class Fire:
    image = PhotoImage(file=SOURCE + '/fire.png').subsample(4)
   
    def __add__(self, other):
        if isinstance(other, Wind):
            return Dust
        
    def __add__(self, other):
        if isinstance(other, Water):
            return Aroma

class Water:
    image = PhotoImage(file=SOURCE + '/water.png').subsample(4)

    def __add__(self, other):
        if isinstance(other, Earth):
            return Clay
        
    def __add__(self, other):
        if isinstance(other, Fire):
            return Aroma

class Wind:
    image = PhotoImage(file=SOURCE + '/wind.png').subsample(4)

    def __add__(self, other):
        if isinstance(other, Fire):
            return Dust
        
class Earth:
    image = PhotoImage(file=SOURCE + '/ground.png').subsample(4)

    def __add__(self, other):
        if isinstance(other, Water):
            return Clay

class Clay:
    image = PhotoImage(file=SOURCE + '/pottery.png').subsample(4)

class Dust:
    image = PhotoImage(file=SOURCE + '/dust.png').subsample(4)

class Aroma:
    image = PhotoImage(file=SOURCE + '/aroma.png').subsample(4)

# вывод на экран картинок элементов
canvas = Canvas(window, width=600, height=600)
canvas.pack()

elements = [Fire(), Earth(), Water(), Wind()]
for elem in elements:
    img = canvas.create_image(randint(50, 550), randint(50, 550), image=elem.image)


def move(event):
    images_id = canvas.find_overlapping(event.x, event.y, event.x + 10, event.y + 10) # список с объектами рядом с мышкой 

    if len(images_id) == 2:
        elem_id_1, elem_id_2 = images_id[0], images_id[1]
        element_1 = elements[elem_id_1 - 1]
        element_2 = elements[elem_id_2 - 1]

        new_element = element_1 + element_2

        if new_element:
            if new_element not in elements:
                canvas.create_image(event.x, event.y, image=new_element.image)
                elements.append(new_element)


    canvas.coords(images_id, event.x, event.y)

window.bind('<B1-Motion>', move)
window.mainloop()





