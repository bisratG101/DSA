class FrequencyTracker:

    def __init__(self):
        self.mp_count = {}
        self.mp_freq = {}     
       
    def add(self, number: int) -> None:
        if number not in self.mp_count:
            self.mp_count[number]=1
            self.mp_freq[1]=self.mp_freq.get(1,0)+1
            return
        old = self.mp_count.get(number,0)  
        
        new = old+1
        self.mp_count[number] = new
        if old>0:
            self.mp_freq[old]-=1
        self.mp_freq[new]=self.mp_freq.get(new,0)+1

    def deleteOne(self, number: int) -> None:
        if number not in self.mp_count:
            return 

        old = self.mp_count[number]       
        new = old-1
        self.mp_freq[old] -=1 

        if self.mp_freq[old] == 0 and new == 0:            
            del self.mp_freq[old]   
            del self.mp_count[number]
            return      
        if self.mp_freq[old] == 0:
            del self.mp_freq[old]  
        if new == 0:
            del self.mp_count[number]
        else :
            self.mp_count[number] = new                
            self.mp_freq[new] = self.mp_freq.get(new , 0)+1 
      
       

        


        # old = self.mp_count[number]
        # new = old - 1
        # self.mp_count[number] = new
        # self.mp_freq[old] -=1
        # if new > 0:
        #     self.mp_freq[new]=self.mp_freq.get(new , 0)+1
      
    def hasFrequency(self, frequency: int) -> bool:
        return self.mp_freq.get(frequency,0)> 0

        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)