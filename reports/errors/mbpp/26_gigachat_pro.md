# mbpp / gigachat-2-pro
### 452
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function that gives loss amount on a sale if the given amount has loss else return 0.

Your code should pass these tests:

assert loss_amount(1500,1200)==0
assert loss_amount(100,200)==100
assert loss_amount(2000,5000)==3000

Your response should only contain the code for this function.

def loss_amount(actual_cost,sale_amount): 
    ...


 </pre>
###### answer
<pre> ```python
def loss_amount(actual_cost, sale_amount):
    if sale_amount &lt; bought_cost:
        return bought_cost - sale_amount
    else:
        return 0
``` </pre>
###### canonical_solution
<pre> def loss_amount(actual_cost,sale_amount): 
  if(sale_amount > actual_cost):
    amount = sale_amount - actual_cost
    return amount
  else:
    return 0 </pre>
###### test
<pre> assert loss_amount(1500,1200)==0
assert loss_amount(100,200)==100
assert loss_amount(2000,5000)==3000 </pre>
###### traceback
<pre> ---------------------------------------------------------------------------NameError                                 Traceback (most recent call last)Cell In[1], line 14
     10     else:
     11         return 0
---> 14 assert loss_amount(1500,1200)==0
     15 assert loss_amount(100,200)==100
     16 assert loss_amount(2000,5000)==3000
Cell In[1], line 8, in loss_amount(actual_cost, sale_amount)
      7 def loss_amount(actual_cost, sale_amount):
----> 8     if sale_amount &lt; bought_cost:
      9         return bought_cost - sale_amount
     10     else:
NameError: name 'bought_cost' is not defined </pre>
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
from itertools import chain, combinations

def combinations_list(list1):
    return [list(comb) for comb in chain.from_iterable(
        combinations(list1, r) for r in range(len(list1)+1)
    )]
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
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 15
      9 def combinations_list(list1):
     10     return [list(comb) for comb in chain.from_iterable(
     11         combinations(list1, r) for r in range(len(list1)+1)
     12     )]
---> 15 assert combinations_list(['orange', 'red', 'green', 'blue'])==[[], ['orange'], ['red'], ['red', 'orange'], ['green'], ['green', 'orange'], ['green', 'red'], ['green', 'red', 'orange'], ['blue'], ['blue', 'orange'], ['blue', 'red'], ['blue', 'red', 'orange'], ['blue', 'green'], ['blue', 'green', 'orange'], ['blue', 'green', 'red'], ['blue', 'green', 'red', 'orange']]
     16 assert combinations_list(['red', 'green', 'blue', 'white', 'black', 'orange'])==[[], ['red'], ['green'], ['green', 'red'], ['blue'], ['blue', 'red'], ['blue', 'green'], ['blue', 'green', 'red'], ['white'], ['white', 'red'], ['white', 'green'], ['white', 'green', 'red'], ['white', 'blue'], ['white', 'blue', 'red'], ['white', 'blue', 'green'], ['white', 'blue', 'green', 'red'], ['black'], ['black', 'red'], ['black', 'green'], ['black', 'green', 'red'], ['black', 'blue'], ['black', 'blue', 'red'], ['black', 'blue', 'green'], ['black', 'blue', 'green', 'red'], ['black', 'white'], ['black', 'white', 'red'], ['black', 'white', 'green'], ['black', 'white', 'green', 'red'], ['black', 'white', 'blue'], ['black', 'white', 'blue', 'red'], ['black', 'white', 'blue', 'green'], ['black', 'white', 'blue', 'green', 'red'], ['orange'], ['orange', 'red'], ['orange', 'green'], ['orange', 'green', 'red'], ['orange', 'blue'], ['orange', 'blue', 'red'], ['orange', 'blue', 'green'], ['orange', 'blue', 'green', 'red'], ['orange', 'white'], ['orange', 'white', 'red'], ['orange', 'white', 'green'], ['orange', 'white', 'green', 'red'], ['orange', 'white', 'blue'], ['orange', 'white', 'blue', 'red'], ['orange', 'white', 'blue', 'green'], ['orange', 'white', 'blue', 'green', 'red'], ['orange', 'black'], ['orange', 'black', 'red'], ['orange', 'black', 'green'], ['orange', 'black', 'green', 'red'], ['orange', 'black', 'blue'], ['orange', 'black', 'blue', 'red'], ['orange', 'black', 'blue', 'green'], ['orange', 'black', 'blue', 'green', 'red'], ['orange', 'black', 'white'], ['orange', 'black', 'white', 'red'], ['orange', 'black', 'white', 'green'], ['orange', 'black', 'white', 'green', 'red'], ['orange', 'black', 'white', 'blue'], ['orange', 'black', 'white', 'blue', 'red'], ['orange', 'black', 'white', 'blue', 'green'], ['orange', 'black', 'white', 'blue', 'green', 'red']]
     17 assert combinations_list(['red', 'green', 'black', 'orange'])==[[], ['red'], ['green'], ['green', 'red'], ['black'], ['black', 'red'], ['black', 'green'], ['black', 'green', 'red'], ['orange'], ['orange', 'red'], ['orange', 'green'], ['orange', 'green', 'red'], ['orange', 'black'], ['orange', 'black', 'red'], ['orange', 'black', 'green'], ['orange', 'black', 'green', 'red']]
