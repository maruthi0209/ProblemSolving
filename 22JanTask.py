#########################################################
def rotate_array(nums, k):
    # Handle cases where k is greater than the length of the array
    k %= len(nums)
    
    # Rotate the array
    nums[:] = nums[-k:] + nums[:-k]
    return nums

# Input from the user
nums = list(map(int, input("Enter the elements of the array separated by space: ").split()))
k = int(input("Enter the number of steps to rotate: "))

# Perform rotation and print the result
rotated_array = rotate_array(nums, k)
print(f"Rotated array: {rotated_array}")

#########################################################
class Solution:
    def leaders(self, arr):
        # code here
        n = len(arr)
        leaders = []
        max_from_right = arr[-1]  # Start with the rightmost element
        
        # The rightmost element is always a leader
        leaders.append(max_from_right)
        
        # Traverse the array from right to left
        for i in range(n - 2, -1, -1):
            if arr[i] >= max_from_right:
                max_from_right = arr[i]  # Update max_from_right
                leaders.append(arr[i])  # Add current element to leaders
        
        # Since we traverse from right to left, reverse the leaders list
        return leaders[::-1]


#########################################################
def rotate_left(arr, k):
    n = len(arr)
    k %= n  # Handle cases where k is greater than the length of the array
    # Rotate the array to the left
    return arr[k:] + arr[:k]

# Input from the user
arr = list(map(int, input("Enter the elements of the array separated by space: ").split()))
k = int(input("Enter the number of elements to rotate to the left: "))

# Perform rotation and print the result
rotated_array = rotate_left(arr, k)
print(f"Rotated array: {rotated_array}")
