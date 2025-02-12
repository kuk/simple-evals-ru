# humaneval / yandexgpt-3-lite
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
    if (a + b > c) and (a + c > b) and (b + c > a):
        p = (a + b + c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))
    else:
        return -1
``` </pre>
###### pred
<pre> 
def triangle_area(a, b, c):
    if (a + b > c) and (a + c > b) and (b + c > a):
        p = (a + b + c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))
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
<pre> ---------------------------------------------------------------------------NameError                                 Traceback (most recent call last)Cell In[1], line 42
     37     assert candidate(1, 1, 1) == 0.43, "This prints if this assert fails 2 (also good for debugging!)"
     38     assert candidate(2, 2, 10) == -1
---> 42 check(triangle_area)
Cell In[1], line 28, in check(candidate)
     25 def check(candidate):
     26 
     27     # Check some simple cases
---> 28     assert candidate(3, 4, 5) == 6.00, "This prints if this assert fails 1 (good for debugging!)"
     29     assert candidate(1, 2, 10) == -1
     30     assert candidate(4, 8, 5) == 8.18
Cell In[1], line 20, in triangle_area(a, b, c)
     18 if (a + b > c) and (a + c > b) and (b + c > a):
     19     p = (a + b + c) / 2
---> 20     return math.sqrt(p * (p - a) * (p - b) * (p - c))
     21 else:
     22     return -1
NameError: name 'math' is not defined </pre>
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
    depth = 0
    for char in paren_string:
        if char == "(":
            depth += 1
        elif char == ")":
            if depth == 1:
                result.append(1)
            else:
                depth -= 1
    return result
``` </pre>
###### pred
<pre> 
def parse_nested_parens(paren_string: str) -> List[int]:
    result = []
    depth = 0
    for char in paren_string:
        if char == "(":
            depth += 1
        elif char == ")":
            if depth == 1:
                result.append(1)
            else:
                depth -= 1
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
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 44
     40     assert candidate('() (()) ((())) (((())))') == [1, 2, 3, 4]
     41     assert candidate('(()(())((())))') == [4]
---> 44 check(parse_nested_parens)
Cell In[1], line 39, in check(candidate)
     38 def check(candidate):
---> 39     assert candidate('(()()) ((())) () ((())()())') == [2, 3, 1, 3]
     40     assert candidate('() (()) ((())) (((())))') == [1, 2, 3, 4]
     41     assert candidate('(()(())((())))') == [4]
