# import vk_api  #vk1.a.Q_SpTNLG-UbReqa6Np6FOembrnIe0-qch4QaDx3szwGUAawgDOblk7Ey5yjO7mvraUO7BNNS8cEP-kXqGx7t7hk7XD3dCOP_glrxlZ7qNe1UJcPPI5S8NMcD13rhnEBT2R1fmlzhZ6mHGb2adSTF9YjGhHJqV-PcG-jfoIae0C39yZmqcewu7VRc65m_dgCVBEOUbizp10Y5Ai3BIOqczQ
# import course
# import check_planet_diametr
# import starship

# TOKEN = 'vk1.a.Q_SpTNLG-UbReqa6Np6FOembrnIe0-qch4QaDx3szwGUAawgDOblk7Ey5yjO7mvraUO7BNNS8cEP-kXqGx7t7hk7XD3dCOP_glrxlZ7qNe1UJcPPI5S8NMcD13rhnEBT2R1fmlzhZ6mHGb2adSTF9YjGhHJqV-PcG-jfoIae0C39yZmqcewu7VRc65m_dgCVBEOUbizp10Y5Ai3BIOqczQ'
# vk = vk_api.VkApi(token=token)
# vk._auth_token()

# while True:
#     messages = vk.method('messages.getConversations', {'count': 20, 'filter': 'unanswered'})
#     if messages['count'] >= 1:
#         user_id = messages['items'][0]['last_message']['from_id']
#         message_id = messages['items'][0]['last_message']['id']
#         message_text = messages['items'][0]['last_message']['text']  # текст сообщения от пользователя
#         if message_text.lower() == 'курс доллара':
#             vk.method('messages.send', {'peer_id': user_id, 'random_id': message_id, 
#                                         'message': f'Курс доллара: {course.get_course("R01235")}'})
#         else:
#             vk.method('messages.send', {'peer_id': user_id, 'random_id': message_id, 'message': 'неизвестная команда'})

#         if message_text.lower() == 'Диаметр планеты':
#             vk.method('messages.send', {'peer_id': user_id, 'random_id': message_id, 
#                                         'message': f'Планета с максимальным диаметром: {check_planet_diametr.check_planet()}'})
#         else:
#             vk.method('messages.send', {'peer_id': user_id, 'random_id': message_id, 'message': 'неизвестная команда'})

#         if message_text.lower() == 'корабли':
#             vk.method('messages.send', {'peer_id': user_id, 'random_id': message_id, 
#                                         'message': f'Звёздный корабль с максимальной скоростью: {starship.check_starships()}'})
#         else:
#             vk.method('messages.send', {'peer_id': user_id, 'random_id': message_id, 'message': 'неизвестная команда'})


















import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from course import get_course
import random
from wiki import get_wiki_artile

TOKEN = 'vk1.a.Q_SpTNLG-UbReqa6Np6FOembrnIe0-qch4QaDx3szwGUAawgDOblk7Ey5yjO7mvraUO7BNNS8cEP-kXqGx7t7hk7XD3dCOP_glrxlZ7qNe1UJcPPI5S8NMcD13rhnEBT2R1fmlzhZ6mHGb2adSTF9YjGhHJqV-PcG-jfoIae0C39yZmqcewu7VRc65m_dgCVBEOUbizp10Y5Ai3BIOqczQ'
vk_session = vk_api.VkApi(token=TOKEN)
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        message = event.text.lower()
        user_id = event.user_id

        random_id = random.randint(1,10**10)
        if message == '-к usd':
            response = f'{get_course("R01235")} рублейй за 1 доллар'
        elif message == '-к eur':
            response = f'{get_course("R01239")} рублейй за 1 евро'
        elif message.startswith('-в'):
            response = get_wiki_artile(message[2:])
        else:
            response = 'Неизвестная команда'

        vk.messages.send(user_id=user_id,random_id=random_id,message=response)








        













