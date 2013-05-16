#!/usr/bin/env python
#coding: utf-8

from bs4 import BeautifulSoup
import requests

def send_image2wstaw(path):
    '''
    发送图片到WSTAWKA

    发送成功则返回URL, 否则返回"err"
    '''
    url = "http://wstaw.org/"
    image = {"pic" : open(path, "rb")}

    try:
        req = requests.post(url, files=image)
    except Exception as err:
        return "err"

    try:
        url = BeautifulSoup(req.text).input["value"]
    except Exception as err:
        return "err"

    return url
