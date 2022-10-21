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

def partition(array, l, h):   #Partition Function - actual logic for quick sort

	pivot = array[h]            #Assingng last assignment as pivot As per the requirementc;
	i = l - 1                   

	for j in range(l, h):        #Comparing pivot with entire array 
		if array[j] <= pivot:    #if element at j is smaller then pivot
			i += 1               #Increment i 
			(array[i], array[j]) = (array[j], array[i])  #swapping (i)th position to (j)th position

	(array[i + 1], array[h]) = (array[h], array[i + 1])     # swappig the pivot with greater element than i

	return i + 1

def quickSort(array, l, h):      
	if l < h:
		pi = partition(array, l, h)         #pivot derivation
		quickSort(array, l, pi - 1)         #recursive call for left array
		quickSort(array, pi + 1, h)         #recursive call for rgiht array


def readFunction(num):
    Sum_array = []
    content_new = np.loadtxt("arr%s.txt"%num)  #Read file data
    content = content_new.tolist()
    
    for j in range(len(content)):           #summation of array
        sumation = sum(content[j])
        content[j].append(sumation)
    # print(content)    
    for z in range(len(content)):           
        Sum_array.append(content[z][3])

    size = len(Sum_array)
    quickSort(Sum_array, 0, size-1)         #main call to sort array of sum column 
    # print(Sum_array)
    lst=[]          #list declaration to store final output
    count = 0
    for i in range(len(Sum_array)):
        if count >=2:               #To prevent multiple entries of same format
            count = count - 1
            continue
        count = 0
        if count==1 or count==0:            #To prevent multiple entries of same format
            for j in range(len(content)):
                if Sum_array[i] == content[j][3]:
                    lst.append(content[j])
                    count = count + 1
    # print("sorted array is:%s" %lst)                   #Remove comment tag to print sorted arrays in terminal 
    with open('arrQS_O_%s.txt' %num, 'w') as f:  #writing the final output in outputfile
            s = '\n'.join(str(x) for x in lst)
            f.writelines(s)


for i in (20,100,1000,4000):           # input for count of rows of no to generate 
    content_generate(i) 
    start = time.time()
    readFunction(i)         # This call will read the file and also appply quicksort. 
    end = time.time()
    time_elapsed = end - start       # time reading meter
    print(f"Sorting complete for {i} numbers.Time taken in Quick sort for {i} numbers: {time_elapsed} seconds.")
    print("\n")