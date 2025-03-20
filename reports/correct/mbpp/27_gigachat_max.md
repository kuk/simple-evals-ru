# mbpp / gigachat-2-max
### 16
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to that returns true if the input string contains sequences of lowercase letters joined with an underscore and false otherwise.

Your code should pass these tests:

assert text_lowercase_underscore("aab_cbbbc")==(True)
assert text_lowercase_underscore("aab_Abbbc")==(False)
assert text_lowercase_underscore("Aaab_abbbc")==(False)

Your response should only contain the code for this function.

def text_lowercase_underscore(text):
    ...


 </pre>
###### answer
<pre> ```python
import re

def text_lowercase_underscore(text):
    pattern = r'^[a-z]+_[a-z]+$'
    return bool(re.fullmatch(pattern, text))
``` </pre>
###### canonical_solution
<pre> import re
def text_lowercase_underscore(text):
        patterns = '^[a-z]+_[a-z]+$'
        if re.search(patterns,  text):
                return True
        else:
                return False </pre>
###### test
<pre> assert text_lowercase_underscore("aab_cbbbc")==(True)
assert text_lowercase_underscore("aab_Abbbc")==(False)
assert text_lowercase_underscore("Aaab_abbbc")==(False) </pre>
### 424
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to extract only the rear index element of each string in the given tuple.

Your code should pass these tests:

assert extract_rear(('Mers', 'for', 'Vers') ) == ['s', 'r', 's']
assert extract_rear(('Avenge', 'for', 'People') ) == ['e', 'r', 'e']
assert extract_rear(('Gotta', 'get', 'go') ) == ['a', 't', 'o']

Your response should only contain the code for this function.

def extract_rear(test_tuple):
    ...


 </pre>
###### answer
<pre> ```python
def extract_rear(test_tuple):
    return [string[-1] for string in test_tuple]
``` </pre>
###### canonical_solution
<pre> def extract_rear(test_tuple):
  res = list(sub[len(sub) - 1] for sub in test_tuple)
  return (res)  </pre>
###### test
<pre> assert extract_rear(('Mers', 'for', 'Vers') ) == ['s', 'r', 's']
assert extract_rear(('Avenge', 'for', 'People') ) == ['e', 'r', 'e']
assert extract_rear(('Gotta', 'get', 'go') ) == ['a', 't', 'o'] </pre>
### 435
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a python function to find the last digit of a given number.

Your code should pass these tests:

assert last_Digit(123) == 3
assert last_Digit(25) == 5
assert last_Digit(30) == 0

Your response should only contain the code for this function.

def last_Digit(n) :
    ...


 </pre>
###### answer
<pre> ```python
def last_Digit(n):
    return n % 10
``` </pre>
###### canonical_solution
<pre> def last_Digit(n) :
    return (n % 10)  </pre>
###### test
<pre> assert last_Digit(123) == 3
assert last_Digit(25) == 5
assert last_Digit(30) == 0 </pre>
### 245
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function that takes an array and finds the maximum sum of a bitonic subsequence for the given array, where a sequence is bitonic if it is first increasing and then decreasing.

Your code should pass these tests:

assert max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9]) == 194
assert max_sum([80, 60, 30, 40, 20, 10]) == 210
assert max_sum([2, 3 ,14, 16, 21, 23, 29, 30]) == 138

Your response should only contain the code for this function.

def max_sum(arr): 
    ...


 </pre>
###### answer
<pre> ```python
def max_sum(arr):
    n = len(arr)
    
    # Initialize two arrays to store sums
    inc = [arr[i] for i in range(n)]   # Maximum sum ending at arr[i]
    dec = [arr[i] for i in range(n)]   # Maximum sum starting from arr[i]
    
    # Compute increasing subsequences (from left to right)
    for i in range(1, n):
        for j in range(i):
            if arr[j] &lt; arr[i]:
                inc[i] = max(inc[i], inc[j] + arr[i])
                
    # Compute decreasing subsequences (from right to left)
    for i in reversed(range(n-1)):
        for j in reversed(range(i+1,n)):
            if arr[j] &lt; arr[i]:
                dec[i] = max(dec[i], dec[j] + arr[i])
    
    # Find the maximum possible sum by combining both sequences
    result = float('-inf')
    for i in range(n):
        result = max(result, inc[i]+dec[i]-arr[i])
        
    return result
```

