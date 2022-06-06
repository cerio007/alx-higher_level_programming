#!/usr/bin/python3
def multiple_returns(sentence):
    len_str = len(sentence)

    if (len_str == 0):
        new_tuple = (len_str, None)
    else:
        new_tuple = (len_str, sentence[0])

    return (new_tuple)
