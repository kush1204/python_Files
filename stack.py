#implementing stack

class stack:
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def is_empty(self):
        return self.items==[]
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]






