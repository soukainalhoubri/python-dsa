#Worst time complexityis O(n²): when the array is decreasignly sorted, we will have to go through the whole process
#Space complexity is O(1) : The algorithm modifies the array in-place, no extra-space is needed

def bubbleSort(array):
  n=len(array)
  still=True# This variable is used to check if swaps are still happening, which means that the array is still unsorted
  while still:
    still=False
    i=0
    while i<n-1:
      if array[i]>array[i+1]:
        array[i],array[i+1]=array[i+1],array[i]
        still=True
      i+=1
    n-=1# in each traversal, we make sure that the largest item is at its correct position, so we can safely decrease the 
    #number of elements we need to check by decrementing n on each traversal
  return array

#testing

array1=[9,8,7,4,3,9]
array2=[5,5,5,5,5]
print(bubbleSort(array1))
print(bubbleSort(array2))
    