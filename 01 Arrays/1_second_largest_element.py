def second_largest_element(nums):
    n = len(nums)
    largest = float('-inf')
    second_largest = float('-inf')
    for i in range(0,n):
        if nums[i] > largest:
            second_largest = largest
            largest = nums[i]

    for j in range(0,n):
        if nums[j] > second_largest and nums[j] != largest:
            second_largest = nums[j]
    
    if second_largest == float('-inf'):
        second_largest = largest
        
    return second_largest

print(second_largest_element([1,2,3]))