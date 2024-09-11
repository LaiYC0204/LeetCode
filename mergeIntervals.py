def merge(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: List[List[int]]
    """
    # 以intervals[0]為基準排序陣列
    intervals.sort(key=lambda x: x[0])
    i = 1
    
    while i < len(intervals):
        if intervals[i][0] <= intervals[i-1][1]: # 判斷是否重疊
            if intervals[i-1][1] <= intervals[i][1]: # 合併區間
                intervals[i] = [intervals[i-1][0], intervals[i][1]]
            else:
                intervals[i] = [intervals[i-1][0], intervals[i-1][1]]
            intervals.pop(i-1) # 刪除已合併的前一個區間
        else:
            i += 1 # 移動指針到下一個區間

    return intervals

def GPTmerge(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: List[List[int]]
    """
    intervals.sort(key=lambda x: x[0])
    i = 1

    while i < len(intervals):
        if intervals[i][0] <= intervals[i-1][1]:  # 判斷是否重疊
            # 合併區間
            intervals[i] = [intervals[i-1][0], max(intervals[i-1][1], intervals[i][1])]
            intervals.pop(i-1)  # 刪除已合併的前一個區間
        else:
            i += 1  # 移動指針到下一個區間

    return intervals

print(GPTmerge([[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]))