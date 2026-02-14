class FrequencyTracker:

    def __init__(self):
        self.numCount = {}
        self.freqCount = {}

    def add(self, number: int) -> None:
        oldFreq = self.numCount.get(number, 0)
        newFreq = oldFreq + 1

        self.numCount[number] = newFreq

        if oldFreq > 0:
            self.freqCount[oldFreq] -= 1

        self.freqCount[newFreq] = self.freqCount.get(newFreq, 0) + 1

    def deleteOne(self, number: int) -> None:
        if number not in self.numCount or self.numCount[number] == 0:
            return

        oldFreq = self.numCount[number]
        newFreq = oldFreq - 1

        self.freqCount[oldFreq] -= 1

        if newFreq > 0:
            self.numCount[number] = newFreq
            self.freqCount[newFreq] = self.freqCount.get(newFreq, 0) + 1
        else:
            del self.numCount[number]

    def hasFrequency(self, frequency: int) -> bool:
        return self.freqCount.get(frequency, 0) > 0



# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)