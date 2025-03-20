# mbpp / vikhr-yandexgpt-8b
### 142
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to count number items that are identical in the same position of three given lists.

Your code should pass these tests:

assert count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,9],[2,1,3,1,2,6,7,9])==3
assert count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,8],[2,1,3,1,2,6,7,8])==4
assert count_samepair([1,2,3,4,2,6,7,8],[2,2,3,1,2,6,7,8],[2,1,3,1,2,6,7,8])==5

Your response should only contain the code for this function.

def count_samepair(list1,list2,list3):
    ...


 </pre>
###### answer
<pre> ```python
def count_samepair(list1, list2, list3):
    count = 0
    for i in range(len(list1)):
        if list1[i] == list2[i] == list3[i]:
            count += 1
    return count
``` </pre>
###### canonical_solution
<pre> def count_samepair(list1,list2,list3):
    result = sum(m == n == o for m, n, o in zip(list1,list2,list3))
    return result </pre>
###### test
<pre> assert count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,9],[2,1,3,1,2,6,7,9])==3
assert count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,8],[2,1,3,1,2,6,7,8])==4
assert count_samepair([1,2,3,4,2,6,7,8],[2,2,3,1,2,6,7,8],[2,1,3,1,2,6,7,8])==5 </pre>
### 246
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function for computing square roots using the babylonian method.

Your code should pass these tests:

import math

assert math.isclose(babylonian_squareroot(10), 3.162277660168379, rel_tol=0.001)
assert math.isclose(babylonian_squareroot(2), 1.414213562373095, rel_tol=0.001)
assert math.isclose(babylonian_squareroot(9), 3.0, rel_tol=0.001)

Your response should only contain the code for this function.

def babylonian_squareroot(number):
    ...


 </pre>
###### answer
<pre> ```python
def babylonian_squareroot(number):
    if number &lt; 0:
        raise ValueError("Cannot compute the square root of a negative number.")
    if number == 0:
        return 0
    
    guess = number / 2.0
    while True:
        new_guess = (guess + number / guess) / 2.0
        if math.isclose(new_guess, guess, rel_tol=0.001):
            return new_guess
        guess = new_guess
``` </pre>
###### canonical_solution
<pre> def babylonian_squareroot(number):
    if(number == 0):
        return 0;
    g = number/2.0;
    g2 = g + 1;
    while(g != g2):
        n = number/ g;
        g2 = g;
        g = (g + n)/2;
    return g; </pre>
###### test
<pre> import math

assert math.isclose(babylonian_squareroot(10), 3.162277660168379, rel_tol=0.001)
assert math.isclose(babylonian_squareroot(2), 1.414213562373095, rel_tol=0.001)
assert math.isclose(babylonian_squareroot(9), 3.0, rel_tol=0.001) </pre>
### 267
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a python function that takes in an integer n and returns the sum of the squares of the first n odd natural numbers.

Your code should pass these tests:

assert square_Sum(2) == 10
assert square_Sum(3) == 35
assert square_Sum(4) == 84

Your response should only contain the code for this function.

def square_Sum(n):  
    ...


 </pre>
###### answer
<pre> ```python
def square_Sum(n):
    return sum(i**2 for i in range(1, 2*n, 2))
``` </pre>
###### canonical_solution
<pre> def square_Sum(n):  
    return int(n*(4*n*n-1)/3)  </pre>
###### test
<pre> assert square_Sum(2) == 10
assert square_Sum(3) == 35
assert square_Sum(4) == 84 </pre>
### 19
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to find whether a given array of integers contains any duplicate element.

Your code should pass these tests:

assert test_duplicate(([1,2,3,4,5]))==False
assert test_duplicate(([1,2,3,4, 4]))==True
assert test_duplicate([1,1,2,2,3,3,4,4,5])==True

Your response should only contain the code for this function.

def test_duplicate(arraynums):
    ...


 </pre>
###### answer
<pre> ```python
def test_duplicate(array_nums):
    return len(array_nums) != len(set(array_nums))
``` </pre>
###### canonical_solution
<pre> def test_duplicate(arraynums):
    nums_set = set(arraynums)    
    return len(arraynums) != len(nums_set)      </pre>
###### test
<pre> assert test_duplicate(([1,2,3,4,5]))==False
assert test_duplicate(([1,2,3,4, 4]))==True
assert test_duplicate([1,1,2,2,3,3,4,4,5])==True </pre>
### 293
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to find the third side of a right angled triangle.

Your code should pass these tests:

