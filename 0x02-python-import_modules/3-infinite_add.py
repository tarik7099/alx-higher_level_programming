#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    len1 = len(sys.argv)
    number = 0

    for i in range(1 ,len1):
        for j in range(i+1, i +2):
            if i + 2 > len1:
                break
            if j >= 3:
                number = number + int(sys.argv[j])
            else:
                number +=    int(sys.argv[i]) + int(sys.argv[j] )
            
    print(number)
