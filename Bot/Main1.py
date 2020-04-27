import vk_api
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll
import json
import database

flag = []  # добавляем id пользователей в флаг, чтобы потом проверять их наличие и использовать это как флаг
flag1 = []
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
                "label": "Дай-ка задачку, неудачник"
            },
            "color": "primary"
        },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "Скажи ответ, нахал"
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
            elif event.object.text.lower() == "дай-ка задачку, неудачник":
                vk.method("messages.send", {"peer_id": event.object.peer_id, "message": "Какую?", "random_id": 0,
                                            "keyboard": keyboard})
                flag1.append(event.object.peer_id)
            elif event.object.peer_id in flag1:
                number = int(event.object.text)
                answer = database.random_exc(number)
                vk.method("messages.send", {"peer_id": event.object.peer_id, "message": answer[0], "random_id": 0,
                                            "keyboard": keyboard})
                del flag1[flag1.index(event.object.peer_id)]
                flag.append(event.object.peer_id)
            elif event.object.peer_id in flag and event.object.text.lower() == answer[1].lower():
                vk.method("messages.send", {"peer_id": event.object.peer_id, "message": "А ты мне нравишься!", "random_id": 0,
                                            "keyboard": keyboard})
                del flag[flag.index(event.object.peer_id)]
            elif event.object.peer_id in flag and event.object.text.lower() == 'скажи ответ, нахал':
                vk.method("messages.send",
                          {"peer_id": event.object.peer_id, "message": answer[1] + ', дурачок', "random_id": 0,
                           "keyboard": keyboard})
                del flag[flag.index(event.object.peer_id)]
            elif event.object.peer_id in flag and event.object.text.lower() != answer[1].lower():
                vk.method("messages.send",
                          {"peer_id": event.object.peer_id, "message": 'Ха, лох',
                           "random_id": 0,
                           "keyboard": keyboard})
            # elif "Negative" in event.object.text:
            #     vk.method("messages.send", {"peer_id": event.object.peer_id, "message": "Красная кнопка", "random_id": 0
            #                                 })
            else:
                vk.method("messages.send", {"peer_id": event.object.peer_id, "message": "Это что значитб?", "random_id": 0,
                                            "keyboard": keyboard})