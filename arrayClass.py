class StaticArrays:
    def __init__(self, capacity):
        self.arr = []
        self.capacity = capacity
      
    def insertEnd(self, value):
        if len(self.arr) < self.capacity:
            self.arr.append(value)
        else:
            new_capacity = 2*self.capacity
            self.capacity = new_capacity
            new_arr = []
            new_arr.extend(self.arr)
            new_arr.append(value)
            self.arr = new_arr
                      

    def removeEnd(self):
        self.arr.pop()

    def insertMiddle(self, index, value):
        if len(self.arr) < self.capacity:
            self.arr.insert(value)
        else:
            new_capacity = 2*self.capacity
            self.capacity = new_capacity
            new_arr = []
            new_arr.extend(self.arr)
            new_arr.append(value)
            self.arr = new_arr
            
        
    def removeMiddle(self, index):
        self.arr.pop(index)
   

    def printArr(self):
        print(self.arr)