This implementation computes the maximum sum of a bitonic subsequence using dynamic programming techniques. </pre>
###### canonical_solution
<pre> def max_sum(arr): 
	MSIBS = arr[:] 
	for i in range(len(arr)): 
		for j in range(0, i): 
			if arr[i] > arr[j] and MSIBS[i] &lt; MSIBS[j] + arr[i]: 
				MSIBS[i] = MSIBS[j] + arr[i] 
	MSDBS = arr[:] 
	for i in range(1, len(arr) + 1): 
		for j in range(1, i): 
			if arr[-i] > arr[-j] and MSDBS[-i] &lt; MSDBS[-j] + arr[-i]: 
				MSDBS[-i] = MSDBS[-j] + arr[-i] 
	max_sum = float("-Inf") 
	for i, j, k in zip(MSIBS, MSDBS, arr): 
		max_sum = max(max_sum, i + j - k) 
	return max_sum </pre>
###### test
<pre> assert max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9]) == 194
assert max_sum([80, 60, 30, 40, 20, 10]) == 210
assert max_sum([2, 3 ,14, 16, 21, 23, 29, 30]) == 138 </pre>
### 63
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to find the maximum difference between available pairs in the given tuple list.

Your code should pass these tests:

assert max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]) == 7
assert max_difference([(4, 6), (2, 17), (9, 13), (11, 12)]) == 15
assert max_difference([(12, 35), (21, 27), (13, 23), (41, 22)]) == 23

Your response should only contain the code for this function.

def max_difference(test_list):
    ...


 </pre>
###### answer
<pre> ```python
def max_difference(test_list):
    return max(abs(a-b) for a,b in test_list)
``` </pre>
###### canonical_solution
<pre> def max_difference(test_list):
  temp = [abs(b - a) for a, b in test_list]
  res = max(temp)
  return (res)  </pre>
###### test
<pre> assert max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]) == 7
assert max_difference([(4, 6), (2, 17), (9, 13), (11, 12)]) == 15
assert max_difference([(12, 35), (21, 27), (13, 23), (41, 22)]) == 23 </pre>
### 106
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to append the given list to the given tuples.

Your code should pass these tests:

assert add_lists([5, 6, 7], (9, 10)) == (9, 10, 5, 6, 7)
assert add_lists([6, 7, 8], (10, 11)) == (10, 11, 6, 7, 8)
assert add_lists([7, 8, 9], (11, 12)) == (11, 12, 7, 8, 9)

Your response should only contain the code for this function.

def add_lists(test_list, test_tup):
    ...


 </pre>
###### answer
<pre> ```python
def add_lists(test_list, test_tup):
    return test_tup + tuple(test_list)
``` </pre>
###### canonical_solution
<pre> def add_lists(test_list, test_tup):
  res = tuple(list(test_tup) + test_list)
  return (res)  </pre>
###### test
<pre> assert add_lists([5, 6, 7], (9, 10)) == (9, 10, 5, 6, 7)
assert add_lists([6, 7, 8], (10, 11)) == (10, 11, 6, 7, 8)
assert add_lists([7, 8, 9], (11, 12)) == (11, 12, 7, 8, 9) </pre>
### 300
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to find the count of all binary sequences of length 2n such that sum of first n bits is same as sum of last n bits.

Your code should pass these tests:

import math

assert math.isclose(count_binary_seq(1), 2.0, rel_tol=0.001)
assert math.isclose(count_binary_seq(2), 6.0, rel_tol=0.001)
assert math.isclose(count_binary_seq(3), 20.0, rel_tol=0.001)