AssertionError:  </pre>
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
        if (1 < num < 100) and (num % 10 and num % 10 > 5) and (num // 10 % 10 and num // 10 % 10 in [1, 3, 5, 7, 9]):
            count += 1
    return count
``` </pre>
###### pred
<pre> 
def specialFilter(nums):
    count = 0
    for num in nums:
        if (1 < num < 100) and (num % 10 and num % 10 > 5) and (num // 10 % 10 and num // 10 % 10 in [1, 3, 5, 7, 9]):
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
Cell In[1], line 26, in check(candidate)
     22 def check(candidate):
     23 
     24     # Check some simple cases
     25     assert candidate([5, -2, 1, -5]) == 0  
---> 26     assert candidate([15, -73, 14, -15]) == 1
     27     assert candidate([33, -2, -3, 45, 21, 109]) == 2
     28     assert candidate([43, -12, 93, 125, 121, 109]) == 4
AssertionError:  </pre>
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
    result = [string]
    prefixes = [string[i:] for i in range(len(string))]
    while prefixes:
        new_prefixes = []
        for prefix in prefixes:
            new_prefixes.append(prefix + string[0])
        prefixes = new_prefixes
        result.extend(prefixes)
    return result
``` </pre>
###### pred
<pre> 
def all_prefixes(string: str) -> List[str]:
    result = [string]
    prefixes = [string[i:] for i in range(len(string))]
    while prefixes:
        new_prefixes = []
        for prefix in prefixes:
            new_prefixes.append(prefix + string[0])
        prefixes = new_prefixes
        result.extend(prefixes)
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
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 39
     35     assert candidate('asdfgh') == ['a', 'as', 'asd', 'asdf', 'asdfg', 'asdfgh']
     36     assert candidate('WWW') == ['W', 'WW', 'WWW']
---> 39 check(all_prefixes)
Cell In[1], line 34, in check(candidate)
     33 def check(candidate):
---> 34     assert candidate('') == []
     35     assert candidate('asdfgh') == ['a', 'as', 'asd', 'asdf', 'asdfg', 'asdfgh']
     36     assert candidate('WWW') == ['W', 'WW', 'WWW']
AssertionError:  </pre>
### HumanEval/50
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.


def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    """
 </pre>
###### answer
<pre> ```
def decode_shift(s: str):
    return "".join(chr(ord(ch) - 5 + ord("a")) for ch in s)
``` </pre>
###### pred
<pre> 
def decode_shift(s: str):
    return "".join(chr(ord(ch) - 5 + ord("a")) for ch in s)
 </pre>
###### canonical_solution
<pre>     return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])
 </pre>
###### test
<pre> 

METADATA = {}


def check(candidate):
    from random import randint, choice
    import copy
    import string

    letters = string.ascii_lowercase
    for _ in range(100):
        str = ''.join(choice(letters) for i in range(randint(10, 20)))
        encoded_str = encode_shift(str)
        assert candidate(copy.deepcopy(encoded_str)) == str

 </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 40
     35         encoded_str = encode_shift(str)
     36         assert candidate(copy.deepcopy(encoded_str)) == str
---> 40 check(decode_shift)
Cell In[1], line 36, in check(candidate)
     34 str = ''.join(choice(letters) for i in range(randint(10, 20)))
     35 encoded_str = encode_shift(str)
---> 36 assert candidate(copy.deepcopy(encoded_str)) == str
AssertionError:  </pre>
### HumanEval/68
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.

def pluck(arr):
    """
    "Given an array representing a branch of a tree that has non-negative integer nodes
    your task is to pluck one of the nodes and return it.
    The plucked node should be the node with the smallest even value.
    If multiple nodes with the same smallest even value are found return the node that has smallest index.

    The plucked node should be returned in a list, [ smalest_value, its index ],
    If there are no even values or the given array is empty, return [].

    Example 1:
        Input: [4,2,3]
        Output: [2, 1]
        Explanation: 2 has the smallest even value, and 2 has the smallest index.

    Example 2:
        Input: [1,2,3]
        Output: [2, 1]
        Explanation: 2 has the smallest even value, and 2 has the smallest index. 

    Example 3:
        Input: []
        Output: []
    
    Example 4:
        Input: [5, 0, 3, 0, 4, 2]
        Output: [0, 1]
        Explanation: 0 is the smallest value, but  there are two zeros,
                     so we will choose the first zero, which has the smallest index.

    Constraints:
        * 1 <= nodes.length <= 10000
        * 0 <= node.value
    """
 </pre>
###### answer
<pre> ```
def pluck(arr):
    even_values = [x for x in arr if x % 2 == 0]
    if not even_values:
        return []
    smallest_even = min(even_values)
    index = even_values.index(smallest_even)
    return [smallest_even, index]
``` </pre>
###### pred
<pre> 
def pluck(arr):
    even_values = [x for x in arr if x % 2 == 0]
    if not even_values:
        return []
    smallest_even = min(even_values)
    index = even_values.index(smallest_even)
    return [smallest_even, index]
 </pre>
###### canonical_solution
<pre>     if(len(arr) == 0): return []
    evens = list(filter(lambda x: x%2 == 0, arr))
    if(evens == []): return []
    return [min(evens), arr.index(min(evens))]
 </pre>
###### test
<pre> def check(candidate):

    # Check some simple cases
    assert True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate([4,2,3]) == [2, 1], "Error"
    assert candidate([1,2,3]) == [2, 1], "Error"
    assert candidate([]) == [], "Error"
    assert candidate([5, 0, 3, 0, 4, 2]) == [0, 1], "Error"

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"
    assert candidate([1, 2, 3, 0, 5, 3]) == [0, 3], "Error"
    assert candidate([5, 4, 8, 4 ,8]) == [4, 1], "Error"
    assert candidate([7, 6, 7, 1]) == [6, 1], "Error"
    assert candidate([7, 9, 7, 1]) == [], "Error"

 </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 67
     62     assert candidate([7, 6, 7, 1]) == [6, 1], "Error"
     63     assert candidate([7, 9, 7, 1]) == [], "Error"
---> 67 check(pluck)
Cell In[1], line 54, in check(candidate)
     52 assert True, "This prints if this assert fails 1 (good for debugging!)"
     53 assert candidate([4,2,3]) == [2, 1], "Error"
---> 54 assert candidate([1,2,3]) == [2, 1], "Error"
     55 assert candidate([]) == [], "Error"
     56 assert candidate([5, 0, 3, 0, 4, 2]) == [0, 1], "Error"
AssertionError: Error </pre>
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
    total_fruits = int(n)
    return total_fruits - int(apples) - int(oranges)
``` </pre>
###### pred
<pre> 
def fruit_distribution(s, n):
    apples, oranges = s.split(" and ")
    total_fruits = int(n)
    return total_fruits - int(apples) - int(oranges)
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
<pre> ---------------------------------------------------------------------------ValueError                                Traceback (most recent call last)Cell In[1], line 37
     33     assert candidate("2 apples and 3 oranges",5) == 0
     34     assert candidate("1 apples and 100 oranges",120) == 19
---> 37 check(fruit_distribution)
Cell In[1], line 28, in check(candidate)
     25 def check(candidate):
     26 
     27     # Check some simple cases
---> 28     assert candidate("5 apples and 6 oranges",19) == 8
     29     assert candidate("5 apples and 6 oranges",21) == 10
     30     assert candidate("0 apples and 1 oranges",3) == 2
Cell In[1], line 22, in fruit_distribution(s, n)
     20 apples, oranges = s.split(" and ")
     21 total_fruits = int(n)
---> 22 return total_fruits - int(apples) - int(oranges)
ValueError: invalid literal for int() with base 10: '5 apples' </pre>
