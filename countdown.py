import os


"""
3
12 3
1 2 3 7 9 3 2 1 8 3 2 1
4 2
101 100 99 98
9 6
100 7 6 5 4 3 2 1 100
"""

"""
{
    total: 3,
    data : {
        n_k: [], 
        n_k: [], 
        n_k: []
    }
}
"""


class Solution:
    def __init__(self, filename="countdown_case.txt"):
        self.filename = filename

        self.raw_data = {}
        self.solutions = []

    def print_raw_data(self):
        # print extracted data
        for data, val in self.raw_data.items():
            try:
                for key, v in val.items():
                    print(f"{key}: {v}")
            except AttributeError:
                print(f"{data}: {val}")

    def extract_data(self, new_filename="n/a"):
        if new_filename == "n/a":
            new_filename = self.filename
        # Extract data from txt
        self.raw_data = {"total": 0, "data": {}}
        with open(new_filename, 'r') as in_file:
            total_cases = int(in_file.readline())
            self.raw_data["total"] = total_cases

            for i in range(total_cases):
                n_k = in_file.readline().strip()
                new_array = in_file.readline().strip().split(" ")
                self.raw_data["data"][n_k] = new_array

        return self.raw_data

    def parse_data(self):
        # Solution
        for n_k, arr in self.raw_data["data"].items():
            countdown_cases = 0
            n, k = n_k.split(" ")
            k = int(k)
            for index, element in enumerate(arr):

                if int(element) == k:
                    next_element = k - 1

                    for j in range(index + 1, len(arr)):
                        # print(f"a{arr[j]} {next_element}")
                        if int(arr[j]) == next_element:
                            next_element = next_element - 1
                            if next_element <= 0:
                                countdown_cases += 1
                                break
                        else:
                            break

            self.solutions.append(countdown_cases)

        # print(self.solutions)
        # print(test_case)
        # return solution_list


def solution():
    # Extract data from txt
    test_case = {"total": 0, "data": {}}
    with open("countdown_case.txt", 'r') as in_file:
        total_cases = int(in_file.readline())
        test_case["total"] = total_cases

        for i in range(total_cases):
            n_k = in_file.readline().strip()
            new_array = in_file.readline().strip().split(" ")
            test_case["data"][n_k] = new_array

    # print extracted data
    # for data, val in test_case.items():
    #     try:
    #         for key, v in val.items():
    #             print(f"{key}: {v}")
    #     except AttributeError:
    #         print(f"{data}: {val}")

    # Parse and Solve data
    number_tests = test_case["total"]

    # Solution
    solution_list = []
    for n_k, arr in test_case["data"].items():
        countdown_cases = 0
        n, k = n_k.split(" ")
        k = int(k)
        for index, element in enumerate(arr):

            if int(element) == k:
                next_element = k - 1

                for j in range(index + 1, len(arr)):
                    # print(f"a{arr[j]} {next_element}")
                    if int(arr[j]) == next_element:
                        next_element = next_element - 1
                        if next_element <= 0:
                            countdown_cases += 1
                            break
                    else:
                        break

        solution_list.append(countdown_cases)

    print(solution_list)
    # print(test_case)
    return solution_list


if __name__ == "__main__":
    # print(solution())
    solution_obj = Solution()
    user_file = "countdown_case.txt"
    solution_obj.extract_data(user_file)
    solution_obj.parse_data()
    solution_obj.print_raw_data()

    print(solution_obj.solutions)
