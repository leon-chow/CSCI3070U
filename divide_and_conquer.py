import math

def init(): 
    string = input("Please enter a string to be searched \n")
    substring = input("Please enter the substring you wish to look for \n")
    counter = 0
    print(divide(string, substring))

def divide(string, substring):
    if len(string) > 1:
        print(string)
        if not string and substring:
            return False
        elif substring == string:
            return True
        else:
            mid = math.ceil(len(string) // 2)
            leftString = string[:mid]
            rightString = string[mid:]

            divide(leftString, substring)
            divide(rightString, substring)
init()



'''# Python program for implementation of MergeSort 
def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 #Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 
  
        mergeSort(L) # Sorting the first half 
        mergeSort(R) # Sorting the second half 
  
        i = j = k = 0
          
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
          
        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1'''
  
