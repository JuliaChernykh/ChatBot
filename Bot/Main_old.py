import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import database


flag = []  # добавляем id пользователей в флаг, чтобы потом проверять их наличие и использовать это как флаг
token = "caa664b4ef024a1ec8c4d9aa7755bccd8fb87a37c71cdf34cd89bf821dac847358c7b2918c9b8b8af14ba"
vk_session = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        message = event.text.lower()
        if message == 'привет' and event.user_id not in flag:  # поздоровались
            if event.from_user:
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=event.random_id,
                    message='Привет!',
                    keyboard=keyboard
                )
        elif len(message.split()) == 2 and message.split()[0] == "задание" and event.user_id not in flag:  # если пользоватиель запросил задание, то отправляем запрос в database
            if event.from_user:
                number = int(message.split()[1])
                answer = database.random_exc(number)
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=event.random_id,
                    message=answer[0],
                    # keyboard=open("keyboards/default.json", "r", encoding="UTF-8").read()
                )
                flag.append(event.user_id)

        elif event.user_id not in flag:   # Если ползователь отправил что-то левое и флаг опущен, то пишем, что мы ничего не понимаем
            if event.from_user:
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=event.random_id,
                    message='Дружочек, я тебя не понимаю :('
                )
        elif event.user_id in flag and message.lower() == answer[1].lower():   # Если флаг поднят и ответ правильный, пишем, что все хорошо и опускаем флаг
            if event.from_user:
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=event.random_id,
                    message='Пральна!'
                )
            del flag[flag.index(event.user_id)]
        elif event.user_id in flag and message.lower() == 'скажи ответ': # если флаг поднят и пользователь просит ответ, выполняем его просьюу
            if event.from_user:
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=event.random_id,
                    message=answer[1] + ', дурачок'
                )
            del flag[flag.index(event.user_id)]
        elif event.user_id in flag and message.lower() != answer[1].lower(): # если флаг поднят и ответ неверный, оставляем флаг и просим ответить еще раз
            if event.from_user:
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=event.random_id,
                    message='Ну уж нет! Попробуй еще раз, дружочек.'
                )


