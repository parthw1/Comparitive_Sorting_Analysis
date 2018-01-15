"""
Created on Mon Jan  11 17:00:23 2018

@author: Parth Wazurkar
"""

from sorting_funcs import getnewlist, SelectionSort, BubbleSort, InsertionSort, test, produceresults, MergeSort, QuickSort

randomlist = getnewlist(500) #Get a list of 500 random numbers

print("SelectionSort took: " + str(test(SelectionSort, randomlist)) + "seconds.")
print("BubbleSort took: " + str(test(BubbleSort, randomlist)) + " seconds.")
print("InsertionSort took: " + str(test(InsertionSort, randomlist)) + "seconds.")
print("MergeSort took: " + str(test(MergeSort, randomlist)) + "seconds.")
print("QuickSort took: " + str(test(QuickSort, randomlist)) + "seconds.")

produceresults(1, 3000, 20) #Comparison graph between algorithms acting on list of size 1 to 3000, incrementing by 20
