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

def mean(L):
    total = 0.0 #Initialize to floating point
    for i in L: #Iterates through each element in the list L
        total += i #Adds the current list element to the total counter
    return total/len(L) #Returns the total divided by the number of elemens | Mean

def median(L):
    if len(L)%2 == 0: #Case where list has an even number of elemements
        total = L[len(L)/2] + L[(len(L)/2) -1] #Takes the two elements in the middle of the list and sums them
        return total / 2.0 #Takes the sum of the two elements in the middle of the list and returns their average
    else: #Case where list has an odd number of elements
        return L[len(L)/2] #Returns the element in the middle of the list.


x = [5,1,2,3,1]
y = [5,1,2,3,1,4]
print "mean test case #1: " + str(mean(x) == float(12)/float(5))
print "mean test case #2: " + str(mean(y) == float(16)/float(6))
print "median test case #1: " + str(median(x) == 2)
print "median test case #2: " + str(median(y) == 2.5)
print median(y)