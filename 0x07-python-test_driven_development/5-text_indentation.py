#!/usr/bin/python3
"""module"""


def text_indentation(text):
    """module"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delm in ".?:":
        # print(delm, text.split(delm))
        text = (delm + "\n\n").join(
            [line.strip(" ") for line in text.split(delm)])

    print(text, end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
