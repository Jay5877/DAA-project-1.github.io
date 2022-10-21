import os.path
import numpy as np
import time

def content_generate(count):  # content generation
    test=[]
    if os.path.exists("arr%s.txt" %count):    # To omit the generate part if already generated
        return()
    else:
        for i in range(count):
            sample = list(np.random.randint(low = 0,high=99,size=3)) #generating Random Integers
            test.append(sample)
            np.savetxt("arr%s.txt" %count , test, fmt = "%s")       # saving in file

def merge(array): #function to fetch the file and summation af columns
    Sum_array = []
    content_new = np.loadtxt("arr%s.txt" %array)  #file fetch
    content = content_new.tolist()
    
    for j in range(len(content)):
        sumation = sum(content[j])                #summation
        content[j].append(sumation)
    

    lst=mergesort(content)                    #mergesort
    # print("sorted array is:%s" %lst)                    #Remove comment tag to print sorted arrays in terminal 

    with open('arrMS_O_%s.txt' %array, 'w') as f:  #writing the final output in outputfile
            s = '\n'.join(str(x) for x in lst)
            f.writelines(s)

def mergesort(arra):                        #Actual logic of merge sort
    if len(arra) > 1:
        mid = len(arra)//2 #deciding the middle element 
        L = arra[:mid]      #partiion left                  
        R = arra[mid:]      #partition right
    
        mergesort(L)        #mergsort call for first half
        mergesort(R)        #mergesort call for second half
        
        i = j = k = 0       #setting all the variable at first pointer

        while i < len(L) and j < len(R):   #for last element
            if L[i][3] <= R[j][3]:
                arra[k] = L[i]
                i += 1
            else:
                arra[k] = R[j]
                j += 1
            k += 1
          
        while i < len(L):
            arra[k] = L[i]
            i += 1
            k += 1
    
        while j < len(R):
            arra[k] = R[j]
            j += 1
            k += 1
    return arra
        
for i in (20,100,1000,4000):  # input for count of rows of no to generate
    content_generate(i)
    start = time.time()
    merge(i)   #Merge sort  
    end = time.time()
    time_elapsed = end - start  # time reading meter
    print(f"Sorting complete for {i} numbers. Time taken in Merge sort for {i} numbers: {time_elapsed} seconds.")
    print("\n")