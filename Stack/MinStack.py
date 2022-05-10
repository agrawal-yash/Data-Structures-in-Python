# -*- coding: utf-8 -*-
"""
Created on Mon May  9 23:14:00 2022

@author: agraw
"""

import math

# Retrieve Minimun Value from stack in constant time
# instead of individual items, you push tuples on stack 
# with each item having the min value of the stack as the 2nd value

class Stack :
    def __init__(self):
        """ Initializing and empty list as our stack """
        self.stack  = []
        
    def isempty(self):
        """ Checking if our list is empty or not """
        return self.stack == []
    
    def __str__(self):
        """ function to print the stack directly from the object """
        return str(self.stack)
    
    def push(self, data):
        """ pushes a tuple onto the stack : the value itself and the min value between itself and the current min of the stack """
        self.stack.append((data, min(data, self.getMin())))
        
    def pop(self):
        """ pops/removes the last value from the list if list is not empty """
        if self.isempty():
            pass
        else:
            self.stack.pop()
        
    def peek(self):
        """ returns to display the last value from the list if list is not empty """
        if self.isempty():
            return ''
        
        return self.stack[-1][0]
    
    def getMin(self):
        if self.stack != []:
            return self.stack[-1][1]
        
        return math.inf

if __name__ == "__main__":
    stack = Stack()
    
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(-1)
    stack.push(4)
    stack.push(5)
    stack.push(-10)
    stack.push(0)
    
    print (stack.getMin())