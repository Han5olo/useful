# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 21:31:31 2020

@author: Dorian
"""
def writeFile(d, name, p='w'):
    f = open(str(name), p)
    f.write(str(d))
    f.close()    
def checkEmpty(d):
    if d.isnull().sum().sum()>0:
        print(d.isnull(),sum().sum() , "empy cells found.")
    else:
        pass #no empty cells    
def printLog(*args, **kwargs):
    print(*args, **kwargs)
    with open('printLog.txt','a') as file:
        print(*args, **kwargs, file=file)
def percentNum(p, num, mod):
    """if mod = np: turns number in percent
       if mod = pn: turn percent in number
    """
    if mod == 'pn':
        return p*num/100
    elif mod == 'np':
        return p/num
#***END**FUNCTIONS
