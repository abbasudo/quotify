from win10toast import ToastNotifier
import requests

toast = ToastNotifier()

while True:
    response = requests.get("http://api.quotable.io/random").json()
    toast.show_toast(response['author'],response['content'], duration=60)