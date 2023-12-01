#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    len1 = len(sys.argv)
    if len1 - 1== 0: 
        print("{} arguments.".format(len1 - 1))
    else:
         print("{} arguments:".format(len1 - 1))
    for i in range(len1):
            i += + 1
            if i == len1:
                break

            print("{}: {}".format(i, sys.argv[i]))
