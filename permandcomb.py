import os
import math


def find_perm(n, k):
    """
    Permutation:    n!/(n-k)!
    """
    n_fact = math.factorial(n)
    n_k_fact = math.factorial(n - k)

    return n_fact / n_k_fact


def find_comb(n, k):
    """
    Combination:    n!/k!(n-k)!
    """
    n_fact = math.factorial(n)
    k_fact = math.factorial(k)
    n_k_fact = math.factorial(n - k)

    return n_fact / (k_fact*n_k_fact)


class Test:
    def __init__(self, objects, choices):
        self.num_obj = objects
        self.num_choices = choices
        self.combinations = find_comb(objects, choices)
        self.permutations = find_perm(objects, choices)

        self.print_me()

    def print_me(self):
        print(f"\n{self.num_obj} objects, w/ {self.num_choices} choices: ")
        print(f"\nCombinations: {self.num_obj} choose {self.num_choices} => {self.combinations:,.0f}")
        print(f"Permutations: {self.num_obj} permute {self.num_choices} => {self.permutations:,.0f}")
        print("\n")


if __name__ == "__main__":
    # num_obj = int(input("Select n: "))
    # num_choices = int(input("Select k: "))

    num_obj = 52
    num_choices = 5

    Test(num_obj, num_choices)
