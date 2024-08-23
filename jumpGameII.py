def jump(nums):
    n = len(nums)
    if n <= 1:
        return 0
    
    jumps = 0
    current_end = 0
    farthest = 0
    
    for i in range(n - 1):  # 不需要遍歷到最後一個元素
        farthest = max(farthest, i + nums[i])
        
        # 當到達了當前這一步的最遠位置
        if i == current_end:
            jumps += 1
            current_end = farthest
            
            # 如果我們已經可以到達或超過最後一個位置
            if current_end >= n - 1:
                break
    
    return jumps

print(jump([1,1,1,1]))
