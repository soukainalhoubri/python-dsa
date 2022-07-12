def selection_sort(array):
   # if len(array) in (0,1):
   #    return array
   n=len(array)
   slow=0
   
   # I keep track of two moving pointers: 
   #the slow pointer to know where to put the minimum
   #the fast one to find the minimum
   
   #I think of using two nested loops where in the inner loop I look for the minimum,and in the outer loop, I move the slow pointer  
   
   while slow<n-1:
      min_index=slow#I store the first element as the minimum
      for fast in range(slow,n):
         if array[min_index]>array[fast]:#I check if my current minimum is larger than the current element in the fast pointer
            min_index=fast#if I find a smaller element, I store its index
      array[slow],array[min_index]=array[min_index],array[slow]#here I have made sure of finding the minimum, I put it in its right place
      slow+=1
   
   return array


#testing

print(selection_sort([5,8,9,0,1]))
print(selection_sort([1,2,3,4]))