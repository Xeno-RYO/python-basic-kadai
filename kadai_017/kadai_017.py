# -*- coding: utf-8 -*-
"""kadai_017

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1X0AhZD04ud5nuMIZ4ttgkq2f7ympWqX_
"""

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def check_adult(self):
        if self.age >= 20:
            print(f"{self.name}は大人です。")
        else:
            print(f"{self.name}は大人ではありません。")

humans = []
humans.append(Human("太郎", 25))
humans.append(Human("花子", 18))
humans.append(Human("一郎", 30))

for human in humans:
    human.check_adult()