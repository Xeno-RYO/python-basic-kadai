# -*- coding: utf-8 -*-
"""kadai_013

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gaK57vTzlpJ4Dgd_gjfNesZUdhu5qq07
"""

def add_two_arguments(price,consumption_tax):

 total = price + price*consumption_tax

 print(f"{total}円")

add_two_arguments(1200 , 0.1)