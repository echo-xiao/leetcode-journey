class TwoSum(object):

    def __init__(self):
        self.counts = {}

        

    def add(self, number):
        if number in self.counts:
            self.counts[number] += 1
        else:
            self.counts[number] = 1
        

    def find(self, value):
        for num in self.counts:
            diff = value - num
            if diff in self.counts:
                if diff != num:
                    return True
                elif self.counts[num] >= 2:
                    return True
        return False
            
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)