import plyer.platforms.win.notification
from plyer import notification
import requests

while True:
    response = requests.get("http://api.quotable.io/random").json()
    notification.notify(response['author'],response['content'],'qouter','icon.ico',timeout=10)