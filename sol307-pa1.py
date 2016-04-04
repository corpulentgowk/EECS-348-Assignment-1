import math



def binarySearch(L,v):
    count = 0 #init depth counter to 0
    ret = False #init return store to false
    midpoint = 99 #Dummy init
    while (midpoint > 0) and (ret == False):
        midpoint = int(len(L) / 2)
        if L[midpoint] == v:
            ret = (True, count)
        else:
            if (L[midpoint] < v):
                L = L[midpoint + 1:] #this function says take all the elements after the midpoint'th element inclusive which is why we add 1
                count += 1
            else:
                L = L[:midpoint] #This says take all the elements up to the midpoint'th element not inclusive which is why we do not need to subtract 1
                count +=1

    if ret == False:
        return (False, count)
    else:
        return ret



L = [0,4,6,12,13,25,27]
print binarySearch(L,-1)

L = [0,4,6,12,13,25,27]
print "binarySearch test case #1: " + str(binarySearch(L,-1) == (False,3))
print "binarySearch test case #2: " + str(binarySearch(L,12) == (True,0))
print "binarySearch test case #3: " + str(binarySearch(L,25) == (True,1))