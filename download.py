#!/usr/bin/env python

import requests


def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)


download("https://i.pinimg.com/originals/74/00/59/740059b3391d584475ee0b947240e9c9.jpg")
