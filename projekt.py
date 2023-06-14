
# from fpdf import FPDF
# from datetime import datetime

# pdf = FPDF('p', 'mm', 'A4', )
# pdf.add_page()

# pdf.add_font('comic',"",'C:\WINDOWS\FONTS\COMIC.ttf', uni=True)
# pdf.set_font('comic', size=37)

# pdf.image('bg.jpg',h=297,w=210,x=0,y=0 )

# pdf.set_text_color(224,4,64)

# name_br = input('Введите имя именинника: \n')

# pdf.cell(0,95, ln=1)
# pdf.cell(0,20,txt='Дорогой, '+name_br+' !', align='C', ln=1)

# pdf.set_right_margin(50)
# pdf.set_left_margin(50)

# message = input('Введите поздравление с днём рождения: \n')
# pdf.set_font('comic', size=27)
# pdf.multi_cell(0,20,txt=message,align='C')

# time = datetime.today().strftime('%d.%m.%Y')

# pdf.set_text_color(224,4,64)
# pdf.cell(0,10,txt=time, align="R",ln=1)
# pdf.set_font('comic', size=27)

# pdf.set_right_margin(50)
# pdf.set_left_margin(50)

# my_name = input('Введите ваше имя: \n ')
# pdf.set_text_color(224,4,64)
# pdf.cell(0,10,txt=my_name, align="R",ln=1)

# pdf.output('br.pdf')








# from tkinter import *

# window = Tk()
# window.geometry('1300x1000')

# def draw_menu():
#     clear()
#     draw_home()
#     label_t = Label(text='Выберите',font=('Arial',24),fg='gold',bg='green')
#     label_t.place(width=1300,height=50,x=0,y=0)
    
#     b1 = Button(text='Открыть таблицу умножения',font=('Arial',24),fg='gold',bg='purple', command=maths)
#     b1.place(x=40,y=75,width=500)
    
#     b2 = Button(text="DON'T CLICK ME",font=('Arial',24),fg='gold',bg='purple', command=skream,)
#     b2.place(x=700,y=75,width=500)

# def skream():
#     clear()
#     img_scr = PhotoImage(file='skelet.gif')
#     img_lab_sc = Label(image=img_scr)
#     img_lab_sc.image = img_scr
#     img_lab_sc.place(x=300, y=250,)

# def maths():
#     clear()
#     img_scr = PhotoImage(file='table.png')
#     img_lab_sc = Label(image=img_scr)
#     img_lab_sc.image = img_scr
#     img_lab_sc.place(x=225, y=100,)

# def clear():
#     all_wd = window.place_slaves()
#     for i in all_wd:
#         i.destroy()
#     draw_home()

# def draw_home():
#     but_home = Button(text="Домой",font=('Arial',24),fg='white',bg='red', command=draw_menu)
#     but_home.place(x=25,y=800,width=1300)


# draw_menu()



# window.mainloop()
























from tkinter import *
import time
import random

window = Tk()

window.title("Ping-Pong")
window.geometry("500x400")
window.resizable(False,False) #не могу изменять размер

window.wm_attributes("-topmost",1) # поверх других окон

canvas = Canvas(window, width = 500, height = 400 )
canvas.pack()

class Ball:
    def __init__(self,canvas,platform,score,color) -> None:
        self.canvas = canvas
        self.platform = platform
        self.score = score
        self.oval = canvas.create_oval(200,200,215,215,fill = color)
        self.x = random.choice([-3,-2,-1,1,2,3]) #выбираю рандомную скорость по x
        self.y = -1 
        self.lvl = None
        self.touch = False # коснулся ли низа
        self.speed()#обьявляем скорость

    def speed(self):
        #положительная и отрицательная скорость по x и y
        self.plus_x = 3
        self.plus_y = 3
        self.minus_x = -3
        self.minus_y = -3


    def touch_platform(self):
        ball_pos = self.canvas.coords(self.oval)
        platform_pos = self.canvas.coords(self.platform.rect)
        #проверка слева и справа по x
        if ball_pos[2] >= platform_pos[0] and ball_pos[0] <= platform_pos[2]:
            #проверка по y
            if ball_pos[3] >= platform_pos[1] and ball_pos[3] <= platform_pos[3]:
                self.score.hit() #увеличиваю счет
                #увеличиваю лвл каждые 10 очков
                if self.score.score % 3 == 0 and self.score.score != 0:
                    self.lvl.lvl_up()
                return 1
        return False



    def draw(self):
        self.canvas.move(self.oval,self.x,self.y)
        pos = self.canvas.coords(self.oval)
        if pos[1] <= 0:
            self.y = self.plus_y
        if pos[3] >= 400: #если коснулся низа
            self.touch = True
        if pos[0] <= 0:
            self.x = self.plus_x
        if pos[2] >= 500:
            self.x = self.minus_x
        if self.touch_platform() == 1: # если мяч коснулся платформы
            self.y = self.minus_y



class Platform:
    def __init__(self,canvas,color) -> None:
        self.canvas = canvas
        self.rect = canvas.create_rectangle(230,300,330,310, fill = color)
        self.x = 0
        self.speed()
        self.canvas.bind_all("<KeyPress-Left>", self.left)
        self.canvas.bind_all("<KeyPress-Right>", self.right)

    def left(self,event):
        self.x = self.minus_x

    def right(self,event):
        self.x = self.plus_x

    def speed(self):
        #положительная и отрицательная скорость по x 
        self.plus_x = 3
        self.minus_x = -3


    def draw(self):
        #движение спрайта по x и y
        self.canvas.move(self.rect,self.x,0)
        pos = self.canvas.coords(self.rect)
        if pos[0] <= 0:#если заходим за левую сторону
            self.x = 0
        if pos[2] >= 500:
            self.x = 0

class Score:
    def __init__(self,canvas,color) -> None:
        self.canvas = canvas
        self.score = 0 
        self.score_text = canvas.create_text(410,10,text = f"score: {self.score}",font =("Ariel",15) , fill = color)

    def hit(self):
        self.score += 1
        self.canvas.itemconfig(self.score_text, text = f"score: {self.score}")#обновляю счет


class Level:
    def __init__(self,canvas,color,platform,ball) -> None:
        self.canvas = canvas
        self.platform = platform
        self.ball = ball
        self.lvl = 0 
        self.lvl_text = canvas.create_text(50,10,text = f"lvl: {self.lvl}",font =("Ariel",15) , fill = color)

    def lvl_up(self):
        self.lvl += 1
        self.canvas.itemconfig(self.lvl_text, text = f"lvl: {self.lvl}")#обновляю уровень
        #изменяю скорость платформы и мяча
        self.ball.plus_x += 1
        self.ball.plus_y += 1
        self.ball.minus_x += -1
        self.ball.minus_y += -1

        self.platform.minus_x += -1
        self.platform.plus_x += 1

platform = Platform(canvas, "purple")
game_score = Score(canvas, "black")
ball = Ball(canvas, platform, game_score, "red")
lvl = Level(canvas,"black",platform,ball)

ball.lvl = lvl

while True:
    if ball.touch == False:
        platform.draw()
        ball.draw()
    else : #когда проиграли
        break
    window.update()
    time.sleep(0.01)