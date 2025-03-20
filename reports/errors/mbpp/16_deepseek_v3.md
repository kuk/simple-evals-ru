# mbpp / deepseek-v3
### 311
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a python function to set the left most unset bit.

Your code should pass these tests:

assert set_left_most_unset_bit(10) == 14
assert set_left_most_unset_bit(12) == 14
assert set_left_most_unset_bit(15) == 15

Your response should only contain the code for this function.

def set_left_most_unset_bit(n): 
    ...


 </pre>
###### answer
<pre> ```python
def set_left_most_unset_bit(n):
    if n == 0:
        return 1
    mask = 1
    while mask &lt;= n:
        if (n & mask) == 0:
            return n | mask
        mask &lt;&lt;= 1
    return n
``` </pre>
###### canonical_solution
<pre> def set_left_most_unset_bit(n): 
    if not (n & (n + 1)): 
        return n 
    pos, temp, count = 0, n, 0 
    while temp: 
        if not (temp & 1): 
            pos = count      
        count += 1; temp>>=1
    return (n | (1 &lt;&lt; (pos)))  </pre>
###### test
<pre> assert set_left_most_unset_bit(10) == 14
assert set_left_most_unset_bit(12) == 14
assert set_left_most_unset_bit(15) == 15 </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 18
     14         mask &lt;&lt;= 1
     15     return n
---> 18 assert set_left_most_unset_bit(10) == 14
     19 assert set_left_most_unset_bit(12) == 14
     20 assert set_left_most_unset_bit(15) == 15
AssertionError:  </pre>
### 248
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function that takes in an integer n and calculates the harmonic sum of n-1.

Your code should pass these tests:

import math

assert math.isclose(harmonic_sum(7), 2.5928571428571425, rel_tol=0.001)
assert math.isclose(harmonic_sum(4), 2.083333333333333, rel_tol=0.001)
assert math.isclose(harmonic_sum(19), 3.547739657143682, rel_tol=0.001)

Your response should only contain the code for this function.

def harmonic_sum(n):
    ...


 </pre>
###### answer
<pre> ```python
def harmonic_sum(n):
    total = 0.0
    for i in range(1, n):
        total += 1.0 / i
    return total
``` </pre>
###### canonical_solution
<pre> def harmonic_sum(n):
  if n &lt; 2:
    return 1
  else:
    return 1 / n + (harmonic_sum(n - 1))  </pre>
###### test
<pre> import math

assert math.isclose(harmonic_sum(7), 2.5928571428571425, rel_tol=0.001)
assert math.isclose(harmonic_sum(4), 2.083333333333333, rel_tol=0.001)
assert math.isclose(harmonic_sum(19), 3.547739657143682, rel_tol=0.001) </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 16
     11     return total
     14 import math
---> 16 assert math.isclose(harmonic_sum(7), 2.5928571428571425, rel_tol=0.001)
     17 assert math.isclose(harmonic_sum(4), 2.083333333333333, rel_tol=0.001)
     18 assert math.isclose(harmonic_sum(19), 3.547739657143682, rel_tol=0.001)
AssertionError:  </pre>
### 306
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to find the maximum sum of increasing subsequence from prefix until ith index and also including a given kth element which is after i, i.e., k > i .

Your code should pass these tests:

assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6) == 11
assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 2, 5) == 7
assert max_sum_increasing_subseq([11, 15, 19, 21, 26, 28, 31], 7, 2, 4) == 71

Your response should only contain the code for this function.

def max_sum_increasing_subseq(a, n, index, k):
    ...


 </pre>
###### answer
<pre> ```python
def max_sum_increasing_subseq(a, n, index, k):
    # Initialize a list to store the maximum sum of increasing subsequence up to each index
    dp = [0] * n
    dp[0] = a[0]
    
    # Fill the dp array up to the index
    for i in range(1, index):
        dp[i] = a[i]
        for j in range(i):
            if a[j] &lt; a[i]:
                dp[i] = max(dp[i], dp[j] + a[i])
    
    # Now, include the kth element and continue the subsequence
    # Initialize the sum with the kth element
    max_sum = a[k]
    
    # Iterate through the elements up to the index to find the maximum sum
    for i in range(index):
        if a[i] &lt; a[k]:
            max_sum = max(max_sum, dp[i] + a[k])
    
    return max_sum
``` </pre>
###### canonical_solution
<pre> def max_sum_increasing_subseq(a, n, index, k):
	dp = [[0 for i in range(n)] 
			for i in range(n)]
	for i in range(n):
		if a[i] > a[0]:
			dp[0][i] = a[i] + a[0]
		else:
			dp[0][i] = a[i]
	for i in range(1, n):
		for j in range(n):
			if a[j] > a[i] and j > i:
				if dp[i - 1][i] + a[j] > dp[i - 1][j]:
					dp[i][j] = dp[i - 1][i] + a[j]
				else:
					dp[i][j] = dp[i - 1][j]
			else:
				dp[i][j] = dp[i - 1][j]
	return dp[index][k] </pre>