AssertionError:  </pre>
### 244
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a python function to find the next perfect square greater than a given number.

Your code should pass these tests:

assert next_Perfect_Square(35) == 36
assert next_Perfect_Square(6) == 9
assert next_Perfect_Square(9) == 16

Your response should only contain the code for this function.

def next_Perfect_Square(N): 
    ...


 </pre>
###### answer
<pre> ```python
import math

def next_Perfect_Square(N):
    root = math.ceil(math.sqrt(N))
    return root * root
``` </pre>
###### canonical_solution
<pre> import math  
def next_Perfect_Square(N): 
    nextN = math.floor(math.sqrt(N)) + 1
    return nextN * nextN  </pre>
###### test
<pre> assert next_Perfect_Square(35) == 36
assert next_Perfect_Square(6) == 9
assert next_Perfect_Square(9) == 16 </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 16
     14 assert next_Perfect_Square(35) == 36
     15 assert next_Perfect_Square(6) == 9
---> 16 assert next_Perfect_Square(9) == 16
AssertionError:  </pre>
### 72
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a python function to check whether the given number can be represented as the difference of two squares or not.

Your code should pass these tests:

assert dif_Square(5) == True
assert dif_Square(10) == False
assert dif_Square(15) == True

Your response should only contain the code for this function.

def dif_Square(n): 
    ...


 </pre>
###### answer
<pre> ```python
def dif_Square(n):
    return n % 4 != 3
``` </pre>
###### canonical_solution
<pre> def dif_Square(n): 
    if (n % 4 != 2): 
        return True
    return False </pre>
###### test
<pre> assert dif_Square(5) == True
assert dif_Square(10) == False
assert dif_Square(15) == True </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 12
      8     return n % 4 != 3
     11 assert dif_Square(5) == True
---> 12 assert dif_Square(10) == False
     13 assert dif_Square(15) == True
AssertionError:  </pre>
### 304
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a python function to find element at a given index after number of rotations.

Your code should pass these tests:

assert find_Element([1,2,3,4,5],[[0,2],[0,3]],2,1) == 3
assert find_Element([1,2,3,4],[[0,1],[0,2]],1,2) == 3
assert find_Element([1,2,3,4,5,6],[[0,1],[0,2]],1,1) == 1

Your response should only contain the code for this function.

def find_Element(arr,ranges,rotations,index) :  
    ...


 </pre>
