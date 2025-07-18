class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        starting_station = 0
        tank = 0

        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                starting_station = i+1
                tank = 0
            
        return starting_station