###### test
<pre> assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6) == 11
assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 2, 5) == 7
assert max_sum_increasing_subseq([11, 15, 19, 21, 26, 28, 31], 7, 2, 4) == 71 </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 32
     28     return max_sum
     31 assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6) == 11
---> 32 assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 2, 5) == 7
     33 assert max_sum_increasing_subseq([11, 15, 19, 21, 26, 28, 31], 7, 2, 4) == 71
AssertionError:  </pre>
### 462
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to find all possible combinations of the elements of a given list.

Your code should pass these tests:

assert combinations_list(['orange', 'red', 'green', 'blue'])==[[], ['orange'], ['red'], ['red', 'orange'], ['green'], ['green', 'orange'], ['green', 'red'], ['green', 'red', 'orange'], ['blue'], ['blue', 'orange'], ['blue', 'red'], ['blue', 'red', 'orange'], ['blue', 'green'], ['blue', 'green', 'orange'], ['blue', 'green', 'red'], ['blue', 'green', 'red', 'orange']]
assert combinations_list(['red', 'green', 'blue', 'white', 'black', 'orange'])==[[], ['red'], ['green'], ['green', 'red'], ['blue'], ['blue', 'red'], ['blue', 'green'], ['blue', 'green', 'red'], ['white'], ['white', 'red'], ['white', 'green'], ['white', 'green', 'red'], ['white', 'blue'], ['white', 'blue', 'red'], ['white', 'blue', 'green'], ['white', 'blue', 'green', 'red'], ['black'], ['black', 'red'], ['black', 'green'], ['black', 'green', 'red'], ['black', 'blue'], ['black', 'blue', 'red'], ['black', 'blue', 'green'], ['black', 'blue', 'green', 'red'], ['black', 'white'], ['black', 'white', 'red'], ['black', 'white', 'green'], ['black', 'white', 'green', 'red'], ['black', 'white', 'blue'], ['black', 'white', 'blue', 'red'], ['black', 'white', 'blue', 'green'], ['black', 'white', 'blue', 'green', 'red'], ['orange'], ['orange', 'red'], ['orange', 'green'], ['orange', 'green', 'red'], ['orange', 'blue'], ['orange', 'blue', 'red'], ['orange', 'blue', 'green'], ['orange', 'blue', 'green', 'red'], ['orange', 'white'], ['orange', 'white', 'red'], ['orange', 'white', 'green'], ['orange', 'white', 'green', 'red'], ['orange', 'white', 'blue'], ['orange', 'white', 'blue', 'red'], ['orange', 'white', 'blue', 'green'], ['orange', 'white', 'blue', 'green', 'red'], ['orange', 'black'], ['orange', 'black', 'red'], ['orange', 'black', 'green'], ['orange', 'black', 'green', 'red'], ['orange', 'black', 'blue'], ['orange', 'black', 'blue', 'red'], ['orange', 'black', 'blue', 'green'], ['orange', 'black', 'blue', 'green', 'red'], ['orange', 'black', 'white'], ['orange', 'black', 'white', 'red'], ['orange', 'black', 'white', 'green'], ['orange', 'black', 'white', 'green', 'red'], ['orange', 'black', 'white', 'blue'], ['orange', 'black', 'white', 'blue', 'red'], ['orange', 'black', 'white', 'blue', 'green'], ['orange', 'black', 'white', 'blue', 'green', 'red']]
assert combinations_list(['red', 'green', 'black', 'orange'])==[[], ['red'], ['green'], ['green', 'red'], ['black'], ['black', 'red'], ['black', 'green'], ['black', 'green', 'red'], ['orange'], ['orange', 'red'], ['orange', 'green'], ['orange', 'green', 'red'], ['orange', 'black'], ['orange', 'black', 'red'], ['orange', 'black', 'green'], ['orange', 'black', 'green', 'red']]

Your response should only contain the code for this function.

def combinations_list(list1):
    ...


 </pre>
###### answer
<pre> ```python
def combinations_list(list1):
    from itertools import combinations
    
    result = []
    for r in range(len(list1) + 1):
        for combo in combinations(list1, r):
            result.append(list(combo))
    return result
``` </pre>
###### canonical_solution
<pre> def combinations_list(list1):
    if len(list1) == 0:
        return [[]]
    result = []
    for el in combinations_list(list1[1:]):
        result += [el, el+[list1[0]]]
    return result </pre>
