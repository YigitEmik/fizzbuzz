# https://leetcode.com/problems/fizz-buzz/
# Fizz Buzz Problem
def fizzBuzz(lst):
    temp = []
    for a in range(1, lst+1):
        if a % 5 == 0 and a % 3 == 0:
            temp.append("FizzBuzz")
        elif a % 3 == 0:
            temp.append("Fizz")
        elif a % 5 == 0:
            temp.append("Buzz")
        else:
            temp.append(str(a))
    return temp

