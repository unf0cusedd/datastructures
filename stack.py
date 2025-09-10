
class Node:
    def __init__(self, value, next_node):  
        self.value = value
        self.next = next_node

class LinkedList:
    def __init__(self):  
        self.start = None 
        self.lngth = 0
    
    def add(self, value):  
        self.start = Node(value, self.start)
        self.lngth += 1

    def print(self): 
        while self.start != None: 
            print(self.start.value)
            self.start = self.start.next
        

    def pop(self):
        p = self.start.value
        new_start = self.start.next 
        self.start = new_start
        return p 
    
    def empty(self): 
        if self.start == None: 
            print("Stack is empty")
            return True 
    
    def __len__(self): 
        return self.lngth



