#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on 

@author: raja.raman

source:
    
    https://stackoverflow.com/questions/16772071/sort-dict-by-value-python
    
    https://stackoverflow.com/questions/20577840/python-dictionary-sorting-in-descending-order-based-on-values
'''

def sort_by_key(dict):
    '''
        ::getRemotrAddr
    '''
    '''
    for key, value in sorted(dict.iteritems(), key=lambda(k,v): (v,k)):
        print("%s: %s" % (key, value))
    '''
    
    for key in sorted(dict.keys()):
        print("%s: %s" % (key, dict[key]))
    
    return None

def sort_by_value(dict):
    '''
        ::getRemotrAddr
    '''
    
    age_sorted = sorted(dict.items(), key=lambda x:x[1])
   
    print(age_sorted)
       
    return None

def sort_by_value_model_2(dict):
    '''
        ::getRemotrAddr
    '''
    
    age_sorted = sorted(dict, key=dict.get)
   
    print(age_sorted)
       
    return None

def reverse_sort_by_value(age):
    '''
        ::getRemotrAddr
    '''
    
    age_sorted = sorted(age.items(), key=lambda x:x[1], reverse=True)
   
    print(age_sorted)
       
    return None


def main():
    
    age = {
            'carl':40,
            'alan':2,
            'bob':1,
            'danny':3
        }
    
    sort_by_value(age)
    
    sort_by_value_model_2(age)
    
    reverse_sort_by_value(age)
     
    
if __name__ == '__main__':
    main()
    