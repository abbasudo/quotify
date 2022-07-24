import requests
from time import sleep
from PIL import Image
from pystray import Icon as icon, Menu as menu, MenuItem as item


def create_image():
    return Image.open(".\icon.ico")

def motivate(icon):
    response = requests.get("http://api.quotable.io/random").json()
    icon.notify(response['content'],response['author'])

def close(icon):
    global exit
    exit = True
    icon.stop()

icon = icon(
            'quotinator',
            create_image(), 
            menu=menu(
                item('motivate', motivate), 
                item('close', close)
                )
        )

icon.run_detached()

while 1:
    motivate(icon)
    # every 20 minutes
    sleep(60 * 20)
