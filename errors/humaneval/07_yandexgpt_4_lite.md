# humaneval / yandexgpt-4-lite
### HumanEval/6
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.
from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
 </pre>
###### answer
<pre> ```
def parse_nested_parens(paren_string: str) -> List[int]:
    result = []
    stack = []

    for char in paren_string:
        if char == '(':
            stack.append(1)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                result.append(0)
        else:
            result.append(0)

    while stack:
        result.append(max(stack))
        stack.pop()

    return result
``` </pre>
###### pred
<pre> 
def parse_nested_parens(paren_string: str) -> List[int]:
    result = []
    stack = []

    for char in paren_string:
        if char == '(':
            stack.append(1)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                result.append(0)
        else:
            result.append(0)

    while stack:
        result.append(max(stack))
        stack.pop()

    return result
 </pre>
###### canonical_solution
<pre>     def parse_paren_group(s):
        depth = 0
        max_depth = 0
        for c in s:
            if c == '(':
                depth += 1
                max_depth = max(depth, max_depth)
            else:
                depth -= 1

        return max_depth

    return [parse_paren_group(x) for x in paren_string.split(' ') if x]
 </pre>
###### test
<pre> 

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('(()()) ((())) () ((())()())') == [2, 3, 1, 3]
    assert candidate('() (()) ((())) (((())))') == [1, 2, 3, 4]
    assert candidate('(()(())((())))') == [4]
 </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 52
     48     assert candidate('() (()) ((())) (((())))') == [1, 2, 3, 4]
     49     assert candidate('(()(())((())))') == [4]
---> 52 check(parse_nested_parens)
Cell In[1], line 47, in check(candidate)
     46 def check(candidate):
---> 47     assert candidate('(()()) ((())) () ((())()())') == [2, 3, 1, 3]
     48     assert candidate('() (()) ((())) (((())))') == [1, 2, 3, 4]
     49     assert candidate('(()(())((())))') == [4]
AssertionError:  </pre>
### HumanEval/71
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.

