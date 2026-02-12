class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        
       
        
        
        
        
        
        state = False 
        ans = []
        strs= ""
        
        for line in source:
            j=0
            while (j < len(line)):
                if state:
                    if j+1<len(line) and line[j] == "*"  and line[j+1]== "/":
                        state=False 
                        j+=1

                else:
                    if j+1<len(line) and line[j]== "/"  and line[j+1] == "/":
                        break
                    elif j+1<len(line) and  line[j]== "/" and line[j+1] == "*":
                        state=True
                        j+=1
                    else:
                        strs +=line[j]           
                   
                j+=1
            if state == False and strs!="":
                ans.append(strs)   
                strs= ""
        
        return ans
            


        