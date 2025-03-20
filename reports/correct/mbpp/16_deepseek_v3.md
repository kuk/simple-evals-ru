# mbpp / deepseek-v3
### 168
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to count the number of occurrences of a number in a given list.

Your code should pass these tests:

assert frequency([1,2,3], 4) == 0
assert frequency([1,2,2,3,3,3,4], 3) == 3
assert frequency([0,1,2,3,1,2], 1) == 2

Your response should only contain the code for this function.

def frequency(a,x): 
    ...


 </pre>
###### answer
<pre> ```python
def frequency(a, x):
    return a.count(x)
``` </pre>
###### canonical_solution
<pre> def frequency(a,x): 
    count = 0  
    for i in a: 
      if i == x: 
        count += 1

    return count  </pre>
###### test
<pre> assert frequency([1,2,3], 4) == 0
assert frequency([1,2,2,3,3,3,4], 3) == 3
assert frequency([0,1,2,3,1,2], 1) == 2 </pre>
### 111
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to find the common elements in given nested lists.

Your code should pass these tests:

assert set(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]))==set([18, 12])
assert set(common_in_nested_lists([[12, 5, 23, 25, 45], [7, 11, 5, 23, 28], [1, 5, 8, 18, 23, 16]]))==set([5,23])
assert set(common_in_nested_lists([[2, 3,4, 1], [4, 5], [6,4, 8],[4, 5], [6, 8,4]]))==set([4])

Your response should only contain the code for this function.

def common_in_nested_lists(nestedlist):
    ...


 </pre>
###### answer
<pre> ```python
def common_in_nested_lists(nestedlist):
    if not nestedlist:
        return set()
    common = set(nestedlist[0])
    for lst in nestedlist[1:]:
        common.intersection_update(lst)
    return common
``` </pre>
###### canonical_solution
<pre> def common_in_nested_lists(nestedlist):
    result = list(set.intersection(*map(set, nestedlist)))
    return result </pre>
###### test
<pre> assert set(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]))==set([18, 12])
assert set(common_in_nested_lists([[12, 5, 23, 25, 45], [7, 11, 5, 23, 28], [1, 5, 8, 18, 23, 16]]))==set([5,23])
assert set(common_in_nested_lists([[2, 3,4, 1], [4, 5], [6,4, 8],[4, 5], [6, 8,4]]))==set([4]) </pre>
### 388
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a python function to find the highest power of 2 that is less than or equal to n.

Your code should pass these tests:

assert highest_Power_of_2(10) == 8
assert highest_Power_of_2(19) == 16
assert highest_Power_of_2(32) == 32

Your response should only contain the code for this function.

def highest_Power_of_2(n): 
    ...


 </pre>
###### answer
<pre> ```python
def highest_Power_of_2(n):
    power = 1
    while power * 2 &lt;= n:
        power *= 2
    return power
``` </pre>
###### canonical_solution
<pre> def highest_Power_of_2(n): 
    res = 0 
    for i in range(n, 0, -1): 
        if ((i & (i - 1)) == 0): 
            res = i 
            break 
    return res  </pre>
###### test
<pre> assert highest_Power_of_2(10) == 8
assert highest_Power_of_2(19) == 16
assert highest_Power_of_2(32) == 32 </pre>
### 115
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to check whether all dictionaries in a list are empty or not.

Your code should pass these tests:

assert empty_dit([{},{},{}])==True
assert empty_dit([{1,2},{},{}])==False
assert empty_dit({})==True

Your response should only contain the code for this function.

def empty_dit(list1):
    ...


 </pre>
###### answer
<pre> ```python
def empty_dit(list1):
    if isinstance(list1, dict):
        return not list1
    return all(not d for d in list1)
``` </pre>
###### canonical_solution
<pre> def empty_dit(list1):
 empty_dit=all(not d for d in list1)
 return empty_dit </pre>
###### test
<pre> assert empty_dit([{},{},{}])==True
assert empty_dit([{1,2},{},{}])==False
assert empty_dit({})==True </pre>
### 167
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a python function to find the smallest power of 2 greater than or equal to n.

Your code should pass these tests:

