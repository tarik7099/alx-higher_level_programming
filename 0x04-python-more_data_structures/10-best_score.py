#!/usr/bin/python3
def best_score(a_dictionary):
    list1 = []
    list2 = []
    if not a_dictionary:
        return None
    else:
        for key, value in a_dictionary.items():
            list1.append(value)
            list2.append(key)
            for j in range(len(list1)):
                for i in range(len(list1) - 1):
                    if list1[j] > list1[i + 1]:
                        key = list2[j]
        return key
