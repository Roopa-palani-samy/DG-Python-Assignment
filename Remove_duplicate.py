# 3. With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list
# after removing all duplicate values with original order reserved.
class Remove_duplicate:
    def removeDuplicate(self):
        lista=[12,24,35,24,88,120,155,88,120,155]
        seta=set()
        for x in lista:
            print(x)
            if not (x in seta):
                seta.add(x)
        print("roopa")        
        for x in seta:
            print(x)        

y=Remove_duplicate()
y.removeDuplicate()