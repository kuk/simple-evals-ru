# humaneval / yandexgpt-4-lite
### HumanEval/8
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.
from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
 </pre>
###### answer
<pre> ```
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    sum_ = 0
    product = 1
    for num in numbers:
        sum_ += num
        product *= num
    return (sum_, product)
``` </pre>
###### canonical_solution
<pre>     sum_value = 0
    prod_value = 1

    for n in numbers:
        sum_value += n
        prod_value *= n
    return sum_value, prod_value
 </pre>
###### test
<pre> 

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate([]) == (0, 1)
    assert candidate([1, 1, 1]) == (3, 1)
    assert candidate([100, 0]) == (100, 0)
    assert candidate([3, 5, 7]) == (3 + 5 + 7, 3 * 5 * 7)
    assert candidate([10]) == (10, 10)
 </pre>
### HumanEval/121
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.

def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
 </pre>
###### answer
<pre> ```
def solution(lst):
    result = 0
    for i in range(len(lst)):
        if i % 2 == 0 and lst[i] % 2 == 1:
            result += lst[i]
    return result
``` </pre>
###### canonical_solution
<pre>     return sum([x for idx, x in enumerate(lst) if idx%2==0 and x%2==1])
 </pre>
###### test
<pre> def check(candidate):

    # Check some simple cases
    assert candidate([5, 8, 7, 1])    == 12
    assert candidate([3, 3, 3, 3, 3]) == 9
    assert candidate([30, 13, 24, 321]) == 0
    assert candidate([5, 9]) == 5
    assert candidate([2, 4, 8]) == 0
    assert candidate([30, 13, 23, 32]) == 23
    assert candidate([3, 13, 2, 9]) == 3

    # Check some edge cases that are easy to work out by hand.

 </pre>
### HumanEval/23
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.


def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
 </pre>
###### answer
<pre> ```
def strlen(string: str) -> int:
    return len(string)
``` </pre>
###### canonical_solution
<pre>     return len(string)
 </pre>
###### test
<pre> 

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('') == 0
    assert candidate('x') == 1
    assert candidate('asdasnakj') == 9
 </pre>
### HumanEval/54
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.


def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')
    True
    >>> same_chars('abcd', 'dddddddabc')
    True
    >>> same_chars('dddddddabc', 'abcd')
    True
    >>> same_chars('eabcd', 'dddddddabc')
    False
    >>> same_chars('abcd', 'dddddddabce')
    False
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddddabc')
    False
    """
 </pre>
###### answer
<pre> ```
def same_chars(s0: str, s1: str):
    return set(s0) == set(s1)
``` </pre>
###### canonical_solution
<pre>     return set(s0) == set(s1)
 </pre>
###### test
<pre> 

METADATA = {}


def check(candidate):
    assert candidate('eabcdzzzz', 'dddzzzzzzzddeddabc') == True
    assert candidate('abcd', 'dddddddabc') == True
    assert candidate('dddddddabc', 'abcd') == True
    assert candidate('eabcd', 'dddddddabc') == False
    assert candidate('abcd', 'dddddddabcf') == False
    assert candidate('eabcdzzzz', 'dddzzzzzzzddddabc') == False
    assert candidate('aabb', 'aaccc') == False

 </pre>
### HumanEval/40
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.


def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.

    >>> triples_sum_to_zero([1, 3, 5, 0])
    False
    >>> triples_sum_to_zero([1, 3, -2, 1])
    True
    >>> triples_sum_to_zero([1, 2, 3, 7])
    False
    >>> triples_sum_to_zero([2, 4, -5, 3, 9, 7])
    True
    >>> triples_sum_to_zero([1])
    False
    """
 </pre>
###### answer
<pre> ```
def triples_sum_to_zero(l: list) -> bool:
    for i in range(len(l) - 2):
        for j in range(i + 1, len(l) - 1):
            for k in range(j + 1, len(l)):
                if l[i] + l[j] + l[k] == 0:
                    return True
    return False
``` </pre>
###### canonical_solution
<pre>     for i in range(len(l)):
        for j in range(i + 1, len(l)):
            for k in range(j + 1, len(l)):
                if l[i] + l[j] + l[k] == 0:
                    return True
    return False
 </pre>
###### test
<pre> 

METADATA = {}


def check(candidate):
    assert candidate([1, 3, 5, 0]) == False
    assert candidate([1, 3, 5, -1]) == False
    assert candidate([1, 3, -2, 1]) == True
    assert candidate([1, 2, 3, 7]) == False
    assert candidate([1, 2, 5, 7]) == False
    assert candidate([2, 4, -5, 3, 9, 7]) == True
    assert candidate([1]) == False
    assert candidate([1, 3, 5, -100]) == False
    assert candidate([100, 3, 5, -100]) == False

 </pre>
### HumanEval/56
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.


def correct_bracketing(brackets: str):
    """ brackets is a string of "&lt;" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("&lt;")
    False
    >>> correct_bracketing("&lt;>")
    True
    >>> correct_bracketing("&lt;&lt;>&lt;>>")
    True
    >>> correct_bracketing(">&lt;&lt;>")
    False
    """
 </pre>