###### test
<pre> assert combinations_list(['orange', 'red', 'green', 'blue'])==[[], ['orange'], ['red'], ['red', 'orange'], ['green'], ['green', 'orange'], ['green', 'red'], ['green', 'red', 'orange'], ['blue'], ['blue', 'orange'], ['blue', 'red'], ['blue', 'red', 'orange'], ['blue', 'green'], ['blue', 'green', 'orange'], ['blue', 'green', 'red'], ['blue', 'green', 'red', 'orange']]
assert combinations_list(['red', 'green', 'blue', 'white', 'black', 'orange'])==[[], ['red'], ['green'], ['green', 'red'], ['blue'], ['blue', 'red'], ['blue', 'green'], ['blue', 'green', 'red'], ['white'], ['white', 'red'], ['white', 'green'], ['white', 'green', 'red'], ['white', 'blue'], ['white', 'blue', 'red'], ['white', 'blue', 'green'], ['white', 'blue', 'green', 'red'], ['black'], ['black', 'red'], ['black', 'green'], ['black', 'green', 'red'], ['black', 'blue'], ['black', 'blue', 'red'], ['black', 'blue', 'green'], ['black', 'blue', 'green', 'red'], ['black', 'white'], ['black', 'white', 'red'], ['black', 'white', 'green'], ['black', 'white', 'green', 'red'], ['black', 'white', 'blue'], ['black', 'white', 'blue', 'red'], ['black', 'white', 'blue', 'green'], ['black', 'white', 'blue', 'green', 'red'], ['orange'], ['orange', 'red'], ['orange', 'green'], ['orange', 'green', 'red'], ['orange', 'blue'], ['orange', 'blue', 'red'], ['orange', 'blue', 'green'], ['orange', 'blue', 'green', 'red'], ['orange', 'white'], ['orange', 'white', 'red'], ['orange', 'white', 'green'], ['orange', 'white', 'green', 'red'], ['orange', 'white', 'blue'], ['orange', 'white', 'blue', 'red'], ['orange', 'white', 'blue', 'green'], ['orange', 'white', 'blue', 'green', 'red'], ['orange', 'black'], ['orange', 'black', 'red'], ['orange', 'black', 'green'], ['orange', 'black', 'green', 'red'], ['orange', 'black', 'blue'], ['orange', 'black', 'blue', 'red'], ['orange', 'black', 'blue', 'green'], ['orange', 'black', 'blue', 'green', 'red'], ['orange', 'black', 'white'], ['orange', 'black', 'white', 'red'], ['orange', 'black', 'white', 'green'], ['orange', 'black', 'white', 'green', 'red'], ['orange', 'black', 'white', 'blue'], ['orange', 'black', 'white', 'blue', 'red'], ['orange', 'black', 'white', 'blue', 'green'], ['orange', 'black', 'white', 'blue', 'green', 'red']]
assert combinations_list(['red', 'green', 'black', 'orange'])==[[], ['red'], ['green'], ['green', 'red'], ['black'], ['black', 'red'], ['black', 'green'], ['black', 'green', 'red'], ['orange'], ['orange', 'red'], ['orange', 'green'], ['orange', 'green', 'red'], ['orange', 'black'], ['orange', 'black', 'red'], ['orange', 'black', 'green'], ['orange', 'black', 'green', 'red']] </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 17
     13             result.append(list(combo))
     14     return result
---> 17 assert combinations_list(['orange', 'red', 'green', 'blue'])==[[], ['orange'], ['red'], ['red', 'orange'], ['green'], ['green', 'orange'], ['green', 'red'], ['green', 'red', 'orange'], ['blue'], ['blue', 'orange'], ['blue', 'red'], ['blue', 'red', 'orange'], ['blue', 'green'], ['blue', 'green', 'orange'], ['blue', 'green', 'red'], ['blue', 'green', 'red', 'orange']]
     18 assert combinations_list(['red', 'green', 'blue', 'white', 'black', 'orange'])==[[], ['red'], ['green'], ['green', 'red'], ['blue'], ['blue', 'red'], ['blue', 'green'], ['blue', 'green', 'red'], ['white'], ['white', 'red'], ['white', 'green'], ['white', 'green', 'red'], ['white', 'blue'], ['white', 'blue', 'red'], ['white', 'blue', 'green'], ['white', 'blue', 'green', 'red'], ['black'], ['black', 'red'], ['black', 'green'], ['black', 'green', 'red'], ['black', 'blue'], ['black', 'blue', 'red'], ['black', 'blue', 'green'], ['black', 'blue', 'green', 'red'], ['black', 'white'], ['black', 'white', 'red'], ['black', 'white', 'green'], ['black', 'white', 'green', 'red'], ['black', 'white', 'blue'], ['black', 'white', 'blue', 'red'], ['black', 'white', 'blue', 'green'], ['black', 'white', 'blue', 'green', 'red'], ['orange'], ['orange', 'red'], ['orange', 'green'], ['orange', 'green', 'red'], ['orange', 'blue'], ['orange', 'blue', 'red'], ['orange', 'blue', 'green'], ['orange', 'blue', 'green', 'red'], ['orange', 'white'], ['orange', 'white', 'red'], ['orange', 'white', 'green'], ['orange', 'white', 'green', 'red'], ['orange', 'white', 'blue'], ['orange', 'white', 'blue', 'red'], ['orange', 'white', 'blue', 'green'], ['orange', 'white', 'blue', 'green', 'red'], ['orange', 'black'], ['orange', 'black', 'red'], ['orange', 'black', 'green'], ['orange', 'black', 'green', 'red'], ['orange', 'black', 'blue'], ['orange', 'black', 'blue', 'red'], ['orange', 'black', 'blue', 'green'], ['orange', 'black', 'blue', 'green', 'red'], ['orange', 'black', 'white'], ['orange', 'black', 'white', 'red'], ['orange', 'black', 'white', 'green'], ['orange', 'black', 'white', 'green', 'red'], ['orange', 'black', 'white', 'blue'], ['orange', 'black', 'white', 'blue', 'red'], ['orange', 'black', 'white', 'blue', 'green'], ['orange', 'black', 'white', 'blue', 'green', 'red']]
     19 assert combinations_list(['red', 'green', 'black', 'orange'])==[[], ['red'], ['green'], ['green', 'red'], ['black'], ['black', 'red'], ['black', 'green'], ['black', 'green', 'red'], ['orange'], ['orange', 'red'], ['orange', 'green'], ['orange', 'green', 'red'], ['orange', 'black'], ['orange', 'black', 'red'], ['orange', 'black', 'green'], ['orange', 'black', 'green', 'red']]
