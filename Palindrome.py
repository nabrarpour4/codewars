# -*- coding: utf-8 -*-
"""
Created on Fri Nov 04 13:48:44 2016

@author: nicko
"""

#Method 1

def Palindrome(num):
    return str(num) == str(num)[::-1]

def highest(bot, top):
    z = 0
    for x in range(top, bot, -1):
        for y in range(top,bot, -1):
            if Palindrome(x*y):
                if x*y > z:
                    z = x*y
    return z    
highest(100,999)
906609


#Method 2

def isPalindrome(s):
    s=str(s)
    return s == s[::-1]
    
def generate_palindrome(minx, maxx):
    tmpList = []
    for i in range(minx, maxx ):
        if isPalindrome(i):
            tmpList.append(i)
        return tmpList
    
generate_palindrome(100, 999)


#Method 3

n = 0  
for a in range(999, 100, -1):  
    for b in range(a, 100, -1):  
        x = a * b  
        if x > n:  
            s = str(a * b)  
            if s == s[::-1]:  
                n = a * b  
print(n)
906609
