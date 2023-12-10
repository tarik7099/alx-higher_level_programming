def roman_to_int(roman_string):
    numeral = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100 , "D": 500, "M": 1000}

    if not roman_string or roman_string is None:
        return 0
    number = 0
    i  = len(roman_string)
    for new_roman in roman_string:
        if new_roman in numeral:
            if i <= 1:
                return numeral[new_roman]
            for inside_roman in roman_string:
                if numeral[new_roman] < numeral[inside_roman]:
                    number -= numeral[inside_roman]
                    number = abs(number)
                else:
                    number += numeral[inside_roman]

            return number


