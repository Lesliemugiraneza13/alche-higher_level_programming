#!/usr/bin/python3
"""Module that defines a Student class with filtered to_json"""


class Student:
    """A class that defines a student with filtered JSON output"""

    def __init__(self, first_name, last_name, age):
        """Initializes a Student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns dictionary representation with optional attribute filter"""
        if isinstance(attrs, list):
            return {k: v for k, v in self.__dict__.items()
                    if k in attrs}
        return self.__dict__
