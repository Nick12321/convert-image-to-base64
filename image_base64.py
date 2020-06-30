# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import base64
with open("cat_1.jpeg", "rb") as image_file:
   encoded_string = base64.b64encode(image_file.read())
print(encoded_string)
