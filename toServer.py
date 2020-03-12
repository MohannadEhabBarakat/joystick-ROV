import requests


def send(PARAMS, subPath="joystick"):
    r = requests.get(url = "192.168.1.2:5000/"+subPath, params = PARAMS)