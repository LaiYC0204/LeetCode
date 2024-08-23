def searchRange(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    length = len(nums)
    left, right = 0, length - 1

    if length == 1 and nums[0] == target:
        return [0,0]

    while left <= right:
        mid = (left + right) // 2 # 二分法O(log n)
        print(nums[mid])
        if nums[mid] == target:
            left = right = mid
            while nums[left] == target: # 搜尋邊界可能會遍歷整個陣列O(n)
                left -= 1
                if left == -1:
                    break
            while nums[right] == target:
                right += 1
                if right == length:
                    break
            return [left + 1, right - 1]
        elif nums[left] <= target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return [-1, -1]

def GPTsearchRange(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    def findLeft(nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def findRight(nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return right
    
    left_index = findLeft(nums, target)
    right_index = findRight(nums, target)

    # 確保找到的數值是有效
    if left_index <= right_index and right_index < len(nums) and nums[left_index] == target and nums[right_index] == target:
        return [left_index, right_index]
    else:
        return [-1, -1]

print(GPTsearchRange([1,1,1,2,3], 1))