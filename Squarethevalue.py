# 8. Write a program which can map() to make a list whose elements are square of numbers
# between 1 and 20 (both included).

# using map
def squared(n): 
    return n * n 

numbers = (1, 2, 3, 4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20) 
result = map(squared, numbers) 
print(list(result)) 

 # using lambda 
result = map(lambda x, y: x * y, numbers, numbers) 
print(list(result)) 