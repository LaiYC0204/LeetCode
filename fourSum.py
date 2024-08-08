#雙指針
def fourSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    if len(nums) < 4:
        return []
    
    nums.sort()
    output = []

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]: #重複狀況
            continue
        for j in range(i+1,len(nums)):
            if j > i + 1 and nums[j] == nums[j - 1]: #重複狀況
                continue

            left, right = j + 1, len(nums) - 1 #重製指針
            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]
                if total > target:
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    output.append([nums[i], nums[j], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:  # 跳過重複的左指針
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:  # 跳過重複的右指針
                        right -= 1
                    left += 1
                    right -= 1
    return output


print(fourSum([-2,-1,-1,1,1,2,2], 0))