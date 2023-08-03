import requests

from bot.tg.dc import GetUpdatesResponse, GetUpdatesResponseSchema, SendMessageResponse, SendMessageResponseSchema


class TgClient:
    def __init__(self, token):
        self.token = token

    def get_url(self, method: str):
        return f"https://api.telegram.org/bot{self.token}/{method}"

    def get_data(self, method: str, **params):
        data = requests.get(f"https://api.telegram.org/bot{self.token}/{method}", params=params)
        return data.json()

    def get_updates(self, offset: int = 0, timeout: int = 60) -> GetUpdatesResponse:
        data = self.get_data("getUpdates", offset=offset, timeout=timeout)
        return GetUpdatesResponseSchema().load(data)

    def send_message(self, chat_id: int, text: str) -> SendMessageResponse:
        data = self.get_data("sendMessage", chat_id=chat_id, text=text)
        return SendMessageResponseSchema().load(data)


offset = 0
tg_client = TgClient("6639076130:AAEbibrXbRh62knEhhooeRdoYvbYyVyCT2E")
while True:
    res = tg_client.get_updates(offset=offset)
    for item in res.result:
        offset = item.update_id + 1
        print(item.message)