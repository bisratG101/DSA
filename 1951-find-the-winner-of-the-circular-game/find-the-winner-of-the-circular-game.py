class Solution(object):
    def findTheWinner(self, n, k):
        arr = list(range(1, n+1))
        kcop = k
        num = n
        i = 0
        while(num!=1):
            if arr[i]==-1 :
                i+=1
                if i==n: i=0
                continue  
            k -=1
            i+=1
            if k==0:
                k=kcop
                arr[i-1]=-1
                num-=1

            if i==n: i=0
        for i in arr:
            if i !=-1:
                return i
        return 0
            

     