AssertionError:  </pre>
### 138
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a python function to check whether the given number can be represented as sum of non-zero powers of 2 or not.

Your code should pass these tests:

assert is_Sum_Of_Powers_Of_Two(10) == True
assert is_Sum_Of_Powers_Of_Two(7) == False
assert is_Sum_Of_Powers_Of_Two(14) == True

Your response should only contain the code for this function.

def is_Sum_Of_Powers_Of_Two(n): 
    ...


 </pre>
###### answer
<pre> ```python
def is_Sum_Of_Powers_Of_Two(n):
    if n == 0:
        return False
    while n > 0:
        if n % 2 == 1:
            n -= 1
        else:
            n = n // 2
        if n == 0:
            return True
    return False
``` </pre>
###### canonical_solution
<pre> def is_Sum_Of_Powers_Of_Two(n): 
    if (n % 2 == 1): 
        return False
    else: 
        return True </pre>
###### test
<pre> assert is_Sum_Of_Powers_Of_Two(10) == True
assert is_Sum_Of_Powers_Of_Two(7) == False
assert is_Sum_Of_Powers_Of_Two(14) == True </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 21
     17     return False
     20 assert is_Sum_Of_Powers_Of_Two(10) == True
---> 21 assert is_Sum_Of_Powers_Of_Two(7) == False
     22 assert is_Sum_Of_Powers_Of_Two(14) == True
AssertionError:  </pre>
### 264
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to calculate a dog's age in dog's years.

Your code should pass these tests:

assert dog_age(12)==61
assert dog_age(15)==73
assert dog_age(24)==109

Your response should only contain the code for this function.

def dog_age(h_age):
    ...


 </pre>
###### answer
<pre> ```python
def dog_age(h_age):
    if h_age &lt;= 0:
        return 0
    elif h_age == 1:
        return 15
    elif h_age == 2:
        return 24
    else:
        return 24 + (h_age - 2) * 5
``` </pre>
###### canonical_solution
<pre> def dog_age(h_age):
 if h_age &lt; 0:
 	exit()
 elif h_age &lt;= 2:
	 d_age = h_age * 10.5
 else:
	 d_age = 21 + (h_age - 2)*4
 return d_age </pre>
###### test
<pre> assert dog_age(12)==61
assert dog_age(15)==73
assert dog_age(24)==109 </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 18
     14     else:
     15         return 24 + (h_age - 2) * 5
---> 18 assert dog_age(12)==61
     19 assert dog_age(15)==73
     20 assert dog_age(24)==109
AssertionError:  </pre>
### 126
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a python function to find the sum of common divisors of two given numbers.

Your code should pass these tests:

assert sum(10,15) == 6
assert sum(100,150) == 93
assert sum(4,6) == 3

Your response should only contain the code for this function.

def sum(a,b): 
    ...


 </pre>
###### answer
<pre> ```python
def sum(a, b):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    
    def get_divisors(n):
        divisors = set()
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                divisors.add(i)
                divisors.add(n // i)
        return divisors
    
    gcd_val = gcd(a, b)
    divisors = get_divisors(gcd_val)
    return sum(divisors)
``` </pre>
###### canonical_solution
<pre> def sum(a,b): 
    sum = 0
    for i in range (1,min(a,b)): 
        if (a % i == 0 and b % i == 0): 
            sum += i 
    return sum </pre>
###### test
<pre> assert sum(10,15) == 6
assert sum(100,150) == 93
assert sum(4,6) == 3 </pre>
###### traceback
<pre> ---------------------------------------------------------------------------TypeError                                 Traceback (most recent call last)Cell In[1], line 26
     22     divisors = get_divisors(gcd_val)
     23     return sum(divisors)
---> 26 assert sum(10,15) == 6
     27 assert sum(100,150) == 93
     28 assert sum(4,6) == 3
Cell In[1], line 23, in sum(a, b)
     21 gcd_val = gcd(a, b)
     22 divisors = get_divisors(gcd_val)
---> 23 return sum(divisors)
TypeError: sum() missing 1 required positional argument: 'b' </pre>
### 400
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to extract the number of unique tuples in the given list.

Your code should pass these tests:

assert extract_freq([(3, 4), (1, 2), (4, 3), (5, 6)] ) == 3
assert extract_freq([(4, 15), (2, 3), (5, 4), (6, 7)] ) == 4
assert extract_freq([(5, 16), (2, 3), (6, 5), (6, 9)] ) == 4