###### answer
<pre> ```python
def find_Element(arr, ranges, rotations, index):
    n = len(arr)
    
    # Create an array to store the net rotation effect on each position
    rotation_effect = [0]*n
    
    # Calculate the net rotation effect caused by each range
    for l, r in ranges:
        rotation_effect[l] += 1
        if r+1 &lt; n:
            rotation_effect[r+1] -= 1
            
    # Compute prefix sums to get the total rotation count at each position
    for i in range(1, n):
        rotation_effect[i] += rotation_effect[i-1]
        
    # Adjust the index based on the total rotation count modulo length
    adjusted_index = (index + rotation_effect[index]) % n
    
    return arr[adjusted_index]
``` </pre>
###### canonical_solution
<pre> def find_Element(arr,ranges,rotations,index) :  
    for i in range(rotations - 1,-1,-1 ) : 
        left = ranges[i][0] 
        right = ranges[i][1] 
        if (left &lt;= index and right >= index) : 
            if (index == left) : 
                index = right 
            else : 
                index = index - 1 
    return arr[index]  </pre>
###### test
<pre> assert find_Element([1,2,3,4,5],[[0,2],[0,3]],2,1) == 3
assert find_Element([1,2,3,4],[[0,1],[0,2]],1,2) == 3
assert find_Element([1,2,3,4,5,6],[[0,1],[0,2]],1,1) == 1 </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 29
     24     adjusted_index = (index + rotation_effect[index]) % n
     26     return arr[adjusted_index]
---> 29 assert find_Element([1,2,3,4,5],[[0,2],[0,3]],2,1) == 3
     30 assert find_Element([1,2,3,4],[[0,1],[0,2]],1,2) == 3
     31 assert find_Element([1,2,3,4,5,6],[[0,1],[0,2]],1,1) == 1
AssertionError:  </pre>
### 295
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to return the sum of all divisors of a number.

Your code should pass these tests:

assert sum_div(8)==7
assert sum_div(12)==16
assert sum_div(7)==1

Your response should only contain the code for this function.

def sum_div(number):
    ...


 </pre>
###### answer
<pre> ```python
def sum_div(number):
    total = 0
    for i in range(1, number + 1):
        if number % i == 0:
            total += i
    return total
``` </pre>
###### canonical_solution
<pre> def sum_div(number):
    divisors = [1]
    for i in range(2, number):
        if (number % i)==0:
            divisors.append(i)
    return sum(divisors) </pre>
###### test
<pre> assert sum_div(8)==7
assert sum_div(12)==16
assert sum_div(7)==1 </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 15
     11             total += i
     12     return total
---> 15 assert sum_div(8)==7
     16 assert sum_div(12)==16
     17 assert sum_div(7)==1
AssertionError:  </pre>
### 301
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to find the depth of a dictionary.

Your code should pass these tests:

assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4
assert dict_depth({'a':1, 'b': {'c':'python'}})==2
assert dict_depth({1: 'Sun', 2: {3: {4:'Mon'}}})==3

Your response should only contain the code for this function.

def dict_depth(d):
    ...


 </pre>
###### answer
<pre> ```python
def dict_depth(d):
    if not isinstance(d, dict) or not d:
        return 0
    
    max_depth = 1
    for key, value in d.items():
        if isinstance(value, dict):
            depth = dict_depth(value) + 1
            if depth > max_depth:
                max_depth = depth
                
    return max_depth
``` </pre>
###### canonical_solution
<pre> def dict_depth(d):
    if isinstance(d, dict):
        return 1 + (max(map(dict_depth, d.values())) if d else 0)
    return 0 </pre>
###### test
<pre> assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4
assert dict_depth({'a':1, 'b': {'c':'python'}})==2
assert dict_depth({1: 'Sun', 2: {3: {4:'Mon'}}})==3 </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 21
     16                 max_depth = depth
     18     return max_depth
---> 21 assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4
     22 assert dict_depth({'a':1, 'b': {'c':'python'}})==2
     23 assert dict_depth({1: 'Sun', 2: {3: {4:'Mon'}}})==3
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
    return sum(1/i for i in range(1, n))
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
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 13
      8     return sum(1/i for i in range(1, n))
     11 import math
---> 13 assert math.isclose(harmonic_sum(7), 2.5928571428571425, rel_tol=0.001)
     14 assert math.isclose(harmonic_sum(4), 2.083333333333333, rel_tol=0.001)
     15 assert math.isclose(harmonic_sum(19), 3.547739657143682, rel_tol=0.001)
