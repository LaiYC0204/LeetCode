#超暴力解
def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    outputs = []
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                #print(f'i:{i} j:{j} k:{k}')
                if nums[i] + nums[j] + nums[k] == 0:
                    repeat = False
                    triplets = [nums[i], nums[j], nums[k]]
                    for output in outputs:
                        if set(output) == set(triplets):
                            repeat = True
                            break
                    if not repeat:
                        outputs.append(triplets)
    return outputs

#雙指針
def GPTThreeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    nums.sort()  # 排序
    res = []  # 存儲結果的列表
    
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:  # 跳過重複的數字
            continue
        
        left, right = i + 1, len(nums) - 1  # 初始化左右指針
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:  # 如果總和小於零，移動左指針
                left += 1
            elif total > 0:  # 如果總和大於零，移動右指針
                right -= 1
            else:
                res.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:  # 跳過重複的左指針
                    left += 1
                while left < right and nums[right] == nums[right - 1]:  # 跳過重複的右指針
                    right -= 1
                left += 1
                right -= 1
                
    return res


inputs = [[0,1,1],[0,0,0],[-1,0,1,2,-1,-4]]
answers = [[],[[0,0,0]],[[-1,-1,2],[-1,0,1]]]

for i in range(len(inputs)):
    output = threeSum(inputs[i])
    if output != answers[i]:
        print(f'input：{inputs[i]} value：{answers[i]} output：{output}')