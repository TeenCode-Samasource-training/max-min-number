def findMaxMin(list=[]):
    final = []
    #check if list has an index 2 or more
    if len(list) < 2:
        return "You can only compare 2 or more digits"
    else:
        list.sort()
        #if all numbers equal return the number.[1, 1, 1] should return [1]
        if list[0] == list[-1]:
            final.append(list[0])
        else:
            #return the  min and max respectively
            final.append(list[0])
            final.append(list[-1])
        return final
