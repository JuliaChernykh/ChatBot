import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import database

flag = 0  # если ожидается ответ на задачу, то зажигается флаг
token = "caa664b4ef024a1ec8c4d9aa7755bccd8fb87a37c71cdf34cd89bf821dac847358c7b2918c9b8b8af14ba"
vk_session = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        message = event.text.lower()
        if message == 'привет' and flag == 0:  # поздоровались
            if event.from_user:
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=event.random_id,
                    message='Привет!'
                )
        elif message.split()[0] == "задание" and flag == 0:  # если пользоватиель запросил задание, то отправляем запрос в database
            if event.from_user:
                number = int(message.split()[1])
                answer = database.random_exc(number)
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=event.random_id,
                    message=answer[0]
                )
                flag = 1

        elif flag == 0:   # Если ползователь отправил что-то левое и флаг опущен, то пишем, что мы ничего не понимаем
            if event.from_user:
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=event.random_id,
                    message='Дружочек, я тебя не понимаю :('
                )
        elif flag == 1 and message.lower() == answer[1].lower():   # Если флаг поднят и ответ правильный, пишем, что все хорошо и опускаем флаг
            if event.from_user:
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=event.random_id,
                    message='Пральна!'
                )
            flag = 0
        elif flag == 1 and message.lower() == 'скажи ответ': # если флаг поднят и пользователь просит ответ, выполняем его просьюу
            if event.from_user:
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=event.random_id,
                    message=answer[1] + ', дурачок'
                )
            flag = 0
        elif flag == 1 and message.lower() != answer[1].lower(): # если флаг поднят и ответ неверный, оставляем флаг и просим ответить еще раз
            if event.from_user:
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=event.random_id,
                    message='Ну уж нет! Попробуй еще раз, дружочек.'
                )