def triangle_area(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return the area of
    the triangle rounded to 2 decimal points if the three sides form a valid triangle. 
    Otherwise return -1
    Three sides make a valid triangle when the sum of any two sides is greater 
    than the third side.
    Example:
    triangle_area(3, 4, 5) == 6.00
    triangle_area(1, 2, 10) == -1
    '''
 </pre>
###### answer
<pre> ```
def triangle_area(a, b, c):
    # Проверяем, можно ли составить треугольник из сторон a, b и c
    if a + b > c and a + c > b and b + c > a:
        # Вычисляем площадь треугольника по формуле Герона
        p = (a + b + c) / 2
        area = sqrt(p * (p - a) * (p - b) * (p - c))
        return round(area, 2)
    else:
        return -1
``` </pre>
###### pred
<pre> 
def triangle_area(a, b, c):
    # Проверяем, можно ли составить треугольник из сторон a, b и c
    if a + b > c and a + c > b and b + c > a:
        # Вычисляем площадь треугольника по формуле Герона
        p = (a + b + c) / 2
        area = sqrt(p * (p - a) * (p - b) * (p - c))
        return round(area, 2)
    else:
        return -1
 </pre>
###### canonical_solution
<pre>     if a + b <= c or a + c <= b or b + c <= a:
        return -1 
    s = (a + b + c)/2    
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    area = round(area, 2)
    return area
 </pre>
###### test
<pre> def check(candidate):

    # Check some simple cases
    assert candidate(3, 4, 5) == 6.00, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate(1, 2, 10) == -1
    assert candidate(4, 8, 5) == 8.18
    assert candidate(2, 2, 2) == 1.73
    assert candidate(1, 2, 3) == -1
    assert candidate(10, 5, 7) == 16.25
    assert candidate(2, 6, 3) == -1

    # Check some edge cases that are easy to work out by hand.
    assert candidate(1, 1, 1) == 0.43, "This prints if this assert fails 2 (also good for debugging!)"
    assert candidate(2, 2, 10) == -1

 </pre>
###### traceback
<pre> ---------------------------------------------------------------------------NameError                                 Traceback (most recent call last)Cell In[1], line 45
     40     assert candidate(1, 1, 1) == 0.43, "This prints if this assert fails 2 (also good for debugging!)"
     41     assert candidate(2, 2, 10) == -1
---> 45 check(triangle_area)
Cell In[1], line 31, in check(candidate)
     28 def check(candidate):
     29 
     30     # Check some simple cases
---> 31     assert candidate(3, 4, 5) == 6.00, "This prints if this assert fails 1 (good for debugging!)"
     32     assert candidate(1, 2, 10) == -1
     33     assert candidate(4, 8, 5) == 8.18
Cell In[1], line 22, in triangle_area(a, b, c)
     19 if a + b > c and a + c > b and b + c > a:
     20     # Вычисляем площадь треугольника по формуле Герона
     21     p = (a + b + c) / 2
---> 22     area = sqrt(p * (p - a) * (p - b) * (p - c))
     23     return round(area, 2)
     24 else:
NameError: name 'sqrt' is not defined </pre>
### HumanEval/94
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.


def skjkasdkd(lst):
    """You are given a list of integers.
    You need to find the largest prime value and return the sum of its digits.

    Examples:
    For lst = [0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3] the output should be 10
    For lst = [1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1] the output should be 25
    For lst = [1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3] the output should be 13
    For lst = [0,724,32,71,99,32,6,0,5,91,83,0,5,6] the output should be 11
    For lst = [0,81,12,3,1,21] the output should be 3
    For lst = [0,8,1,2,1,7] the output should be 7
    """
 </pre>
###### answer
<pre> ```
def skjkasdkd(lst):
    largest_prime = max(lst)
    while largest_prime % 2 == 0:
        largest_prime += 1
    # Проверяем, является ли число простым
    for i in range(2, int(largest_prime ** 0.5) + 1):
        if largest_prime % i == 0:
            return False
    return sum(int(digit) for digit in str(largest_prime))
``` </pre>
###### pred
<pre> 
def skjkasdkd(lst):
    largest_prime = max(lst)
    while largest_prime % 2 == 0:
        largest_prime += 1
    # Проверяем, является ли число простым
    for i in range(2, int(largest_prime ** 0.5) + 1):
        if largest_prime % i == 0:
            return False
    return sum(int(digit) for digit in str(largest_prime))
 </pre>
###### canonical_solution
<pre>     def isPrime(n):
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False

        return True
    maxx = 0
    i = 0
    while i < len(lst):
        if(lst[i] > maxx and isPrime(lst[i])):
            maxx = lst[i]
        i+=1
    result = sum(int(digit) for digit in str(maxx))
    return result

 </pre>
###### test
<pre> def check(candidate):

    # Check some simple cases
    assert candidate([0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3]) == 10, "This prints if this assert fails 1 (good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    assert candidate([1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1]) == 25, "This prints if this assert fails 2 (also good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    assert candidate([1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3]) == 13, "This prints if this assert fails 3 (also good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    assert candidate([0,724,32,71,99,32,6,0,5,91,83,0,5,6]) == 11, "This prints if this assert fails 4 (also good for debugging!)"
    
    # Check some edge cases that are easy to work out by hand.
    assert candidate([0,81,12,3,1,21]) == 3, "This prints if this assert fails 5 (also good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    assert candidate([0,8,1,2,1,7]) == 7, "This prints if this assert fails 6 (also good for debugging!)"

    assert candidate([8191]) == 19, "This prints if this assert fails 7 (also good for debugging!)"
    assert candidate([8191, 123456, 127, 7]) == 19, "This prints if this assert fails 8 (also good for debugging!)"
    assert candidate([127, 97, 8192]) == 10, "This prints if this assert fails 9 (also good for debugging!)"
 </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 55
     51     assert candidate([8191, 123456, 127, 7]) == 19, "This prints if this assert fails 8 (also good for debugging!)"
     52     assert candidate([127, 97, 8192]) == 10, "This prints if this assert fails 9 (also good for debugging!)"
---> 55 check(skjkasdkd)
Cell In[1], line 33, in check(candidate)
     30 def check(candidate):
     31 
     32     # Check some simple cases
---> 33     assert candidate([0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3]) == 10, "This prints if this assert fails 1 (good for debugging!)"
     35     # Check some edge cases that are easy to work out by hand.
     36     assert candidate([1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1]) == 25, "This prints if this assert fails 2 (also good for debugging!)"
AssertionError: This prints if this assert fails 1 (good for debugging!) </pre>
### HumanEval/14
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.
from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
 </pre>
###### answer
<pre> ```
def all_prefixes(string: str) -> List[str]:
    result = []
    for i in range(len(string)):
        for prefix in result:
            if prefix + string[i] not in result:
                result.append(prefix + string[i])
    return result
``` </pre>
###### pred
<pre> 
def all_prefixes(string: str) -> List[str]:
    result = []
    for i in range(len(string)):
        for prefix in result:
            if prefix + string[i] not in result:
                result.append(prefix + string[i])
    return result
 </pre>
###### canonical_solution
<pre>     result = []

    for i in range(len(string)):
        result.append(string[:i+1])
    return result
 </pre>
###### test
<pre> 

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('') == []
    assert candidate('asdfgh') == ['a', 'as', 'asd', 'asdf', 'asdfg', 'asdfgh']
    assert candidate('WWW') == ['W', 'WW', 'WWW']
 </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 36
     32     assert candidate('asdfgh') == ['a', 'as', 'asd', 'asdf', 'asdfg', 'asdfgh']
     33     assert candidate('WWW') == ['W', 'WW', 'WWW']
---> 36 check(all_prefixes)
Cell In[1], line 32, in check(candidate)
     30 def check(candidate):
     31     assert candidate('') == []
---> 32     assert candidate('asdfgh') == ['a', 'as', 'asd', 'asdf', 'asdfg', 'asdfgh']
     33     assert candidate('WWW') == ['W', 'WW', 'WWW']
AssertionError:  </pre>
### HumanEval/67
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.

def fruit_distribution(s,n):
    """
    In this task, you will be given a string that represents a number of apples and oranges 
    that are distributed in a basket of fruit this basket contains 
    apples, oranges, and mango fruits. Given the string that represents the total number of 
    the oranges and apples and an integer that represent the total number of the fruits 
    in the basket return the number of the mango fruits in the basket.
    for examble:
    fruit_distribution("5 apples and 6 oranges", 19) ->19 - 5 - 6 = 8
    fruit_distribution("0 apples and 1 oranges",3) -> 3 - 0 - 1 = 2
    fruit_distribution("2 apples and 3 oranges", 100) -> 100 - 2 - 3 = 95
    fruit_distribution("100 apples and 1 oranges",120) -> 120 - 100 - 1 = 19
    """
 </pre>
###### answer
<pre> ```
def fruit_distribution(s, n):
    apples, oranges = s.split(" and ")
    total_fruits = int(apples) + int(oranges)
    mango_fruits = n - total_fruits
    return mango_fruits
``` </pre>
###### pred
<pre> 
def fruit_distribution(s, n):
    apples, oranges = s.split(" and ")
    total_fruits = int(apples) + int(oranges)
    mango_fruits = n - total_fruits
    return mango_fruits
 </pre>
###### canonical_solution
<pre>     lis = list()
    for i in s.split(' '):
        if i.isdigit():
            lis.append(int(i))
    return n - sum(lis)
 </pre>
###### test
<pre> def check(candidate):

    # Check some simple cases
    assert candidate("5 apples and 6 oranges",19) == 8
    assert candidate("5 apples and 6 oranges",21) == 10
    assert candidate("0 apples and 1 oranges",3) == 2
    assert candidate("1 apples and 0 oranges",3) == 2
    assert candidate("2 apples and 3 oranges",100) == 95
    assert candidate("2 apples and 3 oranges",5) == 0
    assert candidate("1 apples and 100 oranges",120) == 19
 </pre>
###### traceback
<pre> ---------------------------------------------------------------------------ValueError                                Traceback (most recent call last)Cell In[1], line 38
     34     assert candidate("2 apples and 3 oranges",5) == 0
     35     assert candidate("1 apples and 100 oranges",120) == 19
---> 38 check(fruit_distribution)
Cell In[1], line 29, in check(candidate)
     26 def check(candidate):
     27 
     28     # Check some simple cases
---> 29     assert candidate("5 apples and 6 oranges",19) == 8
     30     assert candidate("5 apples and 6 oranges",21) == 10
     31     assert candidate("0 apples and 1 oranges",3) == 2
Cell In[1], line 21, in fruit_distribution(s, n)
     19 def fruit_distribution(s, n):
     20     apples, oranges = s.split(" and ")
---> 21     total_fruits = int(apples) + int(oranges)
     22     mango_fruits = n - total_fruits
     23     return mango_fruits
ValueError: invalid literal for int() with base 10: '5 apples' </pre>
### HumanEval/146
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.

def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
 </pre>
###### answer
<pre> ```
def specialFilter(nums):
    count = 0
    for num in nums:
        if num > 10 and (num // 10) % 2 == 1 and (num % 10) % 2 == 1:
            count += 1
    return count
``` </pre>
###### pred
<pre> 
def specialFilter(nums):
    count = 0
    for num in nums:
        if num > 10 and (num // 10) % 2 == 1 and (num % 10) % 2 == 1:
            count += 1
    return count
 </pre>
###### canonical_solution
<pre>     
    count = 0
    for num in nums:
        if num > 10:
            odd_digits = (1, 3, 5, 7, 9)
            number_as_string = str(num)
            if int(number_as_string[0]) in odd_digits and int(number_as_string[-1]) in odd_digits:
                count += 1
        
    return count 
 </pre>
###### test
<pre> def check(candidate):

    # Check some simple cases
    assert candidate([5, -2, 1, -5]) == 0  
    assert candidate([15, -73, 14, -15]) == 1
    assert candidate([33, -2, -3, 45, 21, 109]) == 2
    assert candidate([43, -12, 93, 125, 121, 109]) == 4
    assert candidate([71, -2, -33, 75, 21, 19]) == 3


    # Check some edge cases that are easy to work out by hand.
    assert candidate([1]) == 0              
    assert candidate([]) == 0                   

 </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 38
     33     assert candidate([1]) == 0              
     34     assert candidate([]) == 0                   
---> 38 check(specialFilter)
Cell In[1], line 27, in check(candidate)
     25 assert candidate([5, -2, 1, -5]) == 0  
     26 assert candidate([15, -73, 14, -15]) == 1
---> 27 assert candidate([33, -2, -3, 45, 21, 109]) == 2
     28 assert candidate([43, -12, 93, 125, 121, 109]) == 4
     29 assert candidate([71, -2, -33, 75, 21, 19]) == 3
AssertionError:  </pre>
