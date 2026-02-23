class Solution:
    def intToRoman(self, num: int) -> str:
    # Forth
        thousands = ["", "M", "MM", "MMM"]
        hundreds  = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        tens      = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        ones      = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        return (
            thousands[num//1000]+
            hundreds[(num%1000)//100]+
            tens[(num%100)//10]+
            ones[num%10]

        )
    
    
    
    
    
    # Third tiral
        # intTo = [
        #     1000 , 900 , 500 , 400 , 
        #     100 , 90 , 50 , 40,
        #     10 , 9 , 5 , 4 , 1
        #     ] 
        # roman = [
        #     "M" , "CM" ,"D" , "CD",
        #     "C" , "XC", "L" ,"XL",
        #     "X" , "IX" , "V" , "IV" , "I"
        # ]

        # res =""
        # for i in range(len(intTo)):
        #     while num >= intTo[i]:
        #         num-=intTo[i]
        #         res +=roman[i]
        # return res 





    # # second try
    #     ans = []
    #     while num>0:
    #         if num >= 1000:
    #             num-= 1000
    #             ans.append("M")
    #         elif num >= 900:
    #             num-= 900
    #             ans.append("CM")
    #         elif num >= 500:
    #             num-= 500
    #             ans.append("D")
    #         elif num >= 400:
    #             num-=400
    #             ans.append("CD")
    #         elif num >= 100:
    #             num -= 100
    #             ans.append("C")
    #         elif num >=90:
    #             num -= 90
    #             ans.append("XC")
    #         elif num >= 50:
    #             num -=50
    #             ans.append("L")
    #         elif num>=40:
    #             num-=40
    #             ans.append("XL")
    #         elif num>=10:
    #             num-=10
    #             ans.append("X")
    #         elif num==9:
                
    #             ans.append("IX")
    #             return "".join(ans)
    #         elif num >=5:
    #             num-=5
    #             ans.append("V")
    #         elif num==4:
    #             ans.append("IV")
    #             return "".join(ans)
    #         else :
    #             num-=1
    #             ans.append("I")
    #     return "".join(ans)





        


    








    #    first try
        # ans = []
        # strs = str(num)
        # i = 0
        # while num > 0: 
        #     if i < len(strs) and i < int(strs[i]) == 4 :
        #         if num >=400:
        #             num-=400
        #             ans.append("CD")
        #             i+=1
        #         elif num >= 40:
        #             num-=40
        #             ans.append("XL")
        #             i+=1
        #         elif num == 4:                    
        #             ans.append("IV")
        #             return ans
        #     elif i < len(strs) and int(strs[i]) == 9:
        #         if num >=900:
        #             num-=900
        #             ans.append("CM")
        #             i+=1
        #         elif num >= 90:
        #             num-=40
        #             ans.append("XC")
        #             i+=1
        #         elif num == 9:                    
        #             ans.append("IX")
        #             return ans
        #     else :
        #         if num >1000:
        #             num-=1000
        #             ans.append("M")
        #             i+=1
        #         elif num > 500:
        #             num-=1000
        #             ans.append("D")
        #             i+=1
        #         elif num > 50:
        #             num-=50
        #             ans.append("C")
        #             i+=1
        #         elif num > 10:
        #             num-=10
        #             ans.append("X")
        #             i+=1
        #         elif num>5:
        #             num-=5                    
        #             ans.append("V")
        #             i+=1
        #         else:
        #             num-=1
        #             ans.append("I")
        #             i+=1
        # ans = "".join(ans)
        
        # return ans

            



                    

        

    
        