class Solution:
    def __init__(self, instance, max_profit, run_time):
        self.instance = instance
        self.max_profit = max_profit
        self.run_time = run_time


def print_solutions(solutions):
    run_times = [solution.run_time for solution in solutions]
    print(f"\nAverage run_time: {sum(run_times) / len(run_times) :.2e} seconds")
    print(f"\n{'Instance input':<15} Instance output")
    for s in solutions:
        print(
            f"{s.instance.instance_summary:<15} {s.instance.instance_key + ':':<8} {s.max_profit}"
        )
