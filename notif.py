import os
import sys
import requests
from time import sleep
from PIL import Image
from pystray import Icon as icon, Menu as menu, MenuItem as item


def create_image():
    return Image.open(resource_path("icon.ico"))

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def motivate(icon):
    response = requests.get("http://api.quotable.io/random").json()
    icon.notify(response['content'],response['author'])

exit = False

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

while not exit:
    motivate(icon)
    # every 20 minutes
    sleep(60 * 20)