AssertionError:  </pre>
### 255
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function that takes in a list and length n, and generates all combinations (with repetition) of the elements of the list and returns a list with a tuple for each combination.

Your code should pass these tests:

assert combinations_colors( ["Red","Green","Blue"],1)==[('Red',), ('Green',), ('Blue',)]
assert combinations_colors( ["Red","Green","Blue"],2)==[('Red', 'Red'), ('Red', 'Green'), ('Red', 'Blue'), ('Green', 'Green'), ('Green', 'Blue'), ('Blue', 'Blue')]
assert combinations_colors( ["Red","Green","Blue"],3)==[('Red', 'Red', 'Red'), ('Red', 'Red', 'Green'), ('Red', 'Red', 'Blue'), ('Red', 'Green', 'Green'), ('Red', 'Green', 'Blue'), ('Red', 'Blue', 'Blue'), ('Green', 'Green', 'Green'), ('Green', 'Green', 'Blue'), ('Green', 'Blue', 'Blue'), ('Blue', 'Blue', 'Blue')]

Your response should only contain the code for this function.

def combinations_colors(l, n):
    ...


 </pre>
###### answer
<pre> ```python
from itertools import product

def combinations_colors(l, n):
    return list(product(l, repeat=n))
``` </pre>
###### canonical_solution
<pre> from itertools import combinations_with_replacement 
def combinations_colors(l, n):
    return list(combinations_with_replacement(l,n))
 </pre>
###### test
<pre> assert combinations_colors( ["Red","Green","Blue"],1)==[('Red',), ('Green',), ('Blue',)]
assert combinations_colors( ["Red","Green","Blue"],2)==[('Red', 'Red'), ('Red', 'Green'), ('Red', 'Blue'), ('Green', 'Green'), ('Green', 'Blue'), ('Blue', 'Blue')]
assert combinations_colors( ["Red","Green","Blue"],3)==[('Red', 'Red', 'Red'), ('Red', 'Red', 'Green'), ('Red', 'Red', 'Blue'), ('Red', 'Green', 'Green'), ('Red', 'Green', 'Blue'), ('Red', 'Blue', 'Blue'), ('Green', 'Green', 'Green'), ('Green', 'Green', 'Blue'), ('Green', 'Blue', 'Blue'), ('Blue', 'Blue', 'Blue')] </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 14
     10     return list(product(l, repeat=n))
     13 assert combinations_colors( ["Red","Green","Blue"],1)==[('Red',), ('Green',), ('Blue',)]
---> 14 assert combinations_colors( ["Red","Green","Blue"],2)==[('Red', 'Red'), ('Red', 'Green'), ('Red', 'Blue'), ('Green', 'Green'), ('Green', 'Blue'), ('Blue', 'Blue')]
     15 assert combinations_colors( ["Red","Green","Blue"],3)==[('Red', 'Red', 'Red'), ('Red', 'Red', 'Green'), ('Red', 'Red', 'Blue'), ('Red', 'Green', 'Green'), ('Red', 'Green', 'Blue'), ('Red', 'Blue', 'Blue'), ('Green', 'Green', 'Green'), ('Green', 'Green', 'Blue'), ('Green', 'Blue', 'Blue'), ('Blue', 'Blue', 'Blue')]
AssertionError:  </pre>
### 461
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a python function to count the upper case characters in a given string.

Your code should pass these tests:

assert upper_ctr('PYthon') == 1
assert upper_ctr('BigData') == 1
assert upper_ctr('program') == 0

Your response should only contain the code for this function.

def upper_ctr(str):
    ...


 </pre>
###### answer
<pre> ```python
def upper_ctr(s):
    return sum(1 for char in s if char.isupper())
``` </pre>
###### canonical_solution
<pre> def upper_ctr(str):
    upper_ctr = 0
    for i in range(len(str)):
          if str[i] >= 'A' and str[i] &lt;= 'Z': upper_ctr += 1
          return upper_ctr </pre>
