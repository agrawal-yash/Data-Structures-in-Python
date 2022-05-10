# -*- coding: utf-8 -*-
"""
Created on Mon May  9 22:47:31 2022

@author: agraw
"""

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
        """ pushes value onto the stack ie last position of the list """
        self.stack.append(data)
        
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
        
        return self.stack[-1]

if __name__ == "__main__":
    stack = Stack()
    
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    
    print (stack) # expected : 1, 2, 3, 4, 5
    
    stack.pop()
    
    print (stack) # expected : 1, 2, 3, 4
    
    print (stack.peek()) # expected : 4
    
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    
    print (stack) # expected : empty stack

    stack.pop() # nothing should happen since stack will be empty

    print (stack.peek()) # nothing should happen since stack will be empty