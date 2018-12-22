import requests
import json

# web connectors
url = "https://api.telegram.org/bot<ваш_токен>/"


def get_updates_json(request):
    response = requests.get(request + 'getUpdates')
    return response.json()


def last_update(data):
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]


# local connectors

def get():
    f = open("/home/alex/PycharmProjects/catilina/tests/test1", "r")
    data = json.loads(f.read())
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]
