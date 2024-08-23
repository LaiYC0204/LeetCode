def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    result = []
    n = len(nums)

    def backtrack(combo, remaining):
        if len(combo) == n:
            result.append(combo[:])
            return

        for i in range(len(remaining)):
            combo.append(remaining[i])
            backtrack(combo, remaining[:i] + remaining[i+1:])
            combo.pop()

    backtrack([], nums)
    return result

print(permute([1,1,2]))