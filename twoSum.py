#自己寫的
def myTwoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(len(nums)-1):
        for j in range(i + 1, len(nums)):
            if(nums[i] + nums[j] == target):
                return [i,j]
    return 0

#別人寫的，用dict的方法來找有沒有那個key
def otherTwoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    h = {}
    for i, num in enumerate(nums):
        n = target - num
        if n > 0:
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]              

print(otherTwoSum([3,2,4],6))