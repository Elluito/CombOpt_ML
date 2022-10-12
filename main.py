from problems import MaximumCliqueProblem
import numpy as np
import pandas as pd
from moead_framework.problem.problem import Problem
from problems import KnapsackProblem

def test():
    instance_file = "250_2.txt"
    kp = KnapsackProblem(number_of_objective=2, instance_file=instance_file)
    solution = kp.generate_random_solution()
    problem = MaximumCliqueProblem(number_of_objective=2, instance_file="struc2vec/datasets/C1000-9.mtx", problem_type="BOMWC")
    rand_solution = problem.generate_random_solution()
    print("Decision vector {}".format(rand_solution.decision_vector))
    print("F values of decision vector {}".format(rand_solution.F))


if __name__ == '__main__':
    test()
