import math
import time

from solution import Solution


class DynamicProgramming:
    def __init__(self, instance):
        self.instance = instance

        # define DP dictionary with key (machine, machine.available_day) or
        # (None, self.instance.number_of_days + 1)
        # this is defined for memoization
        self._dp = {
            (machine, machine.available_day): None
            for machine in self.instance.machine_list
        }
        self._dp[
            (None, self.instance.number_of_days + 1)
        ] = None  # the only acceptable state for the end of horizon

    def _prev_availabilities(self, day):
        return [
            machine
            for machine in self.instance.machine_list
            if machine.available_day < day
        ]

    def _max_profit(self, machine, day):
        """
        maximum profit obtained from the start of the horizon
        until the end of the given day, if at the end of the day
        we have the given machine on-hand!
        """

        # initial condition (start with no machine)
        if (machine, day) == (None, 0):
            return self.instance.initial_budget

        # previousely calculated (sub-problem is previously solved)
        if self._dp[(machine, day)] is not None:
            return self._dp[(machine, day)]

        # calculate
        compare_list = [self._max_profit(None, 0)]
        for sold_machine in self._prev_availabilities(day):
            compare_list.append(
                self._max_profit(sold_machine, sold_machine.available_day)
                + sold_machine.resell_price
                + sold_machine.daily_profit * (day - sold_machine.available_day - 1)
            )
        max_value = max(compare_list)
        if machine is not None:  # day < self.instance.number_of_days + 1
            max_value -= machine.purchase_price
        self._dp[(machine, day)] = max_value if max_value >= 0 else -math.inf

        return self._dp[(machine, day)]

    def run(self):

        start_time = time.time()
        # check for special cases
        if (
            self.instance.number_of_machines == 0  # no machines to buy
            or self.instance.number_of_days <= 1  # short time horizon
            or all(  # not enough money to buy any of the machines
                machine.purchase_price > self.instance.initial_budget
                for machine in self.instance.machine_list
            )
        ):
            max_profit = self.instance.initial_budget

        else:  # run the algorithm
            max_profit = self._max_profit(None, self.instance.number_of_days + 1)
        solution = Solution(self.instance, max_profit, time.time() - start_time)
        return solution
