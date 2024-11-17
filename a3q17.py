# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 17:40:56 2024

@author: senor
"""

def vowelRemove(s):
    for i in ['a','e','i','o','u','A','E','I','O','U']:
              s=s.replace(i,'')
    return s
s=input("Enter a string")
print("After removing vowels:",vowelRemove(s))