assert otherside_rightangle(7,8)==10.63014581273465
assert otherside_rightangle(3,4)==5
assert otherside_rightangle(7,15)==16.55294535724685

Your response should only contain the code for this function.

def otherside_rightangle(w,h):
    ...


 </pre>
###### answer
<pre> ```python
import math

def otherside_rightangle(w, h):
    return math.sqrt(w**2 + h**2)
``` </pre>
###### canonical_solution
<pre> import math
def otherside_rightangle(w,h):
  s=math.sqrt((w*w)+(h*h))
  return s </pre>
###### test
<pre> assert otherside_rightangle(7,8)==10.63014581273465
assert otherside_rightangle(3,4)==5
assert otherside_rightangle(7,15)==16.55294535724685 </pre>
### 224
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a python function to count the number of set bits (binary digits with value 1) in a given number.

Your code should pass these tests:

assert count_Set_Bits(2) == 1
assert count_Set_Bits(4) == 1
assert count_Set_Bits(6) == 2

Your response should only contain the code for this function.

def count_Set_Bits(n): 
    ...


 </pre>
###### answer
<pre> ```python
def count_Set_Bits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count
``` </pre>
###### canonical_solution
<pre> def count_Set_Bits(n): 
    count = 0
    while (n): 
        count += n & 1
        n >>= 1
    return count  </pre>
###### test
<pre> assert count_Set_Bits(2) == 1
assert count_Set_Bits(4) == 1
assert count_Set_Bits(6) == 2 </pre>
### 390
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to apply a given format string to all of the elements in a list.

Your code should pass these tests:

assert add_string([1,2,3,4],'temp{0}')==['temp1', 'temp2', 'temp3', 'temp4']
assert add_string(['a','b','c','d'], 'python{0}')==[ 'pythona', 'pythonb', 'pythonc', 'pythond']
assert add_string([5,6,7,8],'string{0}')==['string5', 'string6', 'string7', 'string8']

Your response should only contain the code for this function.

def add_string(list_, string):
    ...


 </pre>
###### answer
<pre> ```python
def add_string(list_, string):
    return [string.format(item) for item in list_]
``` </pre>
###### canonical_solution
<pre> def add_string(list_, string):
 add_string=[string.format(i) for i in  list_]
 return add_string </pre>
###### test
<pre> assert add_string([1,2,3,4],'temp{0}')==['temp1', 'temp2', 'temp3', 'temp4']
assert add_string(['a','b','c','d'], 'python{0}')==[ 'pythona', 'pythonb', 'pythonc', 'pythond']
assert add_string([5,6,7,8],'string{0}')==['string5', 'string6', 'string7', 'string8'] </pre>
### 271
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a python function that takes in an integer n and finds the sum of the first n even natural numbers that are raised to the fifth power.

Your code should pass these tests:

assert even_Power_Sum(2) == 1056
assert even_Power_Sum(3) == 8832
assert even_Power_Sum(1) == 32

Your response should only contain the code for this function.

def even_Power_Sum(n): 
    ...


 </pre>
###### answer
<pre> ```python
def even_Power_Sum(n):
    sum = 0
    for i in range(1, n + 1):
        even_number = 2 * i
        sum += even_number ** 5
    return sum
``` </pre>
###### canonical_solution
<pre> def even_Power_Sum(n): 
    sum = 0; 
    for i in range(1,n+1): 
        j = 2*i; 
        sum = sum + (j*j*j*j*j); 
    return sum;  </pre>
###### test
<pre> assert even_Power_Sum(2) == 1056
assert even_Power_Sum(3) == 8832
assert even_Power_Sum(1) == 32 </pre>
### 458
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to find the area of a rectangle.

Your code should pass these tests:

assert rectangle_area(10,20)==200
assert rectangle_area(10,5)==50
assert rectangle_area(4,2)==8

Your response should only contain the code for this function.

def rectangle_area(l,b):
    ...


 </pre>
###### answer
<pre> ```python
def rectangle_area(l, b):
    return l * b
``` </pre>
###### canonical_solution
<pre> def rectangle_area(l,b):
  area=l*b
  return area </pre>
###### test
<pre> assert rectangle_area(10,20)==200
assert rectangle_area(10,5)==50
assert rectangle_area(4,2)==8 </pre>
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
    # The first two years of a dog's life are equivalent to 10.5 human years each.
    # After that, each year of a dog's life is equivalent to 4 human years.
    if h_age &lt;= 2:
        return h_age * 10.5
    else:
        return 21 + (h_age - 2) * 4
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
