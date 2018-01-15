"""
Created on Mon Jan  11 17:00:23 2018

@author: Parth Wazurkar
"""

from random import random
from time import clock
import matplotlib.pyplot as plt


def getnewlist(nums):
    """Returns a list of (n) random numbers."""
    return [random() for x in range(nums)] 

#Selection Sort Implementation
def SelectionSort(numbers):
    length = len(numbers)
    for i in range (0,len(numbers)):
        max_index = 0
        for j in range(i,(length - i - 1)):
            if numbers[j] > numbers[max_index]:
                max_index = j
                
        numbers[-i-1],numbers[max_index] = numbers[max_index],numbers[-i-1]

#Bubble Sort Implementation
def BubbleSort(numbers): 
    nums = len(numbers)
    for i in range(nums):
        for j in range( i + 1, nums):
            if numbers[j] < numbers[i]:
                numbers[j], numbers[i] = numbers[i], numbers[j] 
                
#Insertion Sort Implementation
def InsertionSort(numbers): 
    for index in range(1, len(numbers)):
        currentvalue = numbers[index]
        position = index        
        while position > 0 and numbers[position - 1] > currentvalue: 
            numbers[position] = numbers[position - 1] 
            position -= 1   
        numbers[position] = currentvalue

#Merge Sort Implementation
def merge(left, right):
    if not len(left) or not len(right):
        return left or right
 
    result = []
    i, j = 0, 0
    while (len(result) < len(left) + len(right)):
        if left[i] < right[j]:
            result.append(left[i])
            i+= 1
        else:
            result.append(right[j])
            j+= 1
        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break
 
    return result
 
def MergeSort(numbers):
    if len(numbers) < 2:
        return numbers
 
    middle = len(numbers)/2
    left = MergeSort(numbers[:int(middle)])
    right = MergeSort(numbers[int(middle):])
 
    return merge(left, right)

#Quick Sort Implementation
def partition(arr,low,high):
    i = ( low-1 )         
    pivot = arr[high]      
    for j in range(low , high):
        if   arr[j] <= pivot:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
 
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return ( i+1 )
 
def QuickSort(numbers):
    low=0
    high=len(numbers)-1
    if low < high:
        pi = partition(numbers,low,high)
        QuickSort(numbers[:int(pi-1)])
        QuickSort(numbers[int(pi+1):])
        
#Test a sorting algorithm on a list and return execution time.
def test(sorttype, unsortedlist):
    copy = unsortedlist[:]
    start = clock() 
    sorttype(copy)
    duration  = clock() - start 
    #print(sortType.__name__ + " took " + str(duration) + " seconds.")
    return duration

#Produce a graph of # of #'s in random list against execution time for each algorithm.
def produceresults(startnumofnums=1, endnumofnums=2000, increment=50):
    xvals = []
    ySelectionSort = []
    yBubbleSort = []
    yInsertionSort = []
    yMergeSort = []
    yQuickSort = []
    
    #append durations returned from sorting alg. to relevant yval list
    for i in range(startnumofnums, endnumofnums, increment):
        listtosort = getnewlist(i)[:] 
        xvals.append(i) 
        ySelectionSort.append(test(SelectionSort, listtosort))
        yBubbleSort.append(test(BubbleSort, listtosort)) 
        yInsertionSort.append(test(InsertionSort, listtosort))
        yMergeSort.append(test(MergeSort, listtosort)) 
        yQuickSort.append(test(QuickSort, listtosort)) 
          
    #Set line on plot   
    plt.plot(xvals, ySelectionSort, color="k", label="Selection Sort")      
    plt.plot(xvals, yBubbleSort, color="r", label="Bubble Sort") 
    plt.plot(xvals, yInsertionSort, color="b", label="Insertion Sort") 
    plt.plot(xvals, yMergeSort, color="g", label="Merge Sort") 
    plt.plot(xvals, yQuickSort, color="y", label="Quick Sort")
    plt.xlabel("Number of numbers in random list") 
    plt.ylabel("Time taken to sort / seconds") 
    plt.title("Time taken for sorting algorithms to sort random lists") 
    plt.legend(loc=2) 
    plt.show() 
            
