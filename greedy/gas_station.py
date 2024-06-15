# https://leetcode.com/problems/gas-station/description/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        fuel_diff = 0
        curr_fuel_stock = curr_start = 0
        for station, (refill, cost) in enumerate(zip(gas, cost)):
            fuel_diff += refill - cost
            curr_fuel_stock += refill - cost
            if curr_fuel_stock < 0:
                curr_fuel_stock, curr_start = 0, station + 1
        return -1 if fuel_diff < 0 else curr_start


def main():
    pass


if __name__ == '__main__':
    main()
