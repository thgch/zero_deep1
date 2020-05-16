"""
ch1.py

Auther: thgch
Created on 2020/05/17

"""


class Man:
    def __init__(self, name):
        self.name = name
        print("Initialized!")

    def hello(self):
        print("Hello {}!".format(self.name))

    def goodbye(self):
        print("Good-bye {}!".format(self.name))


if __name__ == '__main__':
    pass