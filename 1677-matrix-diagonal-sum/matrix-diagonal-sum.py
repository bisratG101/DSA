class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        sum =0
        r = len(mat[0])-1
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if j==i :
                    sum+=mat[i][j]
                if j+i == r:     
                    if i==j:
                        continue               
                    sum+=mat[i][j]
        return sum
        
                


        