Your response should only contain the code for this function.

def extract_freq(test_list):
    ...


 </pre>
###### answer
<pre> ```python
def extract_freq(test_list):
    return len(set(test_list))
``` </pre>
###### canonical_solution
<pre> def extract_freq(test_list):
  res = len(list(set(tuple(sorted(sub)) for sub in test_list)))
  return (res) </pre>
###### test
<pre> assert extract_freq([(3, 4), (1, 2), (4, 3), (5, 6)] ) == 3
assert extract_freq([(4, 15), (2, 3), (5, 4), (6, 7)] ) == 4
assert extract_freq([(5, 16), (2, 3), (6, 5), (6, 9)] ) == 4 </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 11
      7 def extract_freq(test_list):
      8     return len(set(test_list))
---> 11 assert extract_freq([(3, 4), (1, 2), (4, 3), (5, 6)] ) == 3
     12 assert extract_freq([(4, 15), (2, 3), (5, 4), (6, 7)] ) == 4
     13 assert extract_freq([(5, 16), (2, 3), (6, 5), (6, 9)] ) == 4
AssertionError:  </pre>
### 143
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to find number of lists present in the given tuple.

Your code should pass these tests:

assert find_lists(([1, 2, 3, 4], [5, 6, 7, 8])) == 2
assert find_lists(([1, 2], [3, 4], [5, 6]))  == 3
assert find_lists(([9, 8, 7, 6, 5, 4, 3, 2, 1])) == 1

Your response should only contain the code for this function.

def find_lists(Input): 
    ...


 </pre>
###### answer
<pre> ```python
def find_lists(Input):
    return sum(isinstance(element, list) for element in Input)
``` </pre>
###### canonical_solution
<pre> def find_lists(Input): 
	if isinstance(Input, list): 
		return 1
	else: 
		return len(Input)  </pre>
###### test
<pre> assert find_lists(([1, 2, 3, 4], [5, 6, 7, 8])) == 2
assert find_lists(([1, 2], [3, 4], [5, 6]))  == 3
assert find_lists(([9, 8, 7, 6, 5, 4, 3, 2, 1])) == 1 </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 13
     11 assert find_lists(([1, 2, 3, 4], [5, 6, 7, 8])) == 2
     12 assert find_lists(([1, 2], [3, 4], [5, 6]))  == 3
---> 13 assert find_lists(([9, 8, 7, 6, 5, 4, 3, 2, 1])) == 1
AssertionError:  </pre>
### 83
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a python function to find the character made by adding the ASCII value of all the characters of the given string modulo 26.

Your code should pass these tests:

assert get_Char("abc") == "f"
assert get_Char("gfg") == "t"
assert get_Char("ab") == "c"

Your response should only contain the code for this function.

def get_Char(strr):  
    ...


 </pre>
###### answer
<pre> ```python
def get_Char(strr):
    total = 0
    for char in strr:
        total += ord(char)
    return chr((total % 26) + ord('a'))
``` </pre>
###### canonical_solution
<pre> def get_Char(strr):  
    summ = 0
    for i in range(len(strr)): 
        summ += (ord(strr[i]) - ord('a') + 1)  
    if (summ % 26 == 0): 
        return ord('z') 
    else: 
        summ = summ % 26
        return chr(ord('a') + summ - 1) </pre>
###### test
<pre> assert get_Char("abc") == "f"
assert get_Char("gfg") == "t"
assert get_Char("ab") == "c" </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 14
     10         total += ord(char)
     11     return chr((total % 26) + ord('a'))
---> 14 assert get_Char("abc") == "f"
     15 assert get_Char("gfg") == "t"
     16 assert get_Char("ab") == "c"
AssertionError:  </pre>
### 229
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function that takes in an array and an integer n, and re-arranges the first n elements of the given array so that all negative elements appear before positive ones, and where the relative order among negative and positive elements is preserved.

Your code should pass these tests:

assert re_arrange_array([-1, 2, -3, 4, 5, 6, -7, 8, 9], 9) == [-1, -3, -7, 4, 5, 6, 2, 8, 9]
assert re_arrange_array([12, -14, -26, 13, 15], 5) == [-14, -26, 12, 13, 15]
assert re_arrange_array([10, 24, 36, -42, -39, -78, 85], 7) == [-42, -39, -78, 10, 24, 36, 85]

Your response should only contain the code for this function.

def re_arrange_array(arr, n):
    ...


 </pre>
###### answer
<pre> ```python
def re_arrange_array(arr, n):
    negatives = [x for x in arr[:n] if x &lt; 0]
    positives = [x for x in arr[:n] if x >= 0]
    rearranged = negatives + positives
    return rearranged + arr[n:]
``` </pre>
###### canonical_solution
<pre> def re_arrange_array(arr, n):
  j=0
  for i in range(0, n):
    if (arr[i] &lt; 0):
      temp = arr[i]
      arr[i] = arr[j]
      arr[j] = temp
      j = j + 1
  return arr </pre>
