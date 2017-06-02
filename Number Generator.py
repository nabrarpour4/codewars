# -*- coding: utf-8 -*-
"""
Created on Fri Nov 04 13:49:07 2016

@author: nicko
"""

import numpy as np

### Compute the sum of all the multiples of either 3 or 5 between 1 to 1000. 

#Method 1 
def divisible_by_number(limit, divs):
    return (i for i in  range(limit) if any(i % div == 0 for div in divs))    
print(sum(divisible_by_number(1000, (3, 5))))
233168

#Method 2
sum([x for x in range(1,1000) if x%3==0 or x%5==0])
233168

#Method 3
np.array([x for x in range(1,1000) if x%3==0 or x%5==0]).sum()
233168

# Method 4 - Nickolas Abrarpour
def div_func(num):
    lst = []
    for i in range(num):
        if i % 3 == 0 or i % 5 == 0:
            lst = lst + [i]
    return lst
sum(div_func(1000))


