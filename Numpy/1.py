import numpy as np 
# arr = np.array([1, 2, 3])
# print(arr)

# arr1 = np.array([1, 2, 3])

# print(arr1 / arr2)
# # arr.shape
# arr = np.arange(0,51,5)
# print(arr.shape)

# z = np.zeros(10)
# print(z)


# arr = np.array([10,20,30,40,50,60])
# print(arr[: : 2])
# print(arr[[0, 2, 4]])
# print(arr[arr < 25])
# reshaped_arr = arr.reshape(3, 2)
# print(reshaped_arr)


# arr = np.array([10, 20, 30])
# new_arr = np.insert(arr, 1, 100)
# print(new_arr)


arr = np.array([[1,2],[3,4]])
new_arr = np.insert(arr, 1, [5, 6], axis=0)
new_arr2 = np.insert(arr, 1, [5, 6], axis=1)
print(new_arr)
print(new_arr2)
