# mbpp / yandexgpt-5-pro
### 460
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a python function to get the first element of each sublist.

Your code should pass these tests:

assert Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]]) == [1, 3, 6]
assert Extract([[1,2,3],[4, 5]]) == [1,4]
assert Extract([[9,8,1],[1,2]]) == [9,1]

Your response should only contain the code for this function.

def Extract(lst): 
    ...


 </pre>
###### answer
<pre> ```
def Extract(lst):
    return [sublist[0] for sublist in lst]
``` </pre>
###### canonical_solution
<pre> def Extract(lst): 
    return [item[0] for item in lst]  </pre>
###### test
<pre> assert Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]]) == [1, 3, 6]
assert Extract([[1,2,3],[4, 5]]) == [1,4]
assert Extract([[9,8,1],[1,2]]) == [9,1] </pre>
### 291
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to find out the number of ways of painting the fence such that at most 2 adjacent posts have the same color for the given fence with n posts and k colors.

Your code should pass these tests:

assert count_no_of_ways(2, 4) == 16
assert count_no_of_ways(3, 2) == 6
assert count_no_of_ways(4, 4) == 228

Your response should only contain the code for this function.

def count_no_of_ways(n, k): 
    ...


 </pre>
###### answer
<pre> ```
def count_no_of_ways(n, k):
    if n == 0:
        return 0
    if n == 1:
        return k
    same = k
    diff = k * (k - 1)
    for i in range(2, n):
        same, diff = diff, (same + diff) * (k - 1)
    return same + diff
``` </pre>
###### canonical_solution
<pre> def count_no_of_ways(n, k): 
	dp = [0] * (n + 1) 
	total = k 
	mod = 1000000007
	dp[1] = k 
	dp[2] = k * k	 
	for i in range(3,n+1): 
		dp[i] = ((k - 1) * (dp[i - 1] + dp[i - 2])) % mod 
	return dp[n] </pre>
###### test
<pre> assert count_no_of_ways(2, 4) == 16
assert count_no_of_ways(3, 2) == 6
assert count_no_of_ways(4, 4) == 228 </pre>
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
<pre> ```
def count_binary_seq(n):
    from math import comb

    total_count = 0
    for k in range(n + 1):
        total_count += comb(n, k) * comb(n, k)
    return total_count
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
### 256
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a python function that takes in a non-negative number and returns the number of prime numbers less than the given non-negative number.

Your code should pass these tests:

assert count_Primes_nums(5) == 2
assert count_Primes_nums(10) == 4
assert count_Primes_nums(100) == 25

Your response should only contain the code for this function.

def count_Primes_nums(n):
    ...


 </pre>
###### answer
<pre> ```
def count_Primes_nums(n):
    if n &lt;= 2:
        return 0
    sieve = [True] * n
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n, i):
                sieve[j] = False
    return sum(sieve)
``` </pre>
###### canonical_solution
<pre> def count_Primes_nums(n):
    ctr = 0
    for num in range(n):
        if num &lt;= 1:
            continue
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            ctr += 1
    return ctr </pre>
###### test
<pre> assert count_Primes_nums(5) == 2
assert count_Primes_nums(10) == 4
assert count_Primes_nums(100) == 25 </pre>
### 478
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to remove lowercase substrings from a given string.

Your code should pass these tests:

assert remove_lowercase("PYTHon")==('PYTH')
assert remove_lowercase("FInD")==('FID')
assert remove_lowercase("STRinG")==('STRG')

Your response should only contain the code for this function.

def remove_lowercase(str1):
    ...


 </pre>
###### answer
<pre> ```
def remove_lowercase(str1):
    result = ''.join(char for char in str1 if char.isupper())
    return result
``` </pre>
###### canonical_solution
<pre> import re
def remove_lowercase(str1):
 return re.sub('[a-z]', '', str1) </pre>
###### test
<pre> assert remove_lowercase("PYTHon")==('PYTH')
assert remove_lowercase("FInD")==('FID')
assert remove_lowercase("STRinG")==('STRG') </pre>
### 262
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function that takes in a list and an integer L and splits the given list into two parts where the length of the first part of the list is L, and returns the resulting lists in a tuple.

Your code should pass these tests:

assert split_two_parts([1,1,2,3,4,4,5,1],3)==([1, 1, 2], [3, 4, 4, 5, 1])
assert split_two_parts(['a', 'b', 'c', 'd'],2)==(['a', 'b'], ['c', 'd'])
assert split_two_parts(['p', 'y', 't', 'h', 'o', 'n'],4)==(['p', 'y', 't', 'h'], ['o', 'n'])

Your response should only contain the code for this function.

def split_two_parts(list1, L):
    ...


 </pre>
###### answer
<pre> ```
def split_two_parts(list1, L):
    return (list1[:L], list1[L:])
