#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    HH, MM, SEC = s.split(':')
    s = SEC[:2]
    day = SEC[2:]
    if day == 'PM':
        HH = str(int(HH)+12)
        if int(HH) >= 24:
            HH = str(int(HH)-12)
    if day == 'AM' and HH == '12':
        HH = '00'
    return '{}:{}:{}'.format(HH,MM,s)

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
