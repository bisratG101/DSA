class FrequencyTracker:

    def __init__(self):
        self.mp_count = {}
        self.mp_ferq = {}     
       
    def add(self, number: int) -> None:
        if number not in self.mp_count:
            self.mp_count[number]=1
            self.mp_ferq[1]=self.mp_ferq.get(1,0)+1
            return
        old = self.mp_count.get(number,0)  
        
        new = old+1
        self.mp_count[number] = new
        if old>0:
            self.mp_ferq[old]-=1
        self.mp_ferq[new]=self.mp_ferq.get(new,0)+1

    def deleteOne(self, number: int) -> None:
        if number not in self.mp_count or self.mp_count[number]==0:
            return 
        old = self.mp_count[number]
        new = old - 1
        self.mp_count[number] = new
        self.mp_ferq[old] -=1
        if new > 0:
            self.mp_ferq[new]=self.mp_ferq.get(new , 0)+1
      
    def hasFrequency(self, frequency: int) -> bool:
        return self.mp_ferq.get(frequency,0)> 0

        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)