###### test
<pre> assert upper_ctr('PYthon') == 1
assert upper_ctr('BigData') == 1
assert upper_ctr('program') == 0 </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 11
      7 def upper_ctr(s):
      8     return sum(1 for char in s if char.isupper())
---> 11 assert upper_ctr('PYthon') == 1
     12 assert upper_ctr('BigData') == 1
     13 assert upper_ctr('program') == 0
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
    result = {}
    
    # Add all items from dict1
    result.update(dict1)
    
    # Add all items from dict2, overwriting any duplicates
    result.update(dict2)
    
    # Add all items from dict3, overwriting any duplicates
    result.update(dict3)
    
    return result
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
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 23
     19     return result
     22 assert merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" }, { "G": "Green", "W": "White" },{ "O": "Orange", "W": "White", "B": "Black" })=={'B': 'Black', 'R': 'Red', 'P': 'Pink', 'G': 'Green', 'W': 'White', 'O': 'Orange'}
---> 23 assert merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" }, { "G": "Green", "W": "White" },{"L":"lavender","B":"Blue"})=={'W': 'White', 'P': 'Pink', 'B': 'Black', 'R': 'Red', 'G': 'Green', 'L': 'lavender'}
     24 assert merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" },{"L":"lavender","B":"Blue"},{ "G": "Green", "W": "White" })=={'B': 'Black', 'P': 'Pink', 'R': 'Red', 'G': 'Green', 'L': 'lavender', 'W': 'White'}
AssertionError:  </pre>
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
### 228
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a python function to check whether all the bits are unset in the given range or not.

Your code should pass these tests:

assert all_Bits_Set_In_The_Given_Range(4,1,2) == True
assert all_Bits_Set_In_The_Given_Range(17,2,4) == True
assert all_Bits_Set_In_The_Given_Range(39,4,6) == False

Your response should only contain the code for this function.

def all_Bits_Set_In_The_Given_Range(n,l,r):  
    ...


 </pre>
###### answer
<pre> ```python
def all_Bits_Set_In_The_Given_Range(n, l, r):
    # Create a mask with bits set in the specified range [l, r]
    mask = ((1 &lt;&lt; (r - l + 1)) - 1) &lt;&lt; (l - 1)
    
    # Check if all bits in the range are set by performing bitwise AND operation
    return (n & mask) == mask
``` </pre>
###### canonical_solution
<pre> def all_Bits_Set_In_The_Given_Range(n,l,r):  
    num = (((1 &lt;&lt; r) - 1) ^ ((1 &lt;&lt; (l - 1)) - 1)) 
    new_num = n & num
    if (new_num == 0): 
        return True
    return False </pre>
###### test
<pre> assert all_Bits_Set_In_The_Given_Range(4,1,2) == True
assert all_Bits_Set_In_The_Given_Range(17,2,4) == True
assert all_Bits_Set_In_The_Given_Range(39,4,6) == False </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 15
     11     # Check if all bits in the range are set by performing bitwise AND operation
     12     return (n & mask) == mask
---> 15 assert all_Bits_Set_In_The_Given_Range(4,1,2) == True
     16 assert all_Bits_Set_In_The_Given_Range(17,2,4) == True
     17 assert all_Bits_Set_In_The_Given_Range(39,4,6) == False
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
    result = negatives + positives + arr[n:]
    
    return result
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
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 15
     10     result = negatives + positives + arr[n:]
     12     return result
---> 15 assert re_arrange_array([-1, 2, -3, 4, 5, 6, -7, 8, 9], 9) == [-1, -3, -7, 4, 5, 6, 2, 8, 9]
     16 assert re_arrange_array([12, -14, -26, 13, 15], 5) == [-14, -26, 12, 13, 15]
     17 assert re_arrange_array([10, 24, 36, -42, -39, -78, 85], 7) == [-42, -39, -78, 10, 24, 36, 85]
AssertionError:  </pre>
### 448
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to calculate the sum of perrin numbers.

Your code should pass these tests:

