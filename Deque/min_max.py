'''
Problem : Design a data structure in which we can add 2 type of values, maximum and 
          minimum with conditions that minimum and maximum values which are to be inserted
          are not between current maximum and minimum present in the data structure.
          We have 6 main methods available on that data structure which are :
          
          insertMin : Inserts minimum value. Value is always less than current min present in DS.
          insertMax : Inserts maximum value. Value is always greater than current max present in DS.
          getMin : Gets current minimum.
          getMax : Gets current maximum.
          extractMin : Removes current minimum from the DS.
          extractMax : Removes current maximum from the DS.

Approach : Simply use deque. For min, operate at front, for max operate at rear.
'''

from collections import deque

class MaxMinDS :
    def __init__(self) -> None:
        self.dq = deque()
    
    def insertMax(self,val) :
        self.dq.append(val)
    
    def insertMin(self,val) :
        self.dq.appendleft(val)
    
    def getMax(self) :
        return self.dq[-1]
    
    def getMin(self) :
        return self.dq[0]
    
    def extractMax(self) :
        return self.dq.pop()
    
    def extractMin(self) :
        return self.dq.popleft()

if __name__ == "__main__" :
    d = MaxMinDS() 
    d.insertMax(10)
    d.insertMax(11) # Any value less that 10 cannot be passed
    d.insertMin(4)
    d.insertMin(-1)
    d.insertMax(14)
    print(d.getMax()) # 14
    print(d.getMin()) # -1
    print(d.extractMax()) # 14