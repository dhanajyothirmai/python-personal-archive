#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on 

@author: raja.raman

source:
    custom exception:
        https://stackoverflow.com/questions/1319615/proper-way-to-declare-custom-exceptions-in-modern-python
'''
import math

class SGNorthAuthException(Exception):
    pass

def get_remote_address(ip_address):
    '''
        HttpRequestUtil::getRemotrAddr
    '''
    return None

def get_referer():
    '''
        HttpRequestUtil::getReferer
    '''
    
    return None

def get_user_agent():
    '''
        HttpRequestUtil::getUserAgent
    '''
    
    return None


def main():
    pass
     
    
if __name__ == '__main__':
    main()
    