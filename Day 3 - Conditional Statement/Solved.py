#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    N = int(input().strip())
    odd = False

    if (N in range(2, 6) or N > 20) and N % 2 == 0:
        odd = not False
        print('Not Weird')
    else:
        print('Weird')
