# 4.Write a program to generate a 3*5*8 3D array whose each element is 0

class Array3d:
    def create3d(self):
        d1, d2 ,d3 = (3, 5, 8) 
        arr = [[[0 for i in range(d3)] for j in range(d2)] for k in range(d1)]
        print(arr)

x=Array3d()
x.create3d()
