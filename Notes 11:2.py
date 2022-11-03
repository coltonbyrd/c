#1. Use recursion to calculate the sum of a 
# list of numbers. 
def ListSum(list1):
    if len(list1) == 0:
        return 0
    else:
        return list1[0] + ListSum(list1[1:])
Listsum = (ListSum([1,2,3,4,5,6,7,8,9,10]))
print(Listsum)
#2. Use recursion to calculate the sum of the first n 
# natural numbers.
def NatNums(n):
    if n == 1:
        return 1
    else:
        return n + NatNums(n-1)
Natnums = (NatNums(10))
print(Natnums)
#3. Write a Python program to solve the Fibonacci sequence using recursion. 
def FibSeq(i):
    if i == 1 or i == 2:
        return 1
    else:
        return FibSeq(i-1) + FibSeq(i-2)
Fibseq = FibSeq(10)
print(Fibseq)
#4. Write a Python program to get the sum of a non-negative integer. 
"""Example Test Data:
sumDigits(345) -> 12
sumDigits(45) -> 9"""
def NNegInt(a):
    if a == 0:
        return 0
    else:
        return a % 10 + NNegInt(int(a/10))
Nnegint = NNegInt(50)
print(Nnegint)
#5. Identify what the recursive code below does.
def namefunc(string):
    if len(string) == 0:
        return string
    else:
        return namefunc(string[1:]) + string[0]
# 6. Write a Python program to calculate the sum of the positive integers
# of n+(n-2)+(n-4)... (until n-x =< 0). 
"""Test Data:
sum_series(6) -> 12
sum_series(10) -> 30"""

# 7. Write a Python program to calculate the value of 'a' 
# to the power 'b'. 
"""Test Data :
(power(3,4) -> 81"""

# 8. Write a Python program to find  the greatest common divisor 
# (gcd) of two integers. 
