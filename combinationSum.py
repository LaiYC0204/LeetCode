def combinationSum(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    output = []
    l = []
    generate(candidates, target, output, 0, l)

    return output

def generate(candidates, target, output, current, l):
    if current >= len(candidates):
        return
    
    print(f'l:{l} suml:{sum(l)}')
    if sum(l) == target:
        # 增加切片的list而不是直接增加l，怕之後會更改到l這樣就會全部改掉
        output.append(l[:])
        return
    elif sum(l) > target or current >= len(candidates):
        return

    # 選擇自己
    l.append(candidates[current])
    generate(candidates, target, output, current, l)

    # 選擇下一位，並撤銷選擇當前元素
    l.pop()
    generate(candidates, target, output, current + 1, l)

# 濃縮
def GPTcombinationSum(candidates, target):
    result = []
    
    def backtrack(remaining, combo, start):
        if remaining == 0:
            result.append(list(combo))
            return
        elif remaining < 0:
            return
        
        for i in range(start, len(candidates)):
            combo.append(candidates[i])
            print(f'combo:{combo}', end = ' ')
            backtrack(remaining - candidates[i], combo, i)
            combo.pop()
            print(f'pop combo:{combo}')
    
    backtrack(target, [], 0)
    return result


candidates = [2,3,6,7]
target = 7

print(GPTcombinationSum(candidates, target))