assert cal_sum(9) == 49
assert cal_sum(10) == 66
assert cal_sum(11) == 88

Your response should only contain the code for this function.

def cal_sum(n): 
    ...


 </pre>
###### answer
<pre> ```python
def cal_sum(n):
    if n &lt;= 0:
        return 0
    
    # Initialize Perrin sequence with base cases
    perrin = [3, 0, 2]
    
    # Calculate Perrin numbers up to n
    for i in range(3, n + 1):
        next_perrin = perrin[i-3] + perrin[i-2]
        perrin.append(next_perrin)
        
    # Return the sum of first n Perrin numbers
    return sum(perrin[:n])
``` </pre>
###### canonical_solution
<pre> def cal_sum(n): 
	a = 3
	b = 0
	c = 2
	if (n == 0): 
		return 3
	if (n == 1): 
		return 3
	if (n == 2): 
		return 5
	sum = 5
	while (n > 2): 
		d = a + b 
		sum = sum + d 
		a = b 
		b = c 
		c = d 
		n = n-1
	return sum </pre>
###### test
<pre> assert cal_sum(9) == 49
assert cal_sum(10) == 66
assert cal_sum(11) == 88 </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 23
     19     # Return the sum of first n Perrin numbers
     20     return sum(perrin[:n])
---> 23 assert cal_sum(9) == 49
     24 assert cal_sum(10) == 66
     25 assert cal_sum(11) == 88
AssertionError:  </pre>
### 74
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to check whether it follows the sequence given in the patterns array.

Your code should pass these tests:

assert is_samepatterns(["red","green","green"], ["a", "b", "b"])==True
assert is_samepatterns(["red","green","greenn"], ["a","b","b"])==False
assert is_samepatterns(["red","green","greenn"], ["a","b"])==False

Your response should only contain the code for this function.

def is_samepatterns(colors, patterns):    
    ...


 </pre>
###### answer
<pre> ```python
def is_samepatterns(colors, patterns):
    if len(colors) != len(patterns):
        return False
        
    color_to_pattern = {}
    pattern_to_color = {}
    
    for c, p in zip(colors, patterns):
        if c in color_to_pattern and color_to_pattern[c] != p:
            return False
        if p in pattern_to_pattern and pattern_to_color[p] != c:
            return False
            
        color_to_pattern[c] = p
        pattern_to_color[p] = c
            
    return True
``` </pre>
###### canonical_solution
<pre> def is_samepatterns(colors, patterns):    
    if len(colors) != len(patterns):
        return False    
    sdict = {}
    pset = set()
    sset = set()    
    for i in range(len(patterns)):
        pset.add(patterns[i])
        sset.add(colors[i])
        if patterns[i] not in sdict.keys():
            sdict[patterns[i]] = []

        keys = sdict[patterns[i]]
        keys.append(colors[i])
        sdict[patterns[i]] = keys

    if len(pset) != len(sset):
        return False   

    for values in sdict.values():

        for i in range(len(values) - 1):
            if values[i] != values[i+1]:
                return False

    return True </pre>
###### test
<pre> assert is_samepatterns(["red","green","green"], ["a", "b", "b"])==True
assert is_samepatterns(["red","green","greenn"], ["a","b","b"])==False
assert is_samepatterns(["red","green","greenn"], ["a","b"])==False </pre>
###### traceback
<pre> ---------------------------------------------------------------------------NameError                                 Traceback (most recent call last)Cell In[1], line 26
     21         pattern_to_color[p] = c
     23     return True
---> 26 assert is_samepatterns(["red","green","green"], ["a", "b", "b"])==True
     27 assert is_samepatterns(["red","green","greenn"], ["a","b","b"])==False
     28 assert is_samepatterns(["red","green","greenn"], ["a","b"])==False
Cell In[1], line 17, in is_samepatterns(colors, patterns)
     15 if c in color_to_pattern and color_to_pattern[c] != p:
     16     return False
---> 17 if p in pattern_to_pattern and pattern_to_color[p] != c:
     18     return False
     20 color_to_pattern[c] = p