###### test
<pre> assert re_arrange_array([-1, 2, -3, 4, 5, 6, -7, 8, 9], 9) == [-1, -3, -7, 4, 5, 6, 2, 8, 9]
assert re_arrange_array([12, -14, -26, 13, 15], 5) == [-14, -26, 12, 13, 15]
assert re_arrange_array([10, 24, 36, -42, -39, -78, 85], 7) == [-42, -39, -78, 10, 24, 36, 85] </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 14
     10     rearranged = negatives + positives
     11     return rearranged + arr[n:]
---> 14 assert re_arrange_array([-1, 2, -3, 4, 5, 6, -7, 8, 9], 9) == [-1, -3, -7, 4, 5, 6, 2, 8, 9]
     15 assert re_arrange_array([12, -14, -26, 13, 15], 5) == [-14, -26, 12, 13, 15]
     16 assert re_arrange_array([10, 24, 36, -42, -39, -78, 85], 7) == [-42, -39, -78, 10, 24, 36, 85]
AssertionError:  </pre>
### 443
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a python function to find the largest negative number from the given list.

Your code should pass these tests:

assert largest_neg([1,2,3,-4,-6]) == -6
assert largest_neg([1,2,3,-8,-9]) == -9
assert largest_neg([1,2,3,4,-1]) == -1

Your response should only contain the code for this function.

def largest_neg(list1): 
    ...


 </pre>
###### answer
<pre> ```python
def largest_neg(list1):
    negatives = [num for num in list1 if num &lt; 0]
    return max(negatives) if negatives else None
``` </pre>
###### canonical_solution
<pre> def largest_neg(list1): 
    max = list1[0] 
    for x in list1: 
        if x &lt; max : 
             max = x  
    return max </pre>
###### test
<pre> assert largest_neg([1,2,3,-4,-6]) == -6
assert largest_neg([1,2,3,-8,-9]) == -9
assert largest_neg([1,2,3,4,-1]) == -1 </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 12
      8     negatives = [num for num in list1 if num &lt; 0]
      9     return max(negatives) if negatives else None
---> 12 assert largest_neg([1,2,3,-4,-6]) == -6
     13 assert largest_neg([1,2,3,-8,-9]) == -9
     14 assert largest_neg([1,2,3,4,-1]) == -1
AssertionError:  </pre>
### 137
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to find the ratio of zeroes to non-zeroes in an array of integers.

Your code should pass these tests:

import math

assert math.isclose(zero_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]), 0.181818, rel_tol=0.001)
assert math.isclose(zero_count([2, 1, 2, -1, -5, 6, 4, -3, -2, 3, 4, 6, 8]), 0.00, rel_tol=0.001)
assert math.isclose(zero_count([2, 4, -6, -9, 11, -12, 14, -5, 17]), 0.00, rel_tol=0.001)

Your response should only contain the code for this function.

def zero_count(nums):
    ...


 </pre>
###### answer
<pre> ```python
def zero_count(nums):
    zeroes = nums.count(0)
    non_zeroes = len(nums) - zeroes
    if non_zeroes == 0:
        return 0.0
    return zeroes / len(nums)
``` </pre>
###### canonical_solution
<pre> from array import array
def zero_count(nums):
    n = len(nums)
    n1 = 0
    for x in nums:
        if x == 0:
            n1 += 1
        else:
          None
    return n1/(n-n1) </pre>
###### test
<pre> import math

assert math.isclose(zero_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]), 0.181818, rel_tol=0.001)
assert math.isclose(zero_count([2, 1, 2, -1, -5, 6, 4, -3, -2, 3, 4, 6, 8]), 0.00, rel_tol=0.001)
assert math.isclose(zero_count([2, 4, -6, -9, 11, -12, 14, -5, 17]), 0.00, rel_tol=0.001) </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 17
     12     return zeroes / len(nums)
     15 import math
---> 17 assert math.isclose(zero_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]), 0.181818, rel_tol=0.001)
     18 assert math.isclose(zero_count([2, 1, 2, -1, -5, 6, 4, -3, -2, 3, 4, 6, 8]), 0.00, rel_tol=0.001)
     19 assert math.isclose(zero_count([2, 4, -6, -9, 11, -12, 14, -5, 17]), 0.00, rel_tol=0.001)
AssertionError:  </pre>
### 164
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to determine if the sum of the divisors of two integers are the same.

Your code should pass these tests:

assert are_equivalent(36, 57) == False
assert are_equivalent(2, 4) == False
assert are_equivalent(23, 47) == True

Your response should only contain the code for this function.

def div_sum(n): 
    ...


 </pre>
###### answer
<pre> ```python
def div_sum(n):
    if n == 1:
        return 1
    divisors = {1, n}
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return sum(divisors)

def are_equivalent(a, b):
    return div_sum(a) == div_sum(b)
``` </pre>
###### canonical_solution
<pre> import math 
def div_sum(n): 
  total = 1
  i = 2

  while i * i &lt;= n:
    if (n % i == 0):
      total = (total + i + math.floor(n / i))
    i += 1

  return total

def are_equivalent(num1, num2): 
    return div_sum(num1) == div_sum(num2);  </pre>
