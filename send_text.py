#!/usr/bin/env python
#coding: utf-8

import requests

def send_text2kde(data, lang="text"):
    '''
    将文本发送至paste.kde.org

    成功则返回在线地址, 否则返回"err"
    '''

    payload = {"api_submit" : "true", "mode" : "json"}
    payload["paste_data"] = data
    payload["paste_lang"] = lang
    url = "http://paste.kde.org/"

    try:
         req = requests.post(url, payload)
    except Exception as err:
         return "err"

    req_dict = req.json()

    if req_dict["result"].has_key("error"):
       return "err"
    elif req_dict["result"].has_key("id"):
       return "http://paste.kde.org/"+req_dict["result"]["id"]
    else:
       return "err"
