class Solution:
    def minDeletionSize(self, strs):
        matrix = [list(word) for word in strs]
        count = 0
        for i in range(len(matrix[0])):
            for j in range(len(matrix)-1):
                if matrix[j][i] > matrix[j+1][i]:
                    count+=1
                    break
        return count            
