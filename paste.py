#!/usr/bin/env python
#coding: utf-8

import send_text, send_image
import pyperclip

def paste2cloud():
    clipboard = pyperclip.paste()

    type = {"png" : "image",
            "jpeg" : "image",
            "jpg": "image",
            "gif": "image",
            "py": "python",
            "html": "html"}

    if clipboard.startswith("file://"):
        unicode_path = unicode(clipboard[7:], "utf-8")
        file_type = type.get(unicode_path.split(".")[-1], "text")

        if file_type == "image":
           url = send_image.send_image2wstaw(unicode_path)
        else:
            file_content = open(unicode_path, "r").read()
            url = send_text.send_text2kde(file_content, file_type)
    else:
        url = send_text.send_text2kde(clipboard)

    if url != "err":
        pyperclip.copy(url)
