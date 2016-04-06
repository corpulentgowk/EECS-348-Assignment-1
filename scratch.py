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


def dfsr(tree,elem): #approach essentially uses the input list(tree) as a queue. Children are extracted and appended to the end of the lists.
    if tree: #Runs until the queue(tree) is empty
        val = tree.pop(0) #Takes the first element of the queue(tree) out of the list.
        if type(val) == int: #Checks to see if it is an int or a list
            print val #prints value before evaluation
            if val == elem: #checks to see if the value is equal to the sought element
                return True
            else:
                return False or dfsr(tree,elem)
        else: #its a list
            print val[0] #prints value before evaluation
            if val[0] == elem: #Checks to see if the parent node value is equal to the sought element
                return True
            val = val[1:] #takes the cdr since the first was already checked
            val.reverse() #reverses the list to make it easier to prepend it to the queue
            #effectively prioritizing the children of the node currently visited at so that the search goes deep
            for i in val: #iterates trhough the children of the parent node
                tree.insert(0,i) #prepends the childrend to the queue(tree)
            return False or dfsr(tree,elem)
    return False