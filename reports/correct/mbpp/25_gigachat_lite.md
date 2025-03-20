# mbpp / gigachat-2-lite
### 233
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to find the lateral surface area of a cylinder.

Your code should pass these tests:

import math

assert math.isclose(lateralsuface_cylinder(10,5), 314.15000000000003, rel_tol=0.001)
assert math.isclose(lateralsuface_cylinder(4,5), 125.66000000000001, rel_tol=0.001)
assert math.isclose(lateralsuface_cylinder(4,10), 251.32000000000002, rel_tol=0.001)

Your response should only contain the code for this function.

def lateralsuface_cylinder(r,h):
    ...


 </pre>
###### answer
<pre> The lateral surface area (also known as the side area) of a cylinder can be calculated using the formula: 

$$ A = 2\pi rh $$

where $ r $ is the radius of the base circle and $ h $ is the height of the cylinder.

Here’s how we will implement it in Python:

```python
import math

def lateralsuface_cylinder(r, h):
    return 2 * math.pi * r * h
```

This function takes two arguments `r` (radius) and `h` (height) and returns the lateral surface area based on the given formula. </pre>
###### canonical_solution
<pre> def lateralsuface_cylinder(r,h):
  lateralsurface= 2*3.1415*r*h
  return lateralsurface </pre>
###### test
<pre> import math

assert math.isclose(lateralsuface_cylinder(10,5), 314.15000000000003, rel_tol=0.001)
assert math.isclose(lateralsuface_cylinder(4,5), 125.66000000000001, rel_tol=0.001)
assert math.isclose(lateralsuface_cylinder(4,10), 251.32000000000002, rel_tol=0.001) </pre>
### 465
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to drop empty items from a given dictionary.

Your code should pass these tests:

assert drop_empty({'c1': 'Red', 'c2': 'Green', 'c3':None})=={'c1': 'Red', 'c2': 'Green'}
assert drop_empty({'c1': 'Red', 'c2': None, 'c3':None})=={'c1': 'Red'}
assert drop_empty({'c1': None, 'c2': 'Green', 'c3':None})=={ 'c2': 'Green'}

Your response should only contain the code for this function.

def drop_empty(dict1):
    ...


 </pre>
###### answer
<pre> ```python
def drop_empty(dict1):
    return {key: value for key, value in dict1.items() if value is not None}
``` </pre>
###### canonical_solution
<pre> def drop_empty(dict1):
  dict1 = {key:value for (key, value) in dict1.items() if value is not None}
  return dict1 </pre>
###### test
<pre> assert drop_empty({'c1': 'Red', 'c2': 'Green', 'c3':None})=={'c1': 'Red', 'c2': 'Green'}
assert drop_empty({'c1': 'Red', 'c2': None, 'c3':None})=={'c1': 'Red'}
assert drop_empty({'c1': None, 'c2': 'Green', 'c3':None})=={ 'c2': 'Green'} </pre>
### 14
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a python function to find the volume of a triangular prism.

Your code should pass these tests:

assert find_Volume(10,8,6) == 240
assert find_Volume(3,2,2) == 6
assert find_Volume(1,2,1) == 1

Your response should only contain the code for this function.

def find_Volume(l,b,h) : 
    ...


 </pre>
###### answer
<pre> ```python
def find_Volume(l, b, h):
    return (l * b * h) / 2
``` </pre>
###### canonical_solution
<pre> def find_Volume(l,b,h) : 
    return ((l * b * h) / 2)  </pre>
###### test
<pre> assert find_Volume(10,8,6) == 240
assert find_Volume(3,2,2) == 6
assert find_Volume(1,2,1) == 1 </pre>
### 80
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to find the nth tetrahedral number.

Your code should pass these tests:

assert tetrahedral_number(5) == 35
assert tetrahedral_number(6) == 56
assert tetrahedral_number(7) == 84

Your response should only contain the code for this function.

def tetrahedral_number(n): 
    ...


 </pre>
###### answer
<pre> A tetrahedral number is the sum of the first $n$ triangular numbers, or equivalently, it can be calculated using the formula: $T_n = \frac{n(n+1)(n+2)}{6}$.

Here’s how we can write the function based on that formula:

```python
def tetrahedral_number(n):
    return n * (n + 1) * (n + 2) // 6
```

This implementation directly computes the value according to the formula without needing any loops or recursion. </pre>
###### canonical_solution
<pre> def tetrahedral_number(n): 
	return (n * (n + 1) * (n + 2)) / 6 </pre>
###### test
<pre> assert tetrahedral_number(5) == 35
assert tetrahedral_number(6) == 56
assert tetrahedral_number(7) == 84 </pre>
### 312
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to find the volume of a cone.

Your code should pass these tests:

import math

assert math.isclose(volume_cone(5,12), 314.15926535897927, rel_tol=0.001)
assert math.isclose(volume_cone(10,15), 1570.7963267948965, rel_tol=0.001)
assert math.isclose(volume_cone(19,17), 6426.651371693521, rel_tol=0.001)

Your response should only contain the code for this function.

def volume_cone(r,h):
    ...


 </pre>
