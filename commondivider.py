# 6.Write a program using generator to print the numbers which can be divisible by 5
# and 7 between 0 and n in comma separated form while n is input by console.
class commondivider:
    def createlist(self,n):
        divided = []
        for i in range(5,n+1):
            if i % 5 == 0 and i % 7 ==0 :
                divided.append(i)
                print(i)
obj1 = commondivider()
n=int(input('Enter the n value '))
obj1.createlist(n)