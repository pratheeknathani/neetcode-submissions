class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        
        position = 0
        total = 0
        for i in range(len(gas)):
            total += (gas[i]-cost[i])
            if total < 0:
                total = 0
                position = i +1
        return position