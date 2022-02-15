import requests
from .models import TeleSettings

def sendTelegram(tg_name, tg_phone, tg_coming_date):
    if TeleSettings.objects.get(pk=1):
        settings = TeleSettings.objects.get(pk=1)
        token = str(settings.tg_token)
        chat_id = str(settings.tg_chat)
        text = str(settings.tg_message)
        api = 'https://api.telegram.org/bot'
        method = api + token + "/sendMessage"
        if text.find('{') and text.find('}') and text.rfind('{') and text.rfind('}'):
            a = text.find('{')
            b = text.find('}')
            text2 = text[a + 1:]
            c = text2.find('{') + a
            text2 = text2[c:]
            d = text2.find('}') + c
            e = text.rfind('{')
            f = text.rfind('}')

            part_1 = text[0:a]
            part_2 = text[b + 1:c]
            part_3 = text[d + 1:e]
            part_4 = text[f:-1]
            text_slice = part_1 + tg_name + part_2 + tg_phone + part_3 + tg_coming_date + part_4


        else:
            text_slice=text



        try:
            req = requests.post(method, data={'chat_id': chat_id,
                                         'text': text_slice})
        except:
            pass
        finally:
            if req.status_code != 200:
                print("Ошибка отправки!")
            elif req.status_code == 500:
                print('Ошибка 500')
            else:
                print('Всё ОК, сообщение отправлено!')


    else:
        pass