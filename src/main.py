import os
import sys

from algorithm import DynamicProgramming
from instance import get_instance_list
from solution import print_solutions

if __name__ == "__main__":

    if len(sys.argv) == 1:
        raise "Path to the instance file is not provided."

    input_file = sys.argv[1]
    if not os.path.exists(input_file):
        raise "Instance file could not be found."

    instances = get_instance_list(input_file)
    print(f"Successfully received {len(instances)} instance(s).")
    instance_solutions = []
    for instance in instances:
        print(f"Solving {instance.instance_key}.")
        solution = DynamicProgramming(instance).run()
        instance_solutions.append(solution)

    print("All instances are solved. Printing the results.")
    print_solutions(instance_solutions)
    test = 0
