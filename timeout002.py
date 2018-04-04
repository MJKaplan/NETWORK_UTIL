# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 20:46:03 2018

@author: Mik
"""

import time
import timeout_decorator


@timeout_decorator.timeout(5)
def test():
    for i in range (20):
        print (i)
        time.sleep(1)
    
test()