###### answer
<pre> ```
def correct_bracketing(brackets: str):
    count = 0
    for bracket in brackets:
        if bracket == "&lt;":
            count += 1
        elif bracket == ">":
            count -= 1
        if count &lt; 0:
            return False
    return count == 0
``` </pre>
###### canonical_solution
<pre>     depth = 0
    for b in brackets:
        if b == "&lt;":
            depth += 1
        else:
            depth -= 1
        if depth &lt; 0:
            return False
    return depth == 0
 </pre>
###### test
<pre> 

METADATA = {}


def check(candidate):
    assert candidate("&lt;>")
    assert candidate("&lt;&lt;>&lt;>>")
    assert candidate("&lt;>&lt;>&lt;&lt;>&lt;>>&lt;>")
    assert candidate("&lt;>&lt;>&lt;&lt;&lt;>&lt;>&lt;>>&lt;>>&lt;&lt;>&lt;>&lt;&lt;>>>")
    assert not candidate("&lt;&lt;&lt;>&lt;>>>>")
    assert not candidate(">&lt;&lt;>")
    assert not candidate("&lt;")
    assert not candidate("&lt;&lt;&lt;&lt;")
    assert not candidate(">")
    assert not candidate("&lt;&lt;>")
    assert not candidate("&lt;>&lt;>&lt;&lt;>&lt;>>&lt;>>&lt;&lt;>")
    assert not candidate("&lt;>&lt;>&lt;&lt;>&lt;>>&lt;>>>&lt;>")

 </pre>
### HumanEval/4
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
 </pre>
###### answer
<pre> ```
def mean_absolute_deviation(numbers: List[float]) -> float:
    mean = sum(numbers) / len(numbers)
    absolute_deviations = [abs(number - mean) for number in numbers]
    return sum(absolute_deviations) / len(absolute_deviations)
``` </pre>
###### canonical_solution
<pre>     mean = sum(numbers) / len(numbers)
    return sum(abs(x - mean) for x in numbers) / len(numbers)
 </pre>
###### test
<pre> 

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert abs(candidate([1.0, 2.0, 3.0]) - 2.0/3.0) &lt; 1e-6
    assert abs(candidate([1.0, 2.0, 3.0, 4.0]) - 1.0) &lt; 1e-6
    assert abs(candidate([1.0, 2.0, 3.0, 4.0, 5.0]) - 6.0/5.0) &lt; 1e-6

 </pre>
### HumanEval/61
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.


def correct_bracketing(brackets: str):
    """ brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("(")
    False
    >>> correct_bracketing("()")
    True
    >>> correct_bracketing("(()())")
    True
    >>> correct_bracketing(")(()")
    False
    """
 </pre>
###### answer
<pre> ```
def correct_bracketing(brackets: str):
    count = 0
    for bracket in brackets:
        if bracket == "(":
            count += 1
        elif bracket == ")":
            count -= 1
        if count &lt; 0:
            return False
    return count == 0
``` </pre>
###### canonical_solution
<pre>     depth = 0
    for b in brackets:
        if b == "(":
            depth += 1
        else:
            depth -= 1
        if depth &lt; 0:
            return False
    return depth == 0
 </pre>
###### test
<pre> 

METADATA = {}


def check(candidate):
    assert candidate("()")
    assert candidate("(()())")
    assert candidate("()()(()())()")
    assert candidate("()()((()()())())(()()(()))")
    assert not candidate("((()())))")
    assert not candidate(")(()")
    assert not candidate("(")
    assert not candidate("((((")
    assert not candidate(")")
    assert not candidate("(()")
    assert not candidate("()()(()())())(()")
    assert not candidate("()()(()())()))()")

 </pre>
### HumanEval/7
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
 </pre>
###### answer
<pre> ```
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if substring in string]
``` </pre>
###### canonical_solution
<pre>     return [x for x in strings if substring in x]
 </pre>
###### test
<pre> 

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate([], 'john') == []
    assert candidate(['xxx', 'asd', 'xxy', 'john doe', 'xxxAAA', 'xxx'], 'xxx') == ['xxx', 'xxxAAA', 'xxx']
    assert candidate(['xxx', 'asd', 'aaaxxy', 'john doe', 'xxxAAA', 'xxx'], 'xx') == ['xxx', 'aaaxxy', 'xxxAAA', 'xxx']
    assert candidate(['grunt', 'trumpet', 'prune', 'gruesome'], 'run') == ['grunt', 'prune']
 </pre>
### HumanEval/22
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.
from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
 </pre>
###### answer
<pre> ```
def filter_integers(values: List[Any]) -> List[int]:
    return list(filter(lambda x: isinstance(x, int), values))
``` </pre>
###### canonical_solution
<pre>     return [x for x in values if isinstance(x, int)]
 </pre>
###### test
<pre> 

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate([]) == []
    assert candidate([4, {}, [], 23.2, 9, 'adasd']) == [4, 9]
    assert candidate([3, 'c', 3, 3, 'a', 'b']) == [3, 3, 3]
 </pre>
