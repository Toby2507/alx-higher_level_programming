#!/usr/bin/python3
"""
module contains a function that prints a text with 2 new lines
after each of these characters: ., ? and :
"""


def text_indentation(text):
    """prints the text with indentation

    Args:
        text: text to be printed
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    text = text.strip(" ")
    if not text:
        return
    newString = [c if c not in ['.', '?', ':'] else f'{c}\n\n' for c in text]
    for i in range(len(newString)):
        if newString[i].endswith('\n'):
            for j in range(i - 1, -1, -1):
                if newString[j] != " ":
                    break
                newString[j] = ''
            for j in range(i + 1, len(newString)):
                if newString[j] != " ":
                    break
                newString[j] = ''
    print(''.join(newString), end='')
