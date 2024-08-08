def nextPermutation(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    for i in range(len(nums)-2, -1, -1):
        # 由右到左尋找第一個小於的數組
        if nums[i] < nums[i+1]:
            # 由右到左尋找第一個大於nums[i-1]的數字
            for j in range(len(nums)-1, i, -1):
                if nums[j] > nums[i]:
                    # 將數組做交換
                    nums[i], nums[j] = nums[j], nums[i]
                    break
            nums[i+1:] = reversed(nums[i+1:])
            return
        
    # 若沒找到小於的數組將整組陣列做反轉
    nums.reverse()


def GPTnextPermutation(nums):
    # Step 1: Find the first decreasing element from the end
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    if i >= 0:  # If such element is found
        # Step 2: Find the first element larger than nums[i] from the end
        j = len(nums) - 1
        while nums[j] <= nums[i]:
            j -= 1
        # Step 3: Swap elements at i and j
        nums[i], nums[j] = nums[j], nums[i]

    # Step 4: Reverse the elements from i + 1 to the end
    nums[i + 1:] = reversed(nums[i + 1:])


nextPermutation([1,3,2])

