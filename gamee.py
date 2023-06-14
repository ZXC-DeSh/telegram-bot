from tkinter import *
import random

#окно
window = Tk()

#высота и ширина
W = 600
H = 600

window.geometry(f"{W}x{H}")


 
#холст
canvas = Canvas(window,width = W, height = H)
canvas.place(in_ = window ,x = 0, y = 0 )

#записал картинку 
# bg_photo = PhotoImage(file = r"C:\Users\User\Desktop\OOP\bg_2.png")
bg_photo = PhotoImage(file = "bg_2.png")


class Knight:

    #метод инициализатор
    def __init__(self) :
        #свойства класса
        #положение рыцаря 
        self.x = 70
        self.y = H//2

        #скорость
        self.v = 0

        self.v_x = 0

        #изображение
        self.photo = PhotoImage(file = "knight.png")


    #метод вверх
    def up(self,event):
        self.v = -3

    #метод вниз
    def down(self,event):
        self.v = 3

    #метод стоп
    def stop(self,event):
        self.v = 0
        self.v_x = 0

    def right(self, event):
        self.v_x = +3

    def left(self, event):
        self.v_x = -3


class Dragon:
    #метод инициализатор
    def __init__(self) :
        #свойства дракона
        #положение рыцаря 
        self.x = random.randint(750,1500)
        self.y = random.randint(100,500)

        #скорость
        self.v = random.randint(1,3)

        #изображение
        self.photo = PhotoImage(file = "dragon.png")
        


#экземпляр класса
knight = Knight()


#список где хранятся драконы
dragons = []
for i in range(10):
    #добавляю дракона в список
    dragons.append(Dragon())



def game():
    #удаляю все рисунки
    canvas.delete("all")
    canvas.create_image(300,300, image = bg_photo )
    canvas.create_image( knight.x  , knight.y  , image = knight.photo )

    #ДВИЖЕНИЕ РЫЦАРЯ
    knight.y += knight.v
    knight.x += knight.v_x

    #счетчик индекса дракона
    cur_dragon = 0
    dragon_ind = -1

    


    for dragon in dragons:
        dragon.v = -dragon.v
        dragon.x += dragon.v - 1
        canvas.create_image(dragon.x, dragon.y, image = dragon.photo)

        if ((dragon.x - knight.x)**2) + ((dragon.y - knight.y)**2) <= 96**2:
            dragon_ind = cur_dragon


        cur_dragon += 1

        #ЕСЛИ ПРОПУСТИЛИ ДРАКОНА
        if dragon.x<=0:
            canvas.delete("all")
            #текст
            canvas.create_text(W//2, H//2, text = "LOSE", font = "Verdana 42", fill = "red")


        #удаляю дракона
        if dragon_ind >= 0:
            del dragons[dragon_ind]
    
    if knight.y <= 70:
        knight.y = 69
    if knight.y >= 600:
        knight.y = 530
    if knight.x <= 70:
        knight.x = 71
    if knight.x >= 600:
        knight.x = 530
    
    window.after(5,game )

        


game()
#привязал кнопки
window.bind('<Key-Up>', knight.up)
window.bind('<Key-Down>', knight.down)
window.bind('<Key-Right>', knight.right)
window.bind('<Key-Left>', knight.left)
window.bind('<KeyRelease>', knight.stop)



window.resizable(height=False, width=False)
window.mainloop()