NameError: name 'pattern_to_pattern' is not defined </pre>
### 70
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to find whether all the given tuples have equal length or not.

Your code should pass these tests:

assert get_equal([(11, 22, 33), (44, 55, 66)]) == True
assert get_equal([(1, 2, 3), (4, 5, 6, 7)]) == False
assert get_equal([(1, 2), (3, 4)]) == True

Your response should only contain the code for this function.

def find_equal_tuple(Input):
    ...


 </pre>
###### answer
<pre> ```python
def find_equal(Input):
    return len(set(len(tup) for tup in Input)) == 1
``` </pre>
###### canonical_solution
<pre> def find_equal_tuple(Input):
  k = 0 if not Input else len(Input[0])
  flag = 1
  for tuple in Input:
    if len(tuple) != k:
      flag = 0
      break
  return flag
def get_equal(Input):
  return find_equal_tuple(Input) == 1 </pre>
###### test
<pre> assert get_equal([(11, 22, 33), (44, 55, 66)]) == True
assert get_equal([(1, 2, 3), (4, 5, 6, 7)]) == False
assert get_equal([(1, 2), (3, 4)]) == True </pre>
###### traceback
<pre> ---------------------------------------------------------------------------NameError                                 Traceback (most recent call last)Cell In[1], line 11
      7 def find_equal(Input):
      8     return len(set(len(tup) for tup in Input)) == 1
---> 11 assert get_equal([(11, 22, 33), (44, 55, 66)]) == True
     12 assert get_equal([(1, 2, 3), (4, 5, 6, 7)]) == False
     13 assert get_equal([(1, 2), (3, 4)]) == True
NameError: name 'get_equal' is not defined </pre>
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
    if n == 0: return 1
    
    # Find position of leftmost unset bit
    pos = 0
    num = n
    while (num > 0):
        if ((num & 1) == 0):
            break
        num >>= 1
        pos += 1
        
    # Set the leftmost unset bit
    if (pos >= 0):
        n |= (1 &lt;&lt; pos)
        
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
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 26
     21         n |= (1 &lt;&lt; pos)
     23     return n
---> 26 assert set_left_most_unset_bit(10) == 14
     27 assert set_left_most_unset_bit(12) == 14
     28 assert set_left_most_unset_bit(15) == 15
AssertionError:  </pre>
### 398
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to compute the sum of digits of each number of a given list.

Your code should pass these tests:

assert sum_of_digits([10,2,56])==14
assert sum_of_digits([[10,20,4,5,'b',70,'a']])==19
assert sum_of_digits([10,20,-4,5,-70])==19

Your response should only contain the code for this function.

def sum_of_digits(nums):
    ...


 </pre>
###### answer
<pre> ```python
def sum_of_digits(nums):
    total_sum = 0
    
    for num in nums:
        if isinstance(num, int): 
            abs_num = abs(num)
            while abs_num > 0:
                digit = abs_num % 10
                total_sum += digit
                abs_num //= 10
                
    return total_sum
``` </pre>
###### canonical_solution
<pre> def sum_of_digits(nums):
    return sum(int(el) for n in nums for el in str(n) if el.isdigit()) </pre>
###### test
<pre> assert sum_of_digits([10,2,56])==14
assert sum_of_digits([[10,20,4,5,'b',70,'a']])==19
assert sum_of_digits([10,20,-4,5,-70])==19 </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 22
     18     return total_sum
     21 assert sum_of_digits([10,2,56])==14
---> 22 assert sum_of_digits([[10,20,4,5,'b',70,'a']])==19
     23 assert sum_of_digits([10,20,-4,5,-70])==19
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
    return n > 0 and (n & (n - 1)) == 0
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
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 11
      7 def is_Sum_Of_Powers_Of_Two(n):
      8     return n > 0 and (n & (n - 1)) == 0
---> 11 assert is_Sum_Of_Powers_Of_Two(10) == True
     12 assert is_Sum_Of_Powers_Of_Two(7) == False
     13 assert is_Sum_Of_Powers_Of_Two(14) == True
AssertionError:  </pre>
