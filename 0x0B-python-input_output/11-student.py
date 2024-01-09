#!/usr/bin/python3
"""dict"""


class Student:
    """student"""
    def __init__(self, first_name, last_name, age):
        """initilze"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """json"""
        try:
            for att in atts:
                if type(att) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        dictt = dict()
        for k, val in self.__dict__.items():
            if k in atts:
                dictt[k] = val
        return dictt

    def reload_from_json(self, json):
        """jsob:"""
        for k, val in json.items():
            if k in self.__dict__:
                self.__dict__[k] = val
