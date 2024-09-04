class Solution(object):
    def findTheWinner(self, n, k):
      array= []
      for i in range(1,n+1):
        array.append(i) 
      i = 0   
      while len(array)>1:
        i= (i + k -1) %len(array)
        array.pop(i)
      return array[0]    



        