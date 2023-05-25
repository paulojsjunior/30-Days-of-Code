#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent


def resolve(meal_cost, tip_percent, tax_percent):
    tip = (meal_cost / 100) * tip_percent
    tax = (tax_percent / 100) * meal_cost
    total_cost = meal_cost + tip + tax
    print('\nTotal cost:', total_cost)

    print('Round value:', round(total_cost))


meal_cost = float(input('Insert the meal price: '))
tip_percent = int(input('Insert the tip percent: '))
tax_percent = int(input('Insert the tax percent: '))

resolve(meal_cost, tip_percent, tax_percent)
