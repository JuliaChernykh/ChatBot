import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import database

token = "caa664b4ef024a1ec8c4d9aa7755bccd8fb87a37c71cdf34cd89bf821dac847358c7b2918c9b8b8af14ba"
vk_session = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        if event.text.lower() == 'привет':
            if event.from_user:
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=event.random_id,
                    message='Привет!'
                )
        elif event.text.lower() == "задание 1":
            if event.from_user:
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=event.random_id,
                    message=str(database.random_exc(1))
                )

        else:
            if event.from_user:
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=event.random_id,
                    message='Дружочек, я тебя не понимаю :('
                )