Your response should only contain the code for this function.

def count_binary_seq(n): 
    ...


 </pre>
###### answer
<pre> ```python
from math import comb

def count_binary_seq(n):
    total = 0
    
    # Iterate over possible sums from 0 to n (inclusive).
    for k in range(n + 1):
        # Calculate combinations for both halves having 'k' ones.
        c = comb(n, k)
        
        # Multiply by itself since we need matching counts on both sides.
        total += c * c
    
    return float(total)
```

This implementation uses combinatorics (`comb`) to calculate how many ways there are to distribute `k` ones among `n` positions twice—once for each half of the sequence—and then sums up those possibilities across all valid values of `k`. </pre>
###### canonical_solution
<pre> def count_binary_seq(n): 
	nCr = 1
	res = 1
	for r in range(1, n + 1): 
		nCr = (nCr * (n + 1 - r)) / r 
		res += nCr * nCr 
	return res  </pre>
###### test
<pre> import math

assert math.isclose(count_binary_seq(1), 2.0, rel_tol=0.001)
assert math.isclose(count_binary_seq(2), 6.0, rel_tol=0.001)
assert math.isclose(count_binary_seq(3), 20.0, rel_tol=0.001) </pre>
### 425
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to count the number of sublists containing a particular element.

Your code should pass these tests:

assert count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]],1)==3
assert count_element_in_list([['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']],'A')==3
assert count_element_in_list([['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']],'E')==1

Your response should only contain the code for this function.

def count_element_in_list(list1, x): 
    ...


 </pre>
###### answer
<pre> ```python
def count_element_in_list(list_of_lists, target):
    return sum(1 for lst in list_of_lists if target in lst)
``` </pre>
###### canonical_solution
<pre> def count_element_in_list(list1, x): 
    ctr = 0
    for i in range(len(list1)): 
        if x in list1[i]: 
            ctr+= 1          
    return ctr </pre>
###### test
<pre> assert count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]],1)==3
assert count_element_in_list([['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']],'A')==3
assert count_element_in_list([['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']],'E')==1 </pre>
### 455
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to check whether the given month number contains 31 days or not.

Your code should pass these tests:

assert check_monthnumb_number(5)==True
assert check_monthnumb_number(2)==False
assert check_monthnumb_number(6)==False

Your response should only contain the code for this function.

def check_monthnumb_number(monthnum2):
    ...


 </pre>
###### answer
<pre> ```python
def check_monthnumb_number(monthnum2):
    if monthnum2 in [1, 3, 5, 7, 8, 10, 12]:
        return True
    else:
        return False
``` </pre>
###### canonical_solution
<pre> def check_monthnumb_number(monthnum2):
  if(monthnum2==1 or monthnum2==3 or monthnum2==5 or monthnum2==7 or monthnum2==8 or monthnum2==10 or monthnum2==12):
    return True
  else:
    return False </pre>
###### test
<pre> assert check_monthnumb_number(5)==True
assert check_monthnumb_number(2)==False
assert check_monthnumb_number(6)==False </pre>
### 252
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a python function to convert complex numbers to polar coordinates.

Your code should pass these tests:

assert convert(1) == (1.0, 0.0)
assert convert(4) == (4.0,0.0)
assert convert(5) == (5.0,0.0)

Your response should only contain the code for this function.

def convert(numbers):    
    ...


 </pre>
###### answer
<pre> ```python
import cmath

def convert(number):
    return abs(number), cmath.phase(complex(number))
``` </pre>
###### canonical_solution
<pre> import cmath  
def convert(numbers):    
  num = cmath.polar(numbers)  
  return (num)  </pre>
###### test
<pre> assert convert(1) == (1.0, 0.0)
assert convert(4) == (4.0,0.0)
assert convert(5) == (5.0,0.0) </pre>
