def combinationSum2(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    result = []
    candidates.sort()

    def backtrack(remaining, combo, start):
        if remaining == 0:
            if list(combo) not in result:
                result.append(combo[:])
            return
        elif remaining < 0:
            return
        
        for i in range(start, len(candidates)):
            # 跳過重複的元素
            if i > start and candidates[i] == candidates[i - 1]:
                continue

            combo.append(candidates[i])
            backtrack(remaining - candidates[i], combo, i + 1)
            combo.pop()
    
    backtrack(target, [], 0)
    return result

print(combinationSum2([2,5,2,1,2],5))