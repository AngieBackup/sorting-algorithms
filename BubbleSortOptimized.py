# An optimized version of Bubble Sort 
def bubbleSort(array): 
    n = len(array) 
   
    # Traverse through all array elements 
    for i in range(n): 
        swapped = False
  
        # Last i elements are already 
        #  in place 
        for j in range(0, n-i-1): 
   
            # traverse the array from 0 to 
            # n-i-1. Swap if the element  
            # found is greater than the 
            # next element 
            if array[j] > array[j+1] : 
                array[j], array[j+1] = array[j+1], array[j] 
                swapped = True
  
        # IF no two elements were swapped 
        # by inner loop, then break 
        if swapped == False: 
            break

# Driver code to test above 
array = [4, 314, 945, 32, 2, 1, 9]
   
bubbleSort(array) 
   
print ("Sorted array :") 
for i in range(len(array)): 
    print ("%d" %array[i],end=" ")