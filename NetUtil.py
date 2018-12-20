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

def ip_to_long(ip_address):
    '''
        NetUtilSGW::public long ipToLong(String ipAddr)
    '''
    
    if(ip_address == '0:0:0:0:0:0:0:1'):
        ip_address = '127.0.0.1'
        
    ip_address_array = ip_address.split('.')
    
    if(len(ip_address_array) != 4):    
        raise SGNorthAuthException('Invalid Ip')
    
    #print(ip_address_array[1])
    
    num = 0
    for i in range(len(ip_address_array)):
        #print(ip_address_array[i])
        power = 3 - i
        num = num + ( (int(ip_address_array[i]) % 256 * int(math.pow(256, power)) ))
    
    return num

def long_to_ip(ip):
    
    ip_address = ((ip >> 24) & 0xFF) + "." + ((ip >> 16) & 0xFF) + "." + ((ip >> 8) & 0xFF) + "." + (ip & 0xFF)
    
    return ip_address

def main():
    
    try:
        ip_long = ip_to_long('10.3.81.34')        
        print(ip_long)
        
        ip_ = long_to_ip(ip_long)
        
        print(ip_)
        
    except SGNorthAuthException as sgwError:
        print('Error : '+str(sgwError))    
    
if __name__ == '__main__':
    main()
    