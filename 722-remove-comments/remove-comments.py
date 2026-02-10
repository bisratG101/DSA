class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        
        result = []
        in_block = False
        curr = ""

        for line in source:
            i = 0
            while i < len(line):
                if in_block:
                    if i + 1 < len(line) and line[i] == '*' and line[i + 1] == '/':
                        in_block = False
                        i += 1 
                else:                   
                    if i + 1 < len(line) and line[i] == '/' and line[i + 1] == '/':
                        break
                    
                    elif i + 1 < len(line) and line[i] == '/' and line[i + 1] == '*':
                        in_block = True
                        i += 1 
                    else:
                        curr += line[i]
                i += 1

            if not in_block and curr:
                result.append(curr)
                curr = ""

        return result
        
        
        
        
        
        # state = False 
       
        # ans = []
        
        # for i in range(len(source)):

        #     j=0
        #     if state == False:
        #         strs=""
        #     while (j < len(source[i])):
        #         if j<(len(source[i])-1) and source[i][j] == "/"  and source[i][j+1] == "/" and state == False:
        #             break
        #         if j<(len(source[i])-1) and source[i][j] == "/"  and source[i][j+1] == "*" and state==False :
        #             state=True
        #             j+=2
        #         if j<(len(source[i])-1) and source[i][j] == "*"  and source[i][j+1] == "/" and state == True:
        #             state=False 
        #             j+=2
                    
        #         if j<(len(source[i])) and  state == False:
        #             strs+=source[i][j]
        #         j+=1
        #     if state == False and strs!="":
        #         ans.append(strs)     
        # source = ans 
        # return source
            


        