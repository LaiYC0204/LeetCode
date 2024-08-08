def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
    
    return left

inputs = [[[1,3,5,6,8,9], 5], [[1,3,5,6], 2], [[1,3,5,6], 7]]
answers = [2,1,4]

for i in range(len(inputs)):
    answer = searchInsert(inputs[i][0], inputs[i][1])
    if answer != answers[i]:
        print(f'input0:{inputs[i][0]} input1:{inputs[i][1]} output:{answer}')