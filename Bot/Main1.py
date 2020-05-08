import vk_api
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll
import json
import database

available_nums = ['1', '2', '5', '6', '9', '11', '13', '16', '19']  # доступные номера заданий
answer = {} # в словарь записывается пара (пользователь, отвечающий на задачу) - (ответ на задачу)
flag = []  # флаг на ожидание ответа
flag1 = []  # флаг на ожидание номера задания
token = "caa664b4ef024a1ec8c4d9aa7755bccd8fb87a37c71cdf34cd89bf821dac847358c7b2918c9b8b8af14ba"
vk = vk_api.VkApi(token=token)

vk._auth_token()

vk.get_api()

keyboard = {
    "one_time": False,
    "buttons": [
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"1\"}",
                "label": "Получить задачу"
            },
            "color": "primary"
        },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "Получить ответ"
                },
                "color": "primary"
            # },
            # {
            #     "action": {
            #         "type": "text",
            #         "payload": "{\"button\": \"2\"}",
            #         "label": "Primary"
            #     },
            #     "color": "primary"
            # },
            # {
            #     "action": {
            #         "type": "text",
            #         "payload": "{\"button\": \"2\"}",
            #         "label": "Secondary"
            #     },
            #     "color": "secondary"
            }
        ]
    ]
}

keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
keyboard = str(keyboard.decode('utf-8'))

longpoll = VkBotLongPoll(vk, 192652184)

while True:
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            if event.object.text.lower() == "привет":
                vk.method("messages.send", {"peer_id": event.object.peer_id, "message": "Приветики!", "random_id": 0,
                                            "keyboard": keyboard})
            elif event.object.text.lower() == "получить задачу":
                vk.method("messages.send", {"peer_id": event.object.peer_id, "message": "Какую?", "random_id": 0,
                                            "keyboard": keyboard})
                flag1.append(event.object.peer_id)
            elif event.object.peer_id in flag1 and event.object.text in available_nums:
                number = int(event.object.text)
                answer[event.object.peer_id] = database.random_exc(number)
                vk.method("messages.send", {"peer_id": event.object.peer_id, "message": answer[event.object.peer_id][0], "random_id": 0,
                                            "keyboard": keyboard})
                del flag1[flag1.index(event.object.peer_id)]
            elif event.object.peer_id in flag1 and event.object.text not in available_nums:
                vk.method("messages.send", {"peer_id": event.object.peer_id, "message": 'Данного задания нет в базе', "random_id": 0,
                                            "keyboard": keyboard})
            elif event.object.peer_id in answer.keys() and event.object.text.lower() == answer[event.object.peer_id][1].lower():
                vk.method("messages.send", {"peer_id": event.object.peer_id, "message": "Верно!", "random_id": 0,
                                            "keyboard": keyboard})
                answer.pop(event.object.peer_id)
            elif event.object.peer_id in answer.keys() and event.object.text.lower() == 'получить ответ':
                vk.method("messages.send",
                          {"peer_id": event.object.peer_id, "message": answer.pop(event.object.peer_id)[1], "random_id": 0,
                           "keyboard": keyboard})
            elif event.object.peer_id in answer.keys() and event.object.text.lower() != answer[event.object.peer_id][1].lower():
                vk.method("messages.send",
                          {"peer_id": event.object.peer_id, "message": 'Неверный ответ',
                           "random_id": 0,
                           "keyboard": keyboard})
            # elif "Negative" in event.object.text:
            #     vk.method("messages.send", {"peer_id": event.object.peer_id, "message": "Красная кнопка", "random_id": 0
            #                                 })
            else:
                vk.method("messages.send", {"peer_id": event.object.peer_id, "message": "Это что значитб?", "random_id": 0,
                                            "keyboard": keyboard})