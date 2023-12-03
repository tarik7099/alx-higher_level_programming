#!/usr/bin/python3
def multiple_returns(sentence):
    length1 = len(sentence)
    first_char = sentence[0]
    return  length1 , first_char 
#multiple_returns = __import__('8-multiple_returns').multiple_returns

sentence = "At school, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))