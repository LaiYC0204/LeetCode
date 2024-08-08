# 用別人寫好的
def funSearch(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    try:
        return nums.index(target)
    except:
        return -1

# 暴力解
def violenceSearch(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

# GPT演算法
def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] != target:
            # 判斷左側陣列是否為有序的
            if nums[left] <= nums[mid]:
                # 判斷target是否在左側陣列中
                if nums[left] <= target < nums[mid]:
                    right = mid -1
                else:
                    left = mid + 1
            else:
                # 判斷target是否在右側陣列中
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid -1
        else:
            return mid
    return -1

print(search([5,6,7,0,1,2],5))