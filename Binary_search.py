#5.Write a binary search function which searches an item in a sorted list. The function
# should return the index of element to be searched in the list.
def Binary_search(lista,value):
    first = 0
    last = len(lista)-1
    searchindex = -1
    while(first<=last and searchindex == -1):
        mid = (first+last)//2
    
        if lista[mid] == value :
            searchindex = mid
            
        else :
            if value < lista[mid]:
                last = mid-1
            else :
                first = mid+1
    return searchindex

print(Binary_search([1,2,3,4,5,6,7,8],5))