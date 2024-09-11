import collections

def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    dic = {}
    for s in strs:
        sort_word = str(sorted(s))
        if sort_word in dic:
            dic[sort_word].append(s)
        else:
            dic[sort_word] = [s]

    return list(dic.values())

def GPTgroupAnagrams(strs):
    # 訪問一個不存在的鍵時，創建一個空的列表
    anagrams = collections.defaultdict(list)
    
    for s in strs:
        # 使用排序后的字串作為键
        key = tuple(sorted(s))
        anagrams[key].append(s)
    
    return list(anagrams.values())
    
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))