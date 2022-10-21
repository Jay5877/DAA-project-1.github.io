import numpy as np 
import time           
import os.path

def content_generate(count):  # content generation
    test=[]
    if os.path.exists("arr%s.txt" %count):    # To omit the generate part if already generated
        return()
    else:
        for i in range(count):
            sample = list(np.random.randint(low = 0,high=99,size=3)) #generating Random Integers
            test.append(sample)
            np.savetxt("arr%s.txt" %count , test, fmt = "%s")       # saving in file

def insertionsort(count):       
    content_new = np.loadtxt("arr%s.txt" %count)     #Read file data
    content = content_new.tolist()
    for j in range(len(content)):          
        sumation = sum(content[j])                  # summing of values
        content[j].append(sumation)
    for i in range(1, len(content)):
        key = content[i]
        j = i -1
        while j >=0 and key[3] < content[j][3]:
            content[j+1] = content[j]
            j -= 1
        content[j+1] = key
    lst = []             #empty list to store sorted elements
    
    for i in range(len(content)):
        lst.append(content[i])                      #appending the elements in sorted order
    # print("Sorted array is :%s" %lst)             #Remove comment tag to print sorted arrays in terminal

    with open('arrIS_O_%s.txt' %count, 'w') as f:   #writing the final output in outputfile
        s = '\n'.join(str(x) for x in lst)
        f.writelines(s)                         

for i in (20,100,1000,4000):    # input for count of rows of no to generate
    content_generate(i)         # Function for content generation  
    start = time.time() 
    insertionsort(i)            #Insertion sort
    end = time.time()
    time_elapsed = end - start  # time reading meter
    print(f"Sorting complete for {i} numbers. Time taken in Insertion sort for {i} numbers: {time_elapsed} seconds.")
    print("\n")