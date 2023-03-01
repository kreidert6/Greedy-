# File: test_pa2.py
# Author: John Glick    
# Date: February 20, 2023
# Description: Program that tests the correctness
#              of pa2, comp 480, spring 2023.

import sys
from time import process_time

# import the module containing pa2 solution
from pa2 import pa2

def read_correct_answer(f):
    """
    Reads solution from the opened file f.
    Solution is either "impossible" or two lines,
    each containing an order of items.  If solution is
    an order of items, the solution is not necessarily unique.
    """
    first_line = f.readline().strip()
    if first_line == "impossible":
        return first_line
    else:
        first_line = [int(i) for i in first_line.split()]
        second_line = [int(i) for i in f.readline().strip().split()]
        return first_line, second_line
    
def check_answer(input_filename, your_answer):
    """
    Checks that your answer meets requirements.
    """

    # Read in the input file
    f = open(input_filename)
    n = int(f.readline().strip())
    a_size_1 = [int(i) for i in f.readline().split()]
    a_size_2 = [int(i) for i in f.readline().split()]
    b_size_1 = [int(i) for i in f.readline().split()]
    b_size_2 = [int(i) for i in f.readline().split()]

    # Adjust your answers to the range 0, ..., n -1
    your_ans = [[i - 1 for i in your_answer[0]],
                [i - 1 for i in your_answer[1]]]

    # Check that your answer meets the requirements
    if len(your_ans[0]) != n or len(your_ans[1]) != n:
        return False
    
    for i in range(n - 1):
        if a_size_2[your_ans[0][i]] <= b_size_2[your_ans[1][i]]:
            return False
        if a_size_1[your_ans[0][i]] > a_size_1[your_ans[0][i+1]]:
            return False
        if b_size_1[your_ans[1][i]] > b_size_1[your_ans[1][i+1]]:
            return False
        
    if a_size_2[your_ans[0][n-1]] <= b_size_2[your_ans[1][n-1]]:
            return False
    
    return True

if __name__ == "__main__":

    # Print message
    print("Checking your program.")

    TARGET_RUN_TIME = 150

    # Test short inputs for correctness
    min_text_index = 1
    max_test_index = 17
    num_tests = 0
    num_correct = 0
    incorrect_tests = []
    print(f"Testing small inputs.")
    start_time = process_time()
    for i in range(min_text_index, max_test_index + 1):
        num_tests += 1
        input_filename = f"input{i}.txt"
        print(f"Testing input file {input_filename}")
        solution_filename = f"solution{i}.txt"
        solution_f = open(solution_filename, "r")
        correct_answer = read_correct_answer(solution_f)
        your_answer = pa2(input_filename)
        if your_answer == None:
            if correct_answer == "impossible":
                print("Correct\n")
                num_correct += 1
            else:
                print("Incorrect")
                print(f"Your answer = {your_answer}")
                print(f"Correct answer = {correct_answer}")
                incorrect_tests.append(i)
        else:
            if correct_answer == "impossible":
                print("Incorrect")
                print(f"Your answer = {your_answer}")
                print(f"Correct answer = {correct_answer}")
                incorrect_tests.append(i)
            elif len(your_answer) != 2:
                print("Incorrect.  Length not 2")
                print(f"Your answer = {your_answer}")
                print(f"Correct answer = {correct_answer}")
                incorrect_tests.append(i)
            elif (your_answer[0] == correct_answer[0] and
                your_answer[1] == correct_answer[1]):
                print("Correct\n")
                num_correct += 1
            else: 
                correct = check_answer(input_filename, your_answer)
                if correct:
                    print("Correct\n")
                    num_correct += 1
                else:
                    print("Incorrect.  Does not satisfy requirements")
                    print(f"Your answer = {your_answer}")
                    print(f"Correct answer = {correct_answer}")
                    incorrect_tests.append(i)
    finish_time = process_time()
    run_time = finish_time - start_time

    if num_correct == num_tests:
        print("All short jobs correct.  Nice job!  Now trying long ones.")
        print(f"Running time = {run_time}")
    else:
        print(f"One or more tests incorrect.  Keep working on it.")
        print(f"Indices of incorrect tests = {incorrect_tests}")

    # Test long inputs for correctness
    min_text_index = 18
    max_test_index = 33
    num_tests = 0
    num_correct = 0
    incorrect_tests = []
    print("Testing large inputs")
    print(f"Target sum of run times for all tests is {TARGET_RUN_TIME}")
    start_time = process_time()
    for i in range(min_text_index, max_test_index + 1):
        num_tests += 1
        input_filename = f"input{i}.txt"
        print(f"Testing input file {input_filename}")
        solution_filename = f"solution{i}.txt"
        solution_f = open(solution_filename, "r")
        correct_answer = read_correct_answer(solution_f)
        your_answer = pa2(input_filename)
        if your_answer == None and correct_answer == "impossible":
            print("Correct\n")
            num_correct += 1
        elif len(your_answer) != 2:
            print("Incorrect.  Length not 2")
            print(f"Your answer = {your_answer}")
            print(f"Correct answer = {correct_answer}")
            incorrect_tests.append(i)
        elif (your_answer[0] == correct_answer[0] and
              your_answer[1] == correct_answer[1]):
            print("Correct\n")
            num_correct += 1
        else: 
            correct = check_answer(input_filename, your_answer)
            if correct:
                print("Correct\n")
                num_correct += 1
            else:
                print("Incorrect.  Does not satisfy requirements")
                print(f"Your answer = {your_answer}")
                print(f"Correct answer = {correct_answer}")
                incorrect_tests.append(i)

    finish_time = process_time()
    run_time = finish_time - start_time
    print(f"Your runtime was {run_time}")
    if num_correct == num_tests:
        print("All long jobs correct.")
        if run_time > TARGET_RUN_TIME:
            print("But run time too long.")
        else:
            print("Run time less than target.  Nice job!")
            print("Check your program for style requirements before submtting")
    else:
        print(f"One or more tests incorrect.  Keep working on it.")
        print(f"Indices of incorrect tests = {incorrect_tests}")
