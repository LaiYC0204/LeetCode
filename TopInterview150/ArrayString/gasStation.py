class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # 如果汽油比較少花費比較多，不可能開完一圈
        if sum(gas) < sum(cost):
            return -1
        
        current_gas = 0
        start_index = 0

        #一定可以繞完一圈，找尋起始點
        for i in range(len(gas)):
            current_gas += gas[i] - cost[i]
            if current_gas < 0:
                start_index = i + 1
                current_gas = 0

        return start_index

        
gas = [1,2,3,4,5]
costs = [3,4,5,1,2]
s = Solution()
print(s.canCompleteCircuit(gas, costs))
