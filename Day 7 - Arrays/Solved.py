import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    reverse = arr[::-1]

    for i in reverse:
        print(i, end=" ")