###### answer
<pre> ```python
import math

def volume_cone(r, h):
    return (math.pi * r ** 2 * h) / 3
``` </pre>
###### canonical_solution
<pre> import math
def volume_cone(r,h):
  volume = (1.0/3) * math.pi * r * r * h
  return volume </pre>
###### test
<pre> import math

assert math.isclose(volume_cone(5,12), 314.15926535897927, rel_tol=0.001)
assert math.isclose(volume_cone(10,15), 1570.7963267948965, rel_tol=0.001)
assert math.isclose(volume_cone(19,17), 6426.651371693521, rel_tol=0.001) </pre>
### 230
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function that takes in a string and character, replaces blank spaces in the string with the character, and returns the string.

Your code should pass these tests:

assert replace_blank("hello people",'@')==("hello@people")
assert replace_blank("python program language",'$')==("python$program$language")
assert replace_blank("blank space","-")==("blank-space")

Your response should only contain the code for this function.

def replace_blank(str1,char):
    ...


 </pre>
###### answer
<pre> ```python
def replace_blank(str1, char):
    return str1.replace(' ', char)
``` </pre>
###### canonical_solution
<pre> def replace_blank(str1,char):
 str2 = str1.replace(' ', char)
 return str2 </pre>
###### test
<pre> assert replace_blank("hello people",'@')==("hello@people")
assert replace_blank("python program language",'$')==("python$program$language")
assert replace_blank("blank space","-")==("blank-space") </pre>
### 135
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to find the nth hexagonal number.

Your code should pass these tests:

assert hexagonal_num(10) == 190
assert hexagonal_num(5) == 45
assert hexagonal_num(7) == 91

Your response should only contain the code for this function.

def hexagonal_num(n): 
    ...


 </pre>
###### answer
<pre> To calculate the $n$-th hexagonal number, we can use the formula derived from the properties of hexagonal numbers: 

$$H_n = n \cdot (2n - 1)$$

This is because each hexagonal number is formed by adding consecutive integers in a specific pattern that follows this formula.

Here’s how you can write the function based on this formula:

```python
def hexagonal_num(n):
    return n * (2 * n - 1)
```

### Explanation:
- The input `n` represents the position of the hexagonal number in the sequence.
- We multiply `n` by `(2 * n - 1)` to get the corresponding hexagonal number.

### Example usage:
- For `hexagonal_num(10)`, it returns `190`.
- For `hexagonal_num(5)`, it returns `45`.
- For `hexagonal_num(7)`, it returns `91`. </pre>
###### canonical_solution
<pre> def hexagonal_num(n): 
	return n*(2*n - 1)  </pre>
###### test
<pre> assert hexagonal_num(10) == 190
assert hexagonal_num(5) == 45
assert hexagonal_num(7) == 91 </pre>
### 433
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to check whether the entered number is greater than the elements of the given array.

Your code should pass these tests:

assert check_greater([1, 2, 3, 4, 5], 4) == False
assert check_greater([2, 3, 4, 5, 6], 8) == True
assert check_greater([9, 7, 4, 8, 6, 1], 11) == True

Your response should only contain the code for this function.

def check_greater(arr, number):
    ...


 </pre>
###### answer
<pre> ```python
def check_greater(arr, number):
    return all(x &lt; number for x in arr)
``` </pre>
###### canonical_solution
<pre> def check_greater(arr, number):
  arr.sort()
  return number > arr[-1] </pre>
###### test
<pre> assert check_greater([1, 2, 3, 4, 5], 4) == False
assert check_greater([2, 3, 4, 5, 6], 8) == True
assert check_greater([9, 7, 4, 8, 6, 1], 11) == True </pre>
### 170
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to find the sum of numbers in a list within a range specified by two indices.

Your code should pass these tests:

assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 8, 10) == 29
assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 5, 7) == 16
assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 7, 10) == 38

Your response should only contain the code for this function.

def sum_range_list(list1, m, n):                                                                                                                                                                                                
    ...


 </pre>
###### answer
<pre> ```python
def sum_range_list(list1, m, n):
    return sum(list1[m:n+1])
``` </pre>
###### canonical_solution
<pre> def sum_range_list(list1, m, n):                                                                                                                                                                                                
    sum_range = 0                                                                                                                                                                                                         
    for i in range(m, n+1, 1):                                                                                                                                                                                        
        sum_range += list1[i]                                                                                                                                                                                                  
    return sum_range    </pre>
###### test
<pre> assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 8, 10) == 29
assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 5, 7) == 16
assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 7, 10) == 38 </pre>
### 420
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a python function to find the cube sum of first n even natural numbers.

Your code should pass these tests:

assert cube_Sum(2) == 72
assert cube_Sum(3) == 288
assert cube_Sum(4) == 800

Your response should only contain the code for this function.

def cube_Sum(n): 
    ...


 </pre>
###### answer
<pre> ```python
def cube_Sum(n):
    return sum(i**3 for i in range(2, 2*n+1, 2))
``` </pre>
###### canonical_solution
<pre> def cube_Sum(n): 
    sum = 0
    for i in range(1,n + 1): 
        sum += (2*i)*(2*i)*(2*i) 
    return sum </pre>
###### test
<pre> assert cube_Sum(2) == 72
assert cube_Sum(3) == 288
assert cube_Sum(4) == 800 </pre>