``` </pre>
###### canonical_solution
<pre> def split_two_parts(list1, L):
    return list1[:L], list1[L:] </pre>
###### test
<pre> assert split_two_parts([1,1,2,3,4,4,5,1],3)==([1, 1, 2], [3, 4, 4, 5, 1])
assert split_two_parts(['a', 'b', 'c', 'd'],2)==(['a', 'b'], ['c', 'd'])
assert split_two_parts(['p', 'y', 't', 'h', 'o', 'n'],4)==(['p', 'y', 't', 'h'], ['o', 'n']) </pre>
### 279
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to find the nth decagonal number.

Your code should pass these tests:

assert is_num_decagonal(3) == 27
assert is_num_decagonal(7) == 175
assert is_num_decagonal(10) == 370

Your response should only contain the code for this function.

def is_num_decagonal(n): 
    ...


 </pre>
###### answer
<pre> ```
def is_num_decagonal(n):
    return n * (8 * n - 6) // 2
``` </pre>
###### canonical_solution
<pre> def is_num_decagonal(n): 
	return 4 * n * n - 3 * n  </pre>
###### test
<pre> assert is_num_decagonal(3) == 27
assert is_num_decagonal(7) == 175
assert is_num_decagonal(10) == 370 </pre>
### 445
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to perform index wise multiplication of tuple elements in the given two tuples.

Your code should pass these tests:

assert index_multiplication(((1, 3), (4, 5), (2, 9), (1, 10)),((6, 7), (3, 9), (1, 1), (7, 3)) ) == ((6, 21), (12, 45), (2, 9), (7, 30))
assert index_multiplication(((2, 4), (5, 6), (3, 10), (2, 11)),((7, 8), (4, 10), (2, 2), (8, 4)) ) == ((14, 32), (20, 60), (6, 20), (16, 44))
assert index_multiplication(((3, 5), (6, 7), (4, 11), (3, 12)),((8, 9), (5, 11), (3, 3), (9, 5)) ) == ((24, 45), (30, 77), (12, 33), (27, 60))

Your response should only contain the code for this function.

def index_multiplication(test_tup1, test_tup2):
    ...


 </pre>
###### answer
<pre> ```python
def index_multiplication(test_tup1, test_tup2):
    result = tuple(tuple(a * b for a, b in zip(tup1, tup2)) for tup1, tup2 in zip(test_tup1, test_tup2))
    return result
``` </pre>
###### canonical_solution
<pre> def index_multiplication(test_tup1, test_tup2):
  res = tuple(tuple(a * b for a, b in zip(tup1, tup2))
   for tup1, tup2 in zip(test_tup1, test_tup2))
  return (res)  </pre>
###### test
<pre> assert index_multiplication(((1, 3), (4, 5), (2, 9), (1, 10)),((6, 7), (3, 9), (1, 1), (7, 3)) ) == ((6, 21), (12, 45), (2, 9), (7, 30))
assert index_multiplication(((2, 4), (5, 6), (3, 10), (2, 11)),((7, 8), (4, 10), (2, 2), (8, 4)) ) == ((14, 32), (20, 60), (6, 20), (16, 44))
assert index_multiplication(((3, 5), (6, 7), (4, 11), (3, 12)),((8, 9), (5, 11), (3, 3), (9, 5)) ) == ((24, 45), (30, 77), (12, 33), (27, 60)) </pre>
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
<pre> ```
def count_element_in_list(list1, x):
    count = 0
    for sublist in list1:
        if x in sublist:
            count += 1
    return count
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
### 399
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to perform the mathematical bitwise xor operation across the given tuples.

Your code should pass these tests:

assert bitwise_xor((10, 4, 6, 9), (5, 2, 3, 3)) == (15, 6, 5, 10)
assert bitwise_xor((11, 5, 7, 10), (6, 3, 4, 4)) == (13, 6, 3, 14)
assert bitwise_xor((12, 6, 8, 11), (7, 4, 5, 6)) == (11, 2, 13, 13)

Your response should only contain the code for this function.

def bitwise_xor(test_tup1, test_tup2):
    ...


 </pre>
###### answer
<pre> ```
def bitwise_xor(test_tup1, test_tup2):
    res = tuple(a ^ b for a, b in zip(test_tup1, test_tup2))
    return res
``` </pre>
###### canonical_solution
<pre> def bitwise_xor(test_tup1, test_tup2):
  res = tuple(ele1 ^ ele2 for ele1, ele2 in zip(test_tup1, test_tup2))
  return (res)  </pre>
###### test
<pre> assert bitwise_xor((10, 4, 6, 9), (5, 2, 3, 3)) == (15, 6, 5, 10)
assert bitwise_xor((11, 5, 7, 10), (6, 3, 4, 4)) == (13, 6, 3, 14)
assert bitwise_xor((12, 6, 8, 11), (7, 4, 5, 6)) == (11, 2, 13, 13) </pre>
