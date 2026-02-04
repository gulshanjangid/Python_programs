def find_largest(arr):
    if not arr:
        return None  # Return None for an empty array
    largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num
    return largest


arr = [1, 2, 3]
largest_element = find_largest(arr)
print("The largest element in the array is:", largest_element)