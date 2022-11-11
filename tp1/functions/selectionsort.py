# Selection sort in Python
# time complexity O(n*n)
#sorting by finding min_index
def selectionSort(array, size):
    # exp : arr = [10,5,45,23]
	for ind in range(size):
		min_index = ind     # min_index = 10

		for j in range(ind + 1, size): # 10 -> test min index --> [5,45,23]
			# select the minimum element in every iteration
			if array[j] < array[min_index]:
				min_index = j # min_index = 5 -> because 5<10
		# swapping the elements to sort the array
		(array[ind], array[min_index]) = (array[min_index], array[ind])

"""arr = [-2, 45, 0, 11, -9,88,-97,-202,747]
size = len(arr)
selectionSort(arr, size)
print('The array after sorting in Ascending Order by selection sort is:')
print(arr)"""
