#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if not sentence:
        first = None
    else:
        first = sentence[0]
    return length, first

#multiple_returns = __import__('8-multiple_returns').multiple_returns

#sentence = "At school, I learnt C!"
sentence = ""
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))