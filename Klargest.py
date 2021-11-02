
class Raihan:

  def get_k_largest(arr, k):
      # validation when k bigger than length array
      if k > len(arr):
        print (*arr, sep = " ")
        return arr
      else: 
        # Sort the given array arr in reverse
        arr.sort(reverse = True)
        temp = []
        for i in range(k):
          # print (arr[i], end =" ")
          temp.append(arr[i])
        return temp
  
# Run Program
# arr = [1, 23, 12, 9, 30, 2, 50]
# # n = len(arr)
# k = 3
# Raihan.get_k_largest(arr, k)