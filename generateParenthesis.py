#遞迴
def GPTgenerateParentheses(n):
    """
    :type n: int
    :rtype: List[str]
    """
    results = []
    generate("", 0, 0, n, results)
    return results

def generate(current, left, right, max, results):
    if len(current) == 2 * max:
        results.append(current)
        return
    
    if left < max:
        generate(current + "(", left + 1, right, max, results)
    
    if right < left:
        generate(current + ")", left, right + 1, max, results)

# 範例呼叫
n = 1
print(GPTgenerateParentheses(n))

"""
                          ""
                   /                \
                "("                ""
             /       \            /      \
          "(("      "()"      ...     ...
        /    \     /    \
    "((("   "(()" ...   ... 
     /   \   /  \
 "((()" "((())" ...
  /   \
"((()))" ...

"""
