def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    left, right = 0, len(height)-1
    max_water = 0
    while left != right:
        max_water = max(min(height[left], height[right]) * (right - left), max_water)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water

answers = {49:[1,8,6,2,5,4,8,3,7], 1:[1,1]}

for key, value in answers.items():
    output = maxArea(value)
    if output != key:
        print(f'Key: {value}, Value: {key}, Output: {output}')