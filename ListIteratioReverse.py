# 10. Write an iterator class reverse_iter, that takes a list and iterates it from the reverse
# direction.

class reverse_iter:
    def createlist(self,samplist):
        n = len(samplist)-1
        for i in range(0,n+1):
            print(samplist[n-i])
obj1 = reverse_iter()
obj1.createlist([1,2,3,4,5])