###### test
<pre> assert are_equivalent(36, 57) == False
assert are_equivalent(2, 4) == False
assert are_equivalent(23, 47) == True </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 23
     21 assert are_equivalent(36, 57) == False
     22 assert are_equivalent(2, 4) == False
---> 23 assert are_equivalent(23, 47) == True
AssertionError:  </pre>
### 235
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a python function to set all even bits of a given number.

Your code should pass these tests:

assert even_bit_set_number(10) == 10
assert even_bit_set_number(20) == 30
assert even_bit_set_number(30) == 30

Your response should only contain the code for this function.

def even_bit_set_number(n): 
    ...


 </pre>
###### answer
<pre> ```python
def even_bit_set_number(n):
    mask = 0
    i = 0
    while (1 &lt;&lt; i) &lt;= n:
        if i % 2 == 0:
            mask |= (1 &lt;&lt; i)
        i += 1
    return n | mask
``` </pre>
###### canonical_solution
<pre> def even_bit_set_number(n): 
    count = 0;res = 0;temp = n 
    while(temp > 0): 
        if (count % 2 == 1): 
            res |= (1 &lt;&lt; count)
        count+=1
        temp >>= 1
    return (n | res)  </pre>
###### test
<pre> assert even_bit_set_number(10) == 10
assert even_bit_set_number(20) == 30
assert even_bit_set_number(30) == 30 </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 17
     13         i += 1
     14     return n | mask
---> 17 assert even_bit_set_number(10) == 10
     18 assert even_bit_set_number(20) == 30
     19 assert even_bit_set_number(30) == 30
AssertionError:  </pre>
### 310
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to convert a given string to a tuple of characters.

Your code should pass these tests:

assert string_to_tuple("python 3.0")==('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0')
assert string_to_tuple("item1")==('i', 't', 'e', 'm', '1')
assert string_to_tuple("15.10")==('1', '5', '.', '1', '0')

Your response should only contain the code for this function.

def string_to_tuple(str1):
    ...


 </pre>
###### answer
<pre> ```python
def string_to_tuple(str1):
    return tuple(str1)
``` </pre>
###### canonical_solution
<pre> def string_to_tuple(str1):
    result = tuple(x for x in str1 if not x.isspace()) 
    return result </pre>
###### test
<pre> assert string_to_tuple("python 3.0")==('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0')
assert string_to_tuple("item1")==('i', 't', 'e', 'm', '1')
assert string_to_tuple("15.10")==('1', '5', '.', '1', '0') </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 11
      7 def string_to_tuple(str1):
      8     return tuple(str1)
---> 11 assert string_to_tuple("python 3.0")==('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0')
     12 assert string_to_tuple("item1")==('i', 't', 'e', 'm', '1')
     13 assert string_to_tuple("15.10")==('1', '5', '.', '1', '0')
AssertionError:  </pre>
### 438
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to count bidirectional tuple pairs.

Your code should pass these tests:

assert count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 1), (6, 5), (2, 1)] ) == 3
assert count_bidirectional([(5, 6), (1, 3), (6, 5), (9, 1), (6, 5), (2, 1)] ) == 2
assert count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 2), (6, 5), (2, 1)] ) == 4

Your response should only contain the code for this function.

def count_bidirectional(test_list):
    ...


 </pre>
###### answer
<pre> ```python
def count_bidirectional(test_list):
    count = 0
    seen = set()
    for pair in test_list:
        reverse_pair = (pair[1], pair[0])
        if reverse_pair in seen:
            count += 1
            seen.remove(reverse_pair)
        else:
            seen.add(pair)
    return count
``` </pre>
###### canonical_solution
<pre> def count_bidirectional(test_list):
  res = 0
  for idx in range(0, len(test_list)):
    for iidx in range(idx + 1, len(test_list)):
      if test_list[iidx][0] == test_list[idx][1] and test_list[idx][1] == test_list[iidx][0]:
        res += 1
  return res </pre>
###### test
<pre> assert count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 1), (6, 5), (2, 1)] ) == 3
assert count_bidirectional([(5, 6), (1, 3), (6, 5), (9, 1), (6, 5), (2, 1)] ) == 2
assert count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 2), (6, 5), (2, 1)] ) == 4 </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 20
     16             seen.add(pair)
     17     return count
---> 20 assert count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 1), (6, 5), (2, 1)] ) == 3
     21 assert count_bidirectional([(5, 6), (1, 3), (6, 5), (9, 1), (6, 5), (2, 1)] ) == 2
     22 assert count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 2), (6, 5), (2, 1)] ) == 4
AssertionError:  </pre>
### 103
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to find the Eulerian number a(n, m).

Your code should pass these tests:

assert eulerian_num(3, 1) == 4
assert eulerian_num(4, 1) == 11
assert eulerian_num(5, 3) == 26

Your response should only contain the code for this function.

def eulerian_num(n, m): 
    ...


 </pre>
###### answer
<pre> ```python
def eulerian_num(n, m):
    if m &lt; 0 or m >= n:
        return 0
    if n == 0:
        return 1
    return (n - m) * eulerian_num(n - 1, m - 1) + (m + 1) * eulerian_num(n - 1, m)
``` </pre>
###### canonical_solution
<pre> def eulerian_num(n, m): 
	if (m >= n or n == 0): 
		return 0 
	if (m == 0): 
		return 1 
	return ((n - m) * eulerian_num(n - 1, m - 1) +(m + 1) * eulerian_num(n - 1, m)) </pre>
