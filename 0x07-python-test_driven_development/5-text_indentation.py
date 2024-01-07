#!/usr/bin/python3
"""module"""


def text_indentation(text):
    """module"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for del in ".?:":
        # print(del, text.split(del))
        text = (del + "\n\n").join(
            [line.strip(" ") for line in text.split(del)])

    print(text, end="")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")

