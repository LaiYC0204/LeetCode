import random

class RandomizedSet(object):
    def __init__(self):
        self.d = dict()
        self.l = []

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.d:
            return False
        self.d[val] = len(self.l)
        self.l.append(val)
        return True
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.d:
            last = self.l[-1]
            index = self.d[val]
            self.d[last] = index
            self.l[index] = last
            self.l.pop()
            self.d.pop(val)
            return True
        return False
        

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.l)
        


#Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
print(obj.insert(1))
print(obj.remove(2))
print(obj.insert(2))
print(obj.getRandom())
print(obj.remove(1))
print(obj.insert(2))
print(obj.getRandom())