###### test
<pre> assert eulerian_num(3, 1) == 4
assert eulerian_num(4, 1) == 11
assert eulerian_num(5, 3) == 26 </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 15
     11         return 1
     12     return (n - m) * eulerian_num(n - 1, m - 1) + (m + 1) * eulerian_num(n - 1, m)
---> 15 assert eulerian_num(3, 1) == 4
     16 assert eulerian_num(4, 1) == 11
     17 assert eulerian_num(5, 3) == 26
AssertionError:  </pre>
### 249
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to find the intersection of two arrays.

Your code should pass these tests:

assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[1, 2, 4, 8, 9])==[1, 2, 8, 9]
assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[3,5,7,9])==[3,5,7,9]
assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[10,20,30,40])==[10]

Your response should only contain the code for this function.

def intersection_array(array_nums1,array_nums2):
    ...


 </pre>
###### answer
<pre> ```python
def intersection_array(array_nums1, array_nums2):
    return list(set(array_nums1) & set(array_nums2))
``` </pre>
###### canonical_solution
<pre> def intersection_array(array_nums1,array_nums2):
 result = list(filter(lambda x: x in array_nums1, array_nums2)) 
 return result </pre>
###### test
<pre> assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[1, 2, 4, 8, 9])==[1, 2, 8, 9]
assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[3,5,7,9])==[3,5,7,9]
assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[10,20,30,40])==[10] </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 11
      7 def intersection_array(array_nums1, array_nums2):
      8     return list(set(array_nums1) & set(array_nums2))
---> 11 assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[1, 2, 4, 8, 9])==[1, 2, 8, 9]
     12 assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[3,5,7,9])==[3,5,7,9]
     13 assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[10,20,30,40])==[10]
AssertionError:  </pre>
### 87
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to merge three dictionaries into a single dictionary.

Your code should pass these tests:

assert merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" }, { "G": "Green", "W": "White" },{ "O": "Orange", "W": "White", "B": "Black" })=={'B': 'Black', 'R': 'Red', 'P': 'Pink', 'G': 'Green', 'W': 'White', 'O': 'Orange'}
assert merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" }, { "G": "Green", "W": "White" },{"L":"lavender","B":"Blue"})=={'W': 'White', 'P': 'Pink', 'B': 'Black', 'R': 'Red', 'G': 'Green', 'L': 'lavender'}
assert merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" },{"L":"lavender","B":"Blue"},{ "G": "Green", "W": "White" })=={'B': 'Black', 'P': 'Pink', 'R': 'Red', 'G': 'Green', 'L': 'lavender', 'W': 'White'}

Your response should only contain the code for this function.

def merge_dictionaries_three(dict1,dict2, dict3):
    ...


 </pre>
###### answer
<pre> ```python
def merge_dictionaries_three(dict1, dict2, dict3):
    merged_dict = {}
    merged_dict.update(dict1)
    merged_dict.update(dict2)
    merged_dict.update(dict3)
    return merged_dict
``` </pre>
###### canonical_solution
<pre> import collections as ct
def merge_dictionaries_three(dict1,dict2, dict3):
    merged_dict = dict(ct.ChainMap({},dict1,dict2,dict3))
    return merged_dict </pre>
###### test
<pre> assert merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" }, { "G": "Green", "W": "White" },{ "O": "Orange", "W": "White", "B": "Black" })=={'B': 'Black', 'R': 'Red', 'P': 'Pink', 'G': 'Green', 'W': 'White', 'O': 'Orange'}
assert merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" }, { "G": "Green", "W": "White" },{"L":"lavender","B":"Blue"})=={'W': 'White', 'P': 'Pink', 'B': 'Black', 'R': 'Red', 'G': 'Green', 'L': 'lavender'}
assert merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" },{"L":"lavender","B":"Blue"},{ "G": "Green", "W": "White" })=={'B': 'Black', 'P': 'Pink', 'R': 'Red', 'G': 'Green', 'L': 'lavender', 'W': 'White'} </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 16
     12     return merged_dict
     15 assert merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" }, { "G": "Green", "W": "White" },{ "O": "Orange", "W": "White", "B": "Black" })=={'B': 'Black', 'R': 'Red', 'P': 'Pink', 'G': 'Green', 'W': 'White', 'O': 'Orange'}
---> 16 assert merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" }, { "G": "Green", "W": "White" },{"L":"lavender","B":"Blue"})=={'W': 'White', 'P': 'Pink', 'B': 'Black', 'R': 'Red', 'G': 'Green', 'L': 'lavender'}
     17 assert merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" },{"L":"lavender","B":"Blue"},{ "G": "Green", "W": "White" })=={'B': 'Black', 'P': 'Pink', 'R': 'Red', 'G': 'Green', 'L': 'lavender', 'W': 'White'}
AssertionError:  </pre>
