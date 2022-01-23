import stack
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

s=stack()
def bal_par(string):
     index=0
     balanced=True
     while index<len(string) and balanced:
        symbol=string[index]
        if symbol=="(":
               s.push(symbol)
        else:
               if(s.is_empty()==True):
                   balanced=False
               else:
                   s.pop()
        index+=1
     if(s.is_empty() and balanced):
         return True
     else:
         return False

print(bal_par('(()'))







