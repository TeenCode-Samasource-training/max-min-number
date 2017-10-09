def findMaxMin(a=[]):
    final = []
    #check if list has an index 2 or more
    if len(a) < 2:
        return "You can only compare 2 or more digits"
    else:
        a.sort()
        #if all numbers equal return the number.[1, 1, 1] should return [1]
        if a[0] == a[-1]:
            final.append(a[0])
        else:
            #return the  min and max respectively
            final.append(a[0])
            final.append(a[-1])
        return final
print (findMaxMin([2,-10,3,4,9,100,1000,50]))
