#!/usr/bin/python3
"""task module"""


class Student:
    """student"""
    def __init__(self, first_name, last_name, age):
        """initlize"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """json"""
        try:
            for att in attrs:
                if type(att) is not str:
                    return self.__dict__

        except Exception:
            return self.__dict__
        dictt = dict()
        for k, val in self.__dict__.items():
            if k in attrs:
                dictt[k] = val
        return dictt
