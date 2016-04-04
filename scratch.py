def binarySearch(L,v):
    if hasattr(binarySearch,"count"): #Allows for this to be written recursively without declaring a global variable || this effectively stores the count in the function definition
        binarySearch.count += 1 #If the function depth counter has already been declared increment it by 1 since we are in another level of recursion
    else:
        binarySearch.count = 0 #Initilialize the depth counter to zero

    midpoint = int(len(L)/ 2) #Finds the midpoint of the list by taking the length of the list and dividing it by two and casting it to an int
    print midpoint
    if midpoint == 0:
        return(False, binarySearch.count)

    if L[midpoint] == v:
        #return (True, binarySearch.count)
        binarySearch.ret = (True, binarySearch.count)
    else:
        if (L[midpoint] < v):
            binarySearch(L[midpoint + 1:], v)
        else:
            binarySearch(L[:midpoint], v)

    if hasattr(binarySearch, "ret"):
        return binarySearch.ret
    else:
        return (False, binarySearch.count)
    del binarySearch.count

L = [0,4,6,12,13,25,27]
print "binarySearch test case #1: " + str(binarySearch(L,-1) )
print "binarySearch test case #2: " + str(binarySearch(L,12))
#print "binarySearch test case #3: " + str(binarySearch(L,25) )