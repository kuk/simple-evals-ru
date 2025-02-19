# humaneval / yandexgpt-4-lite
### HumanEval/145
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.

def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
 </pre>
###### answer
<pre> ```
def order_by_points(nums):
    return sorted(nums, key=lambda x: sum(int(digit) for digit in str(x)), reverse=False)
``` </pre>
###### canonical_solution
<pre>     def digits_sum(n):
        neg = 1
        if n &lt; 0: n, neg = -1 * n, -1 
        n = [int(i) for i in str(n)]
        n[0] = n[0] * neg
        return sum(n)
    return sorted(nums, key=digits_sum)
 </pre>
###### test
<pre> def check(candidate):

    # Check some simple cases
    assert candidate([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    assert candidate([1234,423,463,145,2,423,423,53,6,37,3457,3,56,0,46]) == [0, 2, 3, 6, 53, 423, 423, 423, 1234, 145, 37, 46, 56, 463, 3457]
    assert candidate([]) == []
    assert candidate([1, -11, -32, 43, 54, -98, 2, -3]) == [-3, -32, -98, -11, 1, 2, 43, 54]
    assert candidate([1,2,3,4,5,6,7,8,9,10,11]) == [1, 10, 2, 11, 3, 4, 5, 6, 7, 8, 9]
    assert candidate([0,6,6,-76,-21,23,4]) == [-76, -21, 0, 4, 23, 6, 6]

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"

 </pre>
###### traceback
<pre> ---------------------------------------------------------------------------ValueError                                Traceback (most recent call last)Cell In[1], line 36
     31     # Check some edge cases that are easy to work out by hand.
     32     assert True, "This prints if this assert fails 2 (also good for debugging!)"
---> 36 check(order_by_points)
Cell In[1], line 24, in check(candidate)
     21 def check(candidate):
     22 
     23     # Check some simple cases
---> 24     assert candidate([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
     25     assert candidate([1234,423,463,145,2,423,423,53,6,37,3457,3,56,0,46]) == [0, 2, 3, 6, 53, 423, 423, 423, 1234, 145, 37, 46, 56, 463, 3457]
     26     assert candidate([]) == []
Cell In[1], line 18, in order_by_points(nums)
     17 def order_by_points(nums):
---> 18     return sorted(nums, key=lambda x: sum(int(digit) for digit in str(x)), reverse=False)
Cell In[1], line 18, in order_by_points.&lt;locals>.&lt;lambda>(x)
     17 def order_by_points(nums):
---> 18     return sorted(nums, key=lambda x: sum(int(digit) for digit in str(x)), reverse=False)
Cell In[1], line 18, in &lt;genexpr>(.0)
     17 def order_by_points(nums):
---> 18     return sorted(nums, key=lambda x: sum(int(digit) for digit in str(x)), reverse=False)
ValueError: invalid literal for int() with base 10: '-' </pre>
### HumanEval/137
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.

def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,

    compare_one(1, 2.5) ➞ 2.5
    compare_one(1, "2,3") ➞ "2,3"
    compare_one("5,1", "6") ➞ "6"
    compare_one("1", 1) ➞ None
    """
 </pre>
###### answer
<pre> ```
def compare_one(a, b):
    if isinstance(a, str) and isinstance(b, str):
        return max(a, b)
    elif isinstance(a, float) or isinstance(a, int):
        if a > b:
            return a
        elif a &lt; b:
            return b
    else:
        return None
``` </pre>
###### canonical_solution
<pre>     temp_a, temp_b = a, b
    if isinstance(temp_a, str): temp_a = temp_a.replace(',','.')
    if isinstance(temp_b, str): temp_b = temp_b.replace(',','.')
    if float(temp_a) == float(temp_b): return None
    return a if float(temp_a) > float(temp_b) else b 
 </pre>
###### test
<pre> def check(candidate):

    # Check some simple cases
    assert candidate(1, 2) == 2
    assert candidate(1, 2.5) == 2.5
    assert candidate(2, 3) == 3
    assert candidate(5, 6) == 6
    assert candidate(1, "2,3") == "2,3"
    assert candidate("5,1", "6") == "6"
    assert candidate("1", "2") == "2"
    assert candidate("1", 1) == None

    # Check some edge cases that are easy to work out by hand.
    assert True

 </pre>
###### traceback
<pre> ---------------------------------------------------------------------------TypeError                                 Traceback (most recent call last)Cell In[1], line 47
     42     # Check some edge cases that are easy to work out by hand.
     43     assert True
---> 47 check(compare_one)
Cell In[1], line 37, in check(candidate)
     35 assert candidate(2, 3) == 3
     36 assert candidate(5, 6) == 6
---> 37 assert candidate(1, "2,3") == "2,3"
     38 assert candidate("5,1", "6") == "6"
     39 assert candidate("1", "2") == "2"
Cell In[1], line 22, in compare_one(a, b)
     20     return max(a, b)
     21 elif isinstance(a, float) or isinstance(a, int):
---> 22     if a > b:
     23         return a
     24     elif a &lt; b:
TypeError: '>' not supported between instances of 'int' and 'str' </pre>
### HumanEval/3
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.
from typing import List


def below_zero(operations: List[int]) -> bool:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fallls below zero, and
    at that point function should return True. Otherwise it should return False.
    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([1, 2, -4, 5])
    True
    """
 </pre>
###### answer
<pre> ```
def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        if operation > 0:
            balance += operation
        else:
            if balance &lt; 0:
                return True
            balance -= operation
    return False
``` </pre>
###### canonical_solution
<pre>     balance = 0

    for op in operations:
        balance += op
        if balance &lt; 0:
            return True

    return False
 </pre>
###### test
<pre> 

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate([]) == False
    assert candidate([1, 2, -3, 1, 2, -3]) == False
    assert candidate([1, 2, -4, 5, 6]) == True
    assert candidate([1, -1, 2, -2, 5, -5, 4, -4]) == False
    assert candidate([1, -1, 2, -2, 5, -5, 4, -5]) == True
    assert candidate([1, -2, 2, -2, 5, -5, 4, -4]) == True
 </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 46
     42     assert candidate([1, -1, 2, -2, 5, -5, 4, -5]) == True
     43     assert candidate([1, -2, 2, -2, 5, -5, 4, -4]) == True
---> 46 check(below_zero)
Cell In[1], line 40, in check(candidate)
     38 assert candidate([]) == False
     39 assert candidate([1, 2, -3, 1, 2, -3]) == False
---> 40 assert candidate([1, 2, -4, 5, 6]) == True
     41 assert candidate([1, -1, 2, -2, 5, -5, 4, -4]) == False
     42 assert candidate([1, -1, 2, -2, 5, -5, 4, -5]) == True
AssertionError:  </pre>
### HumanEval/107
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.

def even_odd_palindrome(n):
    """
    Given a positive integer n, return a tuple that has the number of even and odd
    integer palindromes that fall within the range(1, n), inclusive.

    Example 1:

        Input: 3
        Output: (1, 2)
        Explanation:
        Integer palindrome are 1, 2, 3. one of them is even, and two of them are odd.

    Example 2:

        Input: 12
        Output: (4, 6)
        Explanation:
        Integer palindrome are 1, 2, 3, 4, 5, 6, 7, 8, 9, 11. four of them are even, and 6 of them are odd.

    Note:
        1. 1 &lt;= n &lt;= 10^3
        2. returned tuple has the number of even and odd integer palindromes respectively.
    """
 </pre>
###### answer
<pre> ```
def even_odd_palindrome(n):
    even_count = 0
    odd_count = 0

    for i in range(1, n + 1):
        if i == str(i)[::-1]:
            if int(i) % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

    return (even_count, odd_count)
``` </pre>
###### canonical_solution
<pre>     def is_palindrome(n):
        return str(n) == str(n)[::-1]

    even_palindrome_count = 0
    odd_palindrome_count = 0

    for i in range(1, n+1):
        if i%2 == 1 and is_palindrome(i):
                odd_palindrome_count += 1
        elif i%2 == 0 and is_palindrome(i):
            even_palindrome_count += 1
    return (even_palindrome_count, odd_palindrome_count)
 </pre>
###### test
<pre> def check(candidate):

    # Check some simple cases
    assert candidate(123) == (8, 13)
    assert candidate(12) == (4, 6)
    assert candidate(3) == (1, 2)
    assert candidate(63) == (6, 8)
    assert candidate(25) == (5, 6)
    assert candidate(19) == (4, 6)
    assert candidate(9) == (4, 5), "This prints if this assert fails 1 (good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    assert candidate(1) == (0, 1), "This prints if this assert fails 2 (also good for debugging!)"

 </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 59
     54     # Check some edge cases that are easy to work out by hand.
     55     assert candidate(1) == (0, 1), "This prints if this assert fails 2 (also good for debugging!)"
---> 59 check(even_odd_palindrome)
Cell In[1], line 46, in check(candidate)
     43 def check(candidate):
     44 
     45     # Check some simple cases
---> 46     assert candidate(123) == (8, 13)
     47     assert candidate(12) == (4, 6)
     48     assert candidate(3) == (1, 2)
AssertionError:  </pre>
### HumanEval/153
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.

def Strongest_Extension(class_name, extensions):
    """You will be given the name of a class (a string) and a list of extensions.
    The extensions are to be used to load additional classes to the class. The
    strength of the extension is as follows: Let CAP be the number of the uppercase
    letters in the extension's name, and let SM be the number of lowercase letters 
    in the extension's name, the strength is given by the fraction CAP - SM. 
    You should find the strongest extension and return a string in this 
    format: ClassName.StrongestExtensionName.
    If there are two or more extensions with the same strength, you should
    choose the one that comes first in the list.
    For example, if you are given "Slices" as the class and a list of the
    extensions: ['SErviNGSliCes', 'Cheese', 'StuFfed'] then you should
    return 'Slices.SErviNGSliCes' since 'SErviNGSliCes' is the strongest extension 
    (its strength is -1).
    Example:
    for Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'
    """
 </pre>
###### answer
<pre> ```
def Strongest_Extension(class_name, extensions):
    strongest_extension = None
    for extension in extensions:
        cap = len(list(filter(lambda x: x.isupper(), extension)))
        sm = len(list(filter(lambda x: x.islower(), extension)))
        strength = cap - sm
        if strongest_extension is None or strength > 0:
            strongest_extension = extension
    return f"{class_name}.{strongest_extension}"
``` </pre>
###### canonical_solution
<pre>     strong = extensions[0]
    my_val = len([x for x in extensions[0] if x.isalpha() and x.isupper()]) - len([x for x in extensions[0] if x.isalpha() and x.islower()])
    for s in extensions:
        val = len([x for x in s if x.isalpha() and x.isupper()]) - len([x for x in s if x.isalpha() and x.islower()])
        if val > my_val:
            strong = s
            my_val = val

    ans = class_name + "." + strong
    return ans

 </pre>
###### test
<pre> def check(candidate):

    # Check some simple cases
    assert candidate('Watashi', ['tEN', 'niNE', 'eIGHt8OKe']) == 'Watashi.eIGHt8OKe'
    assert candidate('Boku123', ['nani', 'NazeDa', 'YEs.WeCaNe', '32145tggg']) == 'Boku123.YEs.WeCaNe'
    assert candidate('__YESIMHERE', ['t', 'eMptY', 'nothing', 'zeR00', 'NuLl__', '123NoooneB321']) == '__YESIMHERE.NuLl__'
    assert candidate('K', ['Ta', 'TAR', 't234An', 'cosSo']) == 'K.TAR'
    assert candidate('__HAHA', ['Tab', '123', '781345', '-_-']) == '__HAHA.123'
    assert candidate('YameRore', ['HhAas', 'okIWILL123', 'WorkOut', 'Fails', '-_-']) == 'YameRore.okIWILL123'
    assert candidate('finNNalLLly', ['Die', 'NowW', 'Wow', 'WoW']) == 'finNNalLLly.WoW'

    # Check some edge cases that are easy to work out by hand.
    assert candidate('_', ['Bb', '91245']) == '_.Bb'
    assert candidate('Sp', ['671235', 'Bb']) == 'Sp.671235'
    
 </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 51
     46     assert candidate('_', ['Bb', '91245']) == '_.Bb'
     47     assert candidate('Sp', ['671235', 'Bb']) == 'Sp.671235'
---> 51 check(Strongest_Extension)
Cell In[1], line 39, in check(candidate)
     37 assert candidate('Watashi', ['tEN', 'niNE', 'eIGHt8OKe']) == 'Watashi.eIGHt8OKe'
     38 assert candidate('Boku123', ['nani', 'NazeDa', 'YEs.WeCaNe', '32145tggg']) == 'Boku123.YEs.WeCaNe'
---> 39 assert candidate('__YESIMHERE', ['t', 'eMptY', 'nothing', 'zeR00', 'NuLl__', '123NoooneB321']) == '__YESIMHERE.NuLl__'
     40 assert candidate('K', ['Ta', 'TAR', 't234An', 'cosSo']) == 'K.TAR'
     41 assert candidate('__HAHA', ['Tab', '123', '781345', '-_-']) == '__HAHA.123'
AssertionError:  </pre>
### HumanEval/160
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.

def do_algebra(operator, operand):
    """
    Given two lists operator, and operand. The first list has basic algebra operations, and 
    the second list is a list of integers. Use the two given lists to build the algebric 
    expression and return the evaluation of this expression.

    The basic algebra operations:
    Addition ( + ) 
    Subtraction ( - ) 
    Multiplication ( * ) 
    Floor division ( // ) 
    Exponentiation ( ** ) 

    Example:
    operator['+', '*', '-']
    array = [2, 3, 4, 5]
    result = 2 + 3 * 4 - 5
    => result = 9

    Note:
        The length of operator list is equal to the length of operand list minus one.
        Operand is a list of of non-negative integers.
        Operator list has at least one operator, and operand list has at least two operands.

    """
 </pre>
###### answer
<pre> ```
def do_algebra(operator, operand):
    expression = ""
    for op in operator:
        if op == '+':
            expression += f"({operand[0]} + {operand[1]})"
        elif op == '-':
            expression += f"({operand[0]} - {operand[1]})"
        elif op == '*':
            expression += f"({operand[0]} * {operand[1]})"
        elif op == '//':
            expression += f"({operand[0]} // {operand[1]})"
        elif op == '**':
            expression += f"({operand[0]} ** {operand[1]})"

    result = eval(expression)
    return result
``` </pre>
###### canonical_solution
<pre>     expression = str(operand[0])
    for oprt, oprn in zip(operator, operand[1:]):
        expression+= oprt + str(oprn)
    return eval(expression)
 </pre>
###### test
<pre> def check(candidate):

    # Check some simple cases
    assert candidate(['**', '*', '+'], [2, 3, 4, 5]) == 37
    assert candidate(['+', '*', '-'], [2, 3, 4, 5]) == 9
    assert candidate(['//', '*'], [7, 3, 4]) == 8, "This prints if this assert fails 1 (good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"

 </pre>
###### traceback
<pre> ---------------------------------------------------------------------------TypeError                                 Traceback (most recent call last)Cell In[1], line 61
     56     # Check some edge cases that are easy to work out by hand.
     57     assert True, "This prints if this assert fails 2 (also good for debugging!)"
---> 61 check(do_algebra)
Cell In[1], line 52, in check(candidate)
     49 def check(candidate):
     50 
     51     # Check some simple cases
---> 52     assert candidate(['**', '*', '+'], [2, 3, 4, 5]) == 37
     53     assert candidate(['+', '*', '-'], [2, 3, 4, 5]) == 9
     54     assert candidate(['//', '*'], [7, 3, 4]) == 8, "This prints if this assert fails 1 (good for debugging!)"
Cell In[1], line 45, in do_algebra(operator, operand)
     42     elif op == '**':
     43         expression += f"({operand[0]} ** {operand[1]})"
---> 45 result = eval(expression)
     46 return result
File &lt;string>:1
TypeError: 'int' object is not callable </pre>
### HumanEval/69
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.

def search(lst):
    '''
    You are given a non-empty list of positive integers. Return the greatest integer that is greater than 
    zero, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, return -1.
    Examples:
        search([4, 1, 2, 2, 3, 1]) == 2
        search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
        search([5, 5, 4, 4, 4]) == -1
    '''
 </pre>
###### answer
<pre> ```
def search(lst):
    max_freq = -1
    max_value = -1

    for num in lst:
        count = lst.count(num)
        if count > max_freq and num > 0:
            max_freq = count
            max_value = num

    if max_freq == -1:
        return -1
    else:
        return max_value
``` </pre>
###### canonical_solution
<pre>     frq = [0] * (max(lst) + 1)
    for i in lst:
        frq[i] += 1;

    ans = -1
    for i in range(1, len(frq)):
        if frq[i] >= i:
            ans = i
    
    return ans
 </pre>
###### test
<pre> def check(candidate):

    # manually generated tests
    assert candidate([5, 5, 5, 5, 1]) == 1
    assert candidate([4, 1, 4, 1, 4, 4]) == 4
    assert candidate([3, 3]) == -1
    assert candidate([8, 8, 8, 8, 8, 8, 8, 8]) == 8
    assert candidate([2, 3, 3, 2, 2]) == 2

    # automatically generated tests
    assert candidate([2, 7, 8, 8, 4, 8, 7, 3, 9, 6, 5, 10, 4, 3, 6, 7, 1, 7, 4, 10, 8, 1]) == 1
    assert candidate([3, 2, 8, 2]) == 2
    assert candidate([6, 7, 1, 8, 8, 10, 5, 8, 5, 3, 10]) == 1
    assert candidate([8, 8, 3, 6, 5, 6, 4]) == -1
    assert candidate([6, 9, 6, 7, 1, 4, 7, 1, 8, 8, 9, 8, 10, 10, 8, 4, 10, 4, 10, 1, 2, 9, 5, 7, 9]) == 1
    assert candidate([1, 9, 10, 1, 3]) == 1
    assert candidate([6, 9, 7, 5, 8, 7, 5, 3, 7, 5, 10, 10, 3, 6, 10, 2, 8, 6, 5, 4, 9, 5, 3, 10]) == 5
    assert candidate([1]) == 1
    assert candidate([8, 8, 10, 6, 4, 3, 5, 8, 2, 4, 2, 8, 4, 6, 10, 4, 2, 1, 10, 2, 1, 1, 5]) == 4
    assert candidate([2, 10, 4, 8, 2, 10, 5, 1, 2, 9, 5, 5, 6, 3, 8, 6, 4, 10]) == 2
    assert candidate([1, 6, 10, 1, 6, 9, 10, 8, 6, 8, 7, 3]) == 1
    assert candidate([9, 2, 4, 1, 5, 1, 5, 2, 5, 7, 7, 7, 3, 10, 1, 5, 4, 2, 8, 4, 1, 9, 10, 7, 10, 2, 8, 10, 9, 4]) == 4
    assert candidate([2, 6, 4, 2, 8, 7, 5, 6, 4, 10, 4, 6, 3, 7, 8, 8, 3, 1, 4, 2, 2, 10, 7]) == 4
    assert candidate([9, 8, 6, 10, 2, 6, 10, 2, 7, 8, 10, 3, 8, 2, 6, 2, 3, 1]) == 2
    assert candidate([5, 5, 3, 9, 5, 6, 3, 2, 8, 5, 6, 10, 10, 6, 8, 4, 10, 7, 7, 10, 8]) == -1
    assert candidate([10]) == -1
    assert candidate([9, 7, 7, 2, 4, 7, 2, 10, 9, 7, 5, 7, 2]) == 2
    assert candidate([5, 4, 10, 2, 1, 1, 10, 3, 6, 1, 8]) == 1
    assert candidate([7, 9, 9, 9, 3, 4, 1, 5, 9, 1, 2, 1, 1, 10, 7, 5, 6, 7, 6, 7, 7, 6]) == 1
    assert candidate([3, 10, 10, 9, 2]) == -1

 </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 66
     61     assert candidate([7, 9, 9, 9, 3, 4, 1, 5, 9, 1, 2, 1, 1, 10, 7, 5, 6, 7, 6, 7, 7, 6]) == 1
     62     assert candidate([3, 10, 10, 9, 2]) == -1
---> 66 check(search)
Cell In[1], line 36, in check(candidate)
     33 def check(candidate):
     34 
     35     # manually generated tests
---> 36     assert candidate([5, 5, 5, 5, 1]) == 1
     37     assert candidate([4, 1, 4, 1, 4, 4]) == 4
     38     assert candidate([3, 3]) == -1
AssertionError:  </pre>
### HumanEval/127
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.

def intersection(interval1, interval2):
    """You are given two intervals,
    where each interval is a pair of integers. For example, interval = (start, end) = (1, 2).
    The given intervals are closed which means that the interval (start, end)
    includes both start and end.
    For each given interval, it is assumed that its start is less or equal its end.
    Your task is to determine whether the length of intersection of these two 
    intervals is a prime number.
    Example, the intersection of the intervals (1, 3), (2, 4) is (2, 3)
    which its length is 1, which not a prime number.
    If the length of the intersection is a prime number, return "YES",
    otherwise, return "NO".
    If the two intervals don't intersect, return "NO".


    [input/output] samples:
    intersection((1, 2), (2, 3)) ==> "NO"
    intersection((-1, 1), (0, 4)) ==> "NO"
    intersection((-3, -1), (-5, 5)) ==> "YES"
    """
 </pre>
###### answer
<pre> ```
def intersection(interval1, interval2):
    # Находим пересечение двух интервалов
    start_min = min(interval1[0], interval2[0])
    end_max = max(interval1[1], interval2[1])

    # Если пересечения нет, возвращаем "NO"
    if start_min > end_max:
        return "NO"

    # Находим длину пересечения
    length = end_max - start_min

    # Проверяем, является ли длина пересечения простым числом
    is_prime = isprime(length)

    # Возвращаем результат
    return "YES" if is_prime else "NO"
``` </pre>
###### canonical_solution
<pre>     def is_prime(num):
        if num == 1 or num == 0:
            return False
        if num == 2:
            return True
        for i in range(2, num):
            if num%i == 0:
                return False
        return True

    l = max(interval1[0], interval2[0])
    r = min(interval1[1], interval2[1])
    length = r - l
    if length > 0 and is_prime(length):
        return "YES"
    return "NO"
 </pre>
###### test
<pre> def check(candidate):

    # Check some simple cases
    assert candidate((1, 2), (2, 3)) == "NO"
    assert candidate((-1, 1), (0, 4)) == "NO"
    assert candidate((-3, -1), (-5, 5)) == "YES"
    assert candidate((-2, 2), (-4, 0)) == "YES"

    # Check some edge cases that are easy to work out by hand.
    assert candidate((-11, 2), (-1, -1)) == "NO"
    assert candidate((1, 2), (3, 5)) == "NO"
    assert candidate((1, 2), (1, 2)) == "NO"
    assert candidate((-2, -2), (-3, -2)) == "NO"

 </pre>
###### traceback
<pre> ---------------------------------------------------------------------------NameError                                 Traceback (most recent call last)Cell In[1], line 61
     56     assert candidate((1, 2), (1, 2)) == "NO"
     57     assert candidate((-2, -2), (-3, -2)) == "NO"
---> 61 check(intersection)
Cell In[1], line 48, in check(candidate)
     45 def check(candidate):
     46 
     47     # Check some simple cases
---> 48     assert candidate((1, 2), (2, 3)) == "NO"
     49     assert candidate((-1, 1), (0, 4)) == "NO"
     50     assert candidate((-3, -1), (-5, 5)) == "YES"
Cell In[1], line 39, in intersection(interval1, interval2)
     36 length = end_max - start_min
     38 # Проверяем, является ли длина пересечения простым числом
---> 39 is_prime = isprime(length)
     41 # Возвращаем результат
     42 return "YES" if is_prime else "NO"
NameError: name 'isprime' is not defined </pre>
### HumanEval/80
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.

def is_happy(s):
    """You are given a string s.
    Your task is to check if the string is happy or not.
    A string is happy if its length is at least 3 and every 3 consecutive letters are distinct
    For example:
    is_happy(a) => False
    is_happy(aa) => False
    is_happy(abcd) => True
    is_happy(aabb) => False
    is_happy(adb) => True
    is_happy(xyy) => False
    """
 </pre>
###### answer
<pre> ```
def is_happy(s):
    # Проверяем длину строки
    if len(s) &lt; 3:
        return False

    # Инициализируем переменные для проверки последовательных букв
    current_letter = s[0]
    previous_letter = None

    for letter in s[1:]:
        # Проверяем, отличается ли текущая буква от предыдущей
        if letter == previous_letter:
            return False
        previous_letter = current_letter
        current_letter = letter

    return True
``` </pre>
###### canonical_solution
<pre>     if len(s) &lt; 3:
      return False

    for i in range(len(s) - 2):
      
      if s[i] == s[i+1] or s[i+1] == s[i+2] or s[i] == s[i+2]:
        return False
    return True
 </pre>
###### test
<pre> def check(candidate):

    # Check some simple cases
    assert candidate("a") == False , "a"
    assert candidate("aa") == False , "aa"
    assert candidate("abcd") == True , "abcd"
    assert candidate("aabb") == False , "aabb"
    assert candidate("adb") == True , "adb"
    assert candidate("xyy") == False , "xyy"
    assert candidate("iopaxpoi") == True , "iopaxpoi"
    assert candidate("iopaxioi") == False , "iopaxioi"
 </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 50
     46     assert candidate("iopaxpoi") == True , "iopaxpoi"
     47     assert candidate("iopaxioi") == False , "iopaxioi"
---> 50 check(is_happy)
Cell In[1], line 43, in check(candidate)
     41 assert candidate("aa") == False , "aa"
     42 assert candidate("abcd") == True , "abcd"
---> 43 assert candidate("aabb") == False , "aabb"
     44 assert candidate("adb") == True , "adb"
     45 assert candidate("xyy") == False , "xyy"
AssertionError: aabb </pre>
### HumanEval/90
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.

def next_smallest(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    """
 </pre>
###### answer
<pre> ```
def next_smallest(lst):
    if not lst:
        return None
    lst.sort()
    if len(lst) == 1:
        return None
    return lst[1]
``` </pre>
###### canonical_solution
<pre>     lst = sorted(set(lst))
    return None if len(lst) &lt; 2 else lst[1]
 </pre>
###### test
<pre> def check(candidate):

    # Check some simple cases
    assert candidate([1, 2, 3, 4, 5]) == 2
    assert candidate([5, 1, 4, 3, 2]) == 2
    assert candidate([]) == None
    assert candidate([1, 1]) == None
    assert candidate([1,1,1,1,0]) == 1
    assert candidate([1, 0**0]) == None
    assert candidate([-35, 34, 12, -45]) == -35

    # Check some edge cases that are easy to work out by hand.
    assert True

 </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 42
     37     # Check some edge cases that are easy to work out by hand.
     38     assert True
---> 42 check(next_smallest)
Cell In[1], line 32, in check(candidate)
     30 assert candidate([5, 1, 4, 3, 2]) == 2
     31 assert candidate([]) == None
---> 32 assert candidate([1, 1]) == None
     33 assert candidate([1,1,1,1,0]) == 1
     34 assert candidate([1, 0**0]) == None
AssertionError:  </pre>
