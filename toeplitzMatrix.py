class Solution(object):
    def isToeplitzMatrix(self, matrix):
      for i in range(len(matrix[0])-1):
        for j in range(len(matrix)-1):
            if matrix[j][i] != matrix[j+1][i+1]:
                return False
              
      return True

        