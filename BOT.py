import telebot 
import random
from telebot import types
TOKEN = '5651190184:AAHA3j5Mb5_moQqets5pGo92UBhw9BU_KG4'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['poem'])

def poem(msg):
    text = "Я помню чудное мгновенье: Передо мной явилась ты, Как мимолетное виденье, Как гений чистой красоты."
    bot.send_message(msg.from_user.id, text)

    # Keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)
    # but_1 = telebot.types.InlineKeyboardButton('/poem')
    # Keyboard.add(but_1)

@bot.message_handler(commands=['img'])

def img(msg):
    image = open('bg.jpg','rb')
    bot.send_photo(msg.from_user.id, image)

@bot.message_handler(['music'])

def mus(msg):
    mp3 = open('_____.mp3','rb')
    bot.send_photo(msg.from_user.id, mp3)

@bot.message_handler(commands=['start'])

def start(msg):
    welcome = 'Привет, отправь мне команду'
    Keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, row_width=2)
    but_1 = telebot.types.KeyboardButton('music')
    but_2 = telebot.types.KeyboardButton('poem')
    but_3 = telebot.types.KeyboardButton('img')
    but_5 = telebot.types.KeyboardButton('emoji')
    but_7 = telebot.types.KeyboardButton('game')
    but_8 = telebot.types.KeyboardButton('start')
    but_9 = telebot.types.KeyboardButton('janr')
    Keyboard.add(but_1,but_2,but_3,but_5,but_7,but_8,but_9)
    
    bot.send_message(msg.from_user.id, welcome, reply_markup=Keyboard)

@bot.message_handler(content_types=['text'])
def user_text(msg):
    if msg.text == 'poem':
        poem(msg)
    elif msg.text == 'img':
       img(msg) 
    elif msg.text == 'emoji':
        emoji(msg)
    elif msg.text == 'game':
        game(msg)
    elif msg.text == 'music':
        mus(msg)
    elif msg.text == 'start':
        start(msg)
    elif msg.text == 'janr':
        janr(msg)

@bot.message_handler(commands=['emoji'])
def emoji(msg):
    id_e = ''
    bot.send_sticker(msg.from_user.id, id_e)

@bot.message_handler(commands=['game'])
def game(msg):
    game = 'Minecraft - это инди-игра в жанре песочницы с элементами выживания и открытым миром. Геймплей в игре прост - игроки добывают ресурсы, чтобы строить дома, замки и целые города. Ограничений в Minecraft фактически нет, кроме высоты уровня - в остальном игроки вольны творить все, что пожелают.'
    bot.send_message(msg.from_user.id, game)

@bot.message_handler(commands=['janr'])
def janr(msg):
    markup_inline = types.InlineKeyboardMarkup()
    item_yes = types.InlineKeyboardButton(text = 'ДА', callback_data= 'yes')
    item_no = types.InlineKeyboardButton(text = 'НЕТ', callback_data= 'no')

    markup_inline.add(item_yes, item_no)
    bot.send_message(msg.from_user.id, 'Хотите узнать об игре вашего любимого жанра?', 
        reply_markup = markup_inline
    )

@bot.callback_query_handler(func = lambda call: True)
def answer(call):
    if call.data == 'yes':
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard= True)
        item_id1 = types.KeyboardButton('Жанр1')
        item_id2 = types.KeyboardButton('Жанр2')

        markup_reply.add(item_id1, item_id2)
        bot.send_message(call.massage.chat.id, 'Нажмите на одну из кнопок', 
            reply_markup= markup_reply
        )
    elif call.data == 'no':
        pass
            

@bot.message_handler(content_types=['text'])
def get_text(msg):
    if msg.text == 'Жанр1':
        bot.send_message(msg.from_user.id, 'game1')
    elif msg.text == 'Жанр2':
        bot.send_message(msg.from_user.id, 'game2')
        



















bot.polling()










































































# import time 

# def my_decor_time(func):
    
#     def next_level():
#         start = time.time()
#         func()
#         end = time.time()
#         result = end - start
#         print('Функция выполнилась за:', result)
#     return next_level

# @my_decor_time
# def my_func1():
#     for i in range(100):
#         print(i)

# @my_decor_time
# def my_func2():
#     for i in range(1000):
#         print(i)

# my_func1()
# my_func2()