assert next_power_of_2(0) == 1
assert next_power_of_2(5) == 8
assert next_power_of_2(17) == 32

Your response should only contain the code for this function.

def next_power_of_2(n): 
    ...


 </pre>
###### answer
<pre> ```python
def next_power_of_2(n):
    if n == 0:
        return 1
    power = 1
    while power &lt; n:
        power *= 2
    return power
``` </pre>
###### canonical_solution
<pre> def next_power_of_2(n): 
  if n and not n & (n - 1):
    return n

  count = 0
  while n != 0: 
    n >>= 1
    count += 1

  return 1 &lt;&lt; count;  </pre>
###### test
<pre> assert next_power_of_2(0) == 1
assert next_power_of_2(5) == 8
assert next_power_of_2(17) == 32 </pre>
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
    for k in range(n + 1):
        total += comb(n, k) ** 2
    return total
``` </pre>
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
### 232
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function that takes in a list and an integer n and returns a list containing the n largest items from the list.

Your code should pass these tests:

assert set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2))==set([100,90])
assert set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],5))==set([100,90,80,70,60])
assert set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],3))==set([100,90,80])

Your response should only contain the code for this function.

def larg_nnum(list1,n):
    ...


 </pre>
###### answer
<pre> ```python
def larg_nnum(list1, n):
    return sorted(list1, reverse=True)[:n]
``` </pre>
###### canonical_solution
<pre> import heapq
def larg_nnum(list1,n):
 largest=heapq.nlargest(n,list1)
 return largest </pre>
###### test
<pre> assert set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2))==set([100,90])
assert set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],5))==set([100,90,80,70,60])
assert set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],3))==set([100,90,80]) </pre>
### 269
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to find the ascii value of a character.

Your code should pass these tests:

assert ascii_value('A')==65
assert ascii_value('R')==82
assert ascii_value('S')==83

Your response should only contain the code for this function.

def ascii_value(k):
    ...


 </pre>
###### answer
<pre> ```python
def ascii_value(k):
    return ord(k)
``` </pre>
###### canonical_solution
<pre> def ascii_value(k):
  ch=k
  return ord(ch) </pre>
###### test
<pre> assert ascii_value('A')==65
assert ascii_value('R')==82
assert ascii_value('S')==83 </pre>
### 105
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a python function to count true booleans in the given list.

Your code should pass these tests:

assert count([True,False,True]) == 2
assert count([False,False]) == 0
assert count([True,True,True]) == 3

Your response should only contain the code for this function.

def count(lst):   
    ...


 </pre>
###### answer
<pre> ```python
def count(lst):
    return sum(1 for item in lst if item)
``` </pre>
###### canonical_solution
<pre> def count(lst):   
    return sum(lst)  </pre>
###### test
<pre> assert count([True,False,True]) == 2
assert count([False,False]) == 0
assert count([True,True,True]) == 3 </pre>
### 429
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to extract the elementwise and tuples from the given two tuples.

Your code should pass these tests:

assert and_tuples((10, 4, 6, 9), (5, 2, 3, 3)) == (0, 0, 2, 1)
assert and_tuples((1, 2, 3, 4), (5, 6, 7, 8)) == (1, 2, 3, 0)
assert and_tuples((8, 9, 11, 12), (7, 13, 14, 17)) == (0, 9, 10, 0)

Your response should only contain the code for this function.

def and_tuples(test_tup1, test_tup2):
    ...


 </pre>
###### answer
<pre> ```python
def and_tuples(test_tup1, test_tup2):
    return tuple(a & b for a, b in zip(test_tup1, test_tup2))
``` </pre>
###### canonical_solution
<pre> def and_tuples(test_tup1, test_tup2):
  res = tuple(ele1 & ele2 for ele1, ele2 in zip(test_tup1, test_tup2))
  return (res)  </pre>
###### test
<pre> assert and_tuples((10, 4, 6, 9), (5, 2, 3, 3)) == (0, 0, 2, 1)
assert and_tuples((1, 2, 3, 4), (5, 6, 7, 8)) == (1, 2, 3, 0)
assert and_tuples((8, 9, 11, 12), (7, 13, 14, 17)) == (0, 9, 10, 0) </pre>
