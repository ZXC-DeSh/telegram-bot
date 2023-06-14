# import os 
# from gtts import gTTS
# from pygame import mixer

# f = open('text.txt', 'r', encoding = 'UTF-8')
# text = f.read()
# print(text)                                
# f.close()

# mixer.init()

# tts = gTTs(text = text, lang='ru')
# tts.save('voie.mp3')

# mixer.music.load('voie.mp3')
# mixer.music.play(1,1)
# mixer.music.set_volume(0.6)





# import os 
# from gtts import gTTS
# from pygame import mixer
# import random
# import pyaudio 
# import speech_recognition as sr 

# r = sr.Recognizer()

# while True:
#     with sr.Microphone() as sourse:
#         print('Скажи слово')
#         audio = r.listen(sourse)
#     speech = r.recognize_google(audio, language='ru_RU').lower()
#     print('Вы сказали ',speech)
#     if speech == 'привет':
#         x = ['привет','здарова','хай','доброе утро']
#         print(random.choice(x))
#         break









# import os 
# from gtts import gTTS
# from pygame import mixer
# import random
# import pyaudio 
# import speech_recognition as sr 

# r = sr.Recognizer()

# while True:
#     with sr.Microphone() as sourse:
#         print('Скажи слово')
#         audio = r.listen(sourse)
#     speech = r.recognize_google(audio, language='ru_RU').lower()
#     print('Вы сказали ',speech)
#     if speech == 'фильм':
#         x = ['Зеленая миля','Список Шиндлера','Тайна Коко','Властелин колец: Возвращение короля']
#         print('Советую посмотреть: ', random.choice(x))
#         break