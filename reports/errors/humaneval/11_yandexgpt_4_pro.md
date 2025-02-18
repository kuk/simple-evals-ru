# humaneval / yandexgpt-4-pro
### HumanEval/159
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.

def eat(number, need, remaining):
    """
    You're a hungry rabbit, and you already have eaten a certain number of carrots,
    but now you need to eat more carrots to complete the day's meals.
    you should return an array of [ total number of eaten carrots after your meals,
                                    the number of carrots left after your meals ]
    if there are not enough remaining carrots, you will eat all remaining carrots, but will still be hungry.
    
    Example:
    * eat(5, 6, 10) -> [11, 4]
    * eat(4, 8, 9) -> [12, 1]
    * eat(1, 10, 10) -> [11, 0]
    * eat(2, 11, 5) -> [7, 0]
    
    Variables:
    @number : integer
        the number of carrots that you have eaten.
    @need : integer
        the number of carrots that you need to eat.
    @remaining : integer
        the number of remaining carrots thet exist in stock
    
    Constrain:
    * 0 <= number <= 1000
    * 0 <= need <= 1000
    * 0 <= remaining <= 1000

    Have fun :)
    """
 </pre>
###### answer
<pre> ```
def eat(number, need, remaining):
    total_eaten = number + remaining
    if total_eaten < need:
        total_eaten += need - total_eaten
        remaining = 0
    return [total_eaten, remaining]
``` </pre>
###### canonical_solution
<pre>     if(need <= remaining):
        return [ number + need , remaining-need ]
    else:
        return [ number + remaining , 0]
 </pre>
###### test
<pre> def check(candidate):

    # Check some simple cases
    assert True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate(5, 6, 10) == [11, 4], "Error"
    assert candidate(4, 8, 9) == [12, 1], "Error"
    assert candidate(1, 10, 10) == [11, 0], "Error"
    assert candidate(2, 11, 5) == [7, 0], "Error"

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"
    assert candidate(4, 5, 7) == [9, 2], "Error"
    assert candidate(4, 5, 1) == [5, 0], "Error"

 </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 59
     54     assert candidate(4, 5, 7) == [9, 2], "Error"
     55     assert candidate(4, 5, 1) == [5, 0], "Error"
---> 59 check(eat)
Cell In[1], line 47, in check(candidate)
     43 def check(candidate):
     44 
     45     # Check some simple cases
     46     assert True, "This prints if this assert fails 1 (good for debugging!)"
---> 47     assert candidate(5, 6, 10) == [11, 4], "Error"
     48     assert candidate(4, 8, 9) == [12, 1], "Error"
     49     assert candidate(1, 10, 10) == [11, 0], "Error"
AssertionError: Error </pre>
### HumanEval/70
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.

def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    '''
 </pre>
###### answer
<pre> ```
def strange_sort_list(lst):
    if not lst:
        return []

    min_val = min(lst)
    max_val = max(lst)

    result = [min_val]
    lst.remove(min_val)

    while lst:
        result.append(max_val)
        lst.remove(max_val)
            
        if lst:
            result.append(min_val) 
            lst.remove(min_val)
                
    return result
``` </pre>
###### canonical_solution
<pre>     res, switch = [], True
    while lst:
        res.append(min(lst) if switch else max(lst))
        lst.remove(res[-1])
        switch = not switch
    return res
 </pre>
###### test
<pre> def check(candidate):

    # Check some simple cases
    assert candidate([1, 2, 3, 4]) == [1, 4, 2, 3]
    assert candidate([5, 6, 7, 8, 9]) == [5, 9, 6, 8, 7]
    assert candidate([1, 2, 3, 4, 5]) == [1, 5, 2, 4, 3]
    assert candidate([5, 6, 7, 8, 9, 1]) == [1, 9, 5, 8, 6, 7]
    assert candidate([5, 5, 5, 5]) == [5, 5, 5, 5]
    assert candidate([]) == []
    assert candidate([1,2,3,4,5,6,7,8]) == [1, 8, 2, 7, 3, 6, 4, 5]
    assert candidate([0,2,2,2,5,5,-5,-5]) == [-5, 5, -5, 5, 0, 2, 2, 2]
    assert candidate([111111]) == [111111]

    # Check some edge cases that are easy to work out by hand.
    assert True

 </pre>
###### traceback
<pre> ---------------------------------------------------------------------------ValueError                                Traceback (most recent call last)Cell In[1], line 56
     51     # Check some edge cases that are easy to work out by hand.
     52     assert True
---> 56 check(strange_sort_list)
Cell In[1], line 41, in check(candidate)
     38 def check(candidate):
     39 
     40     # Check some simple cases
---> 41     assert candidate([1, 2, 3, 4]) == [1, 4, 2, 3]
     42     assert candidate([5, 6, 7, 8, 9]) == [5, 9, 6, 8, 7]
     43     assert candidate([1, 2, 3, 4, 5]) == [1, 5, 2, 4, 3]
Cell In[1], line 33, in strange_sort_list(lst)
     31     if lst:
     32         result.append(min_val) 
---> 33         lst.remove(min_val)
     35 return result
ValueError: list.remove(x): x not in list </pre>
### HumanEval/33
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.


def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
 </pre>
###### answer
<pre> ```
def sort_third(l: list):
    new_list = []

    for i in range(len(l)):
        if i % 3 != 0:
            new_list.append(l[i])
        else:
            temp_list = [l[i]]
            for j in range(i + 1, len(l), 3):
                temp_list.append(l[j])
            temp_list.sort()
            new_list += temp_list

    return new_list
``` </pre>
###### canonical_solution
<pre>     l = list(l)
    l[::3] = sorted(l[::3])
    return l
 </pre>
###### test
<pre> 

METADATA = {}


def check(candidate):
    assert tuple(candidate([1, 2, 3])) == tuple(sort_third([1, 2, 3]))
    assert tuple(candidate([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])) == tuple(sort_third([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
    assert tuple(candidate([5, 8, -12, 4, 23, 2, 3, 11, 12, -10])) == tuple(sort_third([5, 8, -12, 4, 23, 2, 3, 11, 12, -10]))
    assert tuple(candidate([5, 6, 3, 4, 8, 9, 2])) == tuple([2, 6, 3, 4, 8, 9, 5])
    assert tuple(candidate([5, 8, 3, 4, 6, 9, 2])) == tuple([2, 8, 3, 4, 6, 9, 5])
    assert tuple(candidate([5, 6, 9, 4, 8, 3, 2])) == tuple([2, 6, 9, 4, 8, 3, 5])
    assert tuple(candidate([5, 6, 3, 4, 8, 9, 2, 1])) == tuple([2, 6, 3, 4, 8, 9, 5, 1])

 </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 48
     43     assert tuple(candidate([5, 6, 9, 4, 8, 3, 2])) == tuple([2, 6, 9, 4, 8, 3, 5])
     44     assert tuple(candidate([5, 6, 3, 4, 8, 9, 2, 1])) == tuple([2, 6, 3, 4, 8, 9, 5, 1])
---> 48 check(sort_third)
Cell In[1], line 41, in check(candidate)
     39 assert tuple(candidate([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])) == tuple(sort_third([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
     40 assert tuple(candidate([5, 8, -12, 4, 23, 2, 3, 11, 12, -10])) == tuple(sort_third([5, 8, -12, 4, 23, 2, 3, 11, 12, -10]))
---> 41 assert tuple(candidate([5, 6, 3, 4, 8, 9, 2])) == tuple([2, 6, 3, 4, 8, 9, 5])
     42 assert tuple(candidate([5, 8, 3, 4, 6, 9, 2])) == tuple([2, 8, 3, 4, 6, 9, 5])
     43 assert tuple(candidate([5, 6, 9, 4, 8, 3, 2])) == tuple([2, 6, 9, 4, 8, 3, 5])
AssertionError:  </pre>
### HumanEval/123
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.

def get_odd_collatz(n):
    """
    Given a positive integer n, return a sorted list that has the odd numbers in collatz sequence.

    The Collatz conjecture is a conjecture in mathematics that concerns a sequence defined
    as follows: start with any positive integer n. Then each term is obtained from the 
    previous term as follows: if the previous term is even, the next term is one half of 
    the previous term. If the previous term is odd, the next term is 3 times the previous
    term plus 1. The conjecture is that no matter what value of n, the sequence will always reach 1.

    Note: 
        1. Collatz(1) is [1].
        2. returned list sorted in increasing order.

    For example:
    get_odd_collatz(5) returns [1, 5] # The collatz sequence for 5 is [5, 16, 8, 4, 2, 1], so the odd numbers are only 1, and 5.
    """
 </pre>
###### answer
<pre> ```
def get_odd_collatz(n):
    if n == 1:
        return [1]

    odd_sequence = []
    while n != 1:
        if n % 2 == 1:  # If n is odd, add it to the sequence.
            odd_sequence.append(n)
        n = (n // 2) if n % 2 == 0 else (3 * n + 1)  # Update n based on Collatz rule.

    return sorted(odd_sequence)  # Return the sorted list of odd numbers in the Collatz sequence. </pre>
###### canonical_solution
<pre>     if n%2==0:
        odd_collatz = [] 
    else:
        odd_collatz = [n]
    while n > 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = n*3 + 1
            
        if n%2 == 1:
            odd_collatz.append(int(n))

    return sorted(odd_collatz)
 </pre>
###### test
<pre> def check(candidate):

    # Check some simple cases
    assert candidate(14) == [1, 5, 7, 11, 13, 17]
    assert candidate(5) == [1, 5]
    assert candidate(12) == [1, 3, 5], "This prints if this assert fails 1 (good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    assert candidate(1) == [1], "This prints if this assert fails 2 (also good for debugging!)"

 </pre>
###### traceback
<pre>   Cell In[1], line 22
    ```
    ^
SyntaxError: invalid syntax
 </pre>
### HumanEval/19
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.
from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
 </pre>
###### answer
<pre> ```
def sort_numbers(numbers: str) -> str:
    # Create a list of numbers from the input string
    number_list = numbers.split()

    # Sort the list in ascending order
    sorted_numbers = sorted(number_list)

    # Join the sorted list into a single string and return it
    return ' '.join(sorted_numbers)
``` </pre>
###### canonical_solution
<pre>     value_map = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    return ' '.join(sorted([x for x in numbers.split(' ') if x], key=lambda x: value_map[x]))
 </pre>
###### test
<pre> 

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('') == ''
    assert candidate('three') == 'three'
    assert candidate('three five nine') == 'three five nine'
    assert candidate('five zero four seven nine eight') == 'zero four five seven eight nine'
    assert candidate('six five four three two one zero') == 'zero one two three four five six'
 </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 42
     38     assert candidate('five zero four seven nine eight') == 'zero four five seven eight nine'
     39     assert candidate('six five four three two one zero') == 'zero one two three four five six'
---> 42 check(sort_numbers)
Cell In[1], line 37, in check(candidate)
     35 assert candidate('') == ''
     36 assert candidate('three') == 'three'
---> 37 assert candidate('three five nine') == 'three five nine'
     38 assert candidate('five zero four seven nine eight') == 'zero four five seven eight nine'
     39 assert candidate('six five four three two one zero') == 'zero one two three four five six'
AssertionError:  </pre>
### HumanEval/134
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.

def check_if_last_char_is_a_letter(txt):
    '''
    Create a function that returns True if the last character
    of a given string is an alphabetical character and is not
    a part of a word, and False otherwise.
    Note: "word" is a group of characters separated by space.

    Examples:
    check_if_last_char_is_a_letter("apple pie") ➞ False
    check_if_last_char_is_a_letter("apple pi e") ➞ True
    check_if_last_char_is_a_letter("apple pi e ") ➞ False
    check_if_last_char_is_a_letter("") ➞ False 
    '''
 </pre>
###### answer
<pre> ```
def check_if_last_char_is_a_letter(txt):
    # Remove trailing whitespace
    txt = txt.strip()

    # Check if the string is empty
    if not txt:
        return False

    # Split the string into words
    words = txt.split()
    
    # Get the last character of the string
    last_char = txt[-1]

    # If the last character is a letter and not part of a word
    if (last_char.isalpha()) and (not any(word.endswith(last_char) for word in words)):
        return True
    else:
        return False </pre>
###### canonical_solution
<pre>  
    check = txt.split(' ')[-1]
    return True if len(check) == 1 and (97 <= ord(check.lower()) <= 122) else False
 </pre>
###### test
<pre> def check(candidate):

    # Check some simple cases
    assert candidate("apple") == False
    assert candidate("apple pi e") == True
    assert candidate("eeeee") == False
    assert candidate("A") == True
    assert candidate("Pumpkin pie ") == False
    assert candidate("Pumpkin pie 1") == False
    assert candidate("") == False
    assert candidate("eeeee e ") == False
    assert candidate("apple pie") == False
    assert candidate("apple pi e ") == False

    # Check some edge cases that are easy to work out by hand.
    assert True

 </pre>
###### traceback
<pre>   Cell In[1], line 18
    ```
    ^
SyntaxError: invalid syntax
 </pre>
### HumanEval/62
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.


def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
 </pre>
###### answer
<pre> ```
def derivative(xs):
    result = []

    # Calculate the derivative of each term in the polynomial
    for i in range(len(xs)):
        term = xs[i]
        if i > 0:
            term *= (i + 1)
        result.append(term)

    return result
``` </pre>
###### canonical_solution
<pre>     return [(i * x) for i, x in enumerate(xs)][1:]
 </pre>
###### test
<pre> 

METADATA = {}


def check(candidate):
    assert candidate([3, 1, 2, 4, 5]) == [1, 4, 12, 20]
    assert candidate([1, 2, 3]) == [2, 6]
    assert candidate([3, 2, 1]) == [2, 2]
    assert candidate([3, 2, 1, 0, 4]) == [2, 2, 0, 16]
    assert candidate([1]) == []

 </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 43
     38     assert candidate([3, 2, 1, 0, 4]) == [2, 2, 0, 16]
     39     assert candidate([1]) == []
---> 43 check(derivative)
Cell In[1], line 35, in check(candidate)
     34 def check(candidate):
---> 35     assert candidate([3, 1, 2, 4, 5]) == [1, 4, 12, 20]
     36     assert candidate([1, 2, 3]) == [2, 6]
     37     assert candidate([3, 2, 1]) == [2, 2]
AssertionError:  </pre>
### HumanEval/96
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.

def count_up_to(n):
    """Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n.
    for example:
    count_up_to(5) => [2,3]
    count_up_to(11) => [2,3,5,7]
    count_up_to(0) => []
    count_up_to(20) => [2,3,5,7,11,13,17,19]
    count_up_to(1) => []
    count_up_to(18) => [2,3,5,7,11,13,17]
    """
 </pre>
###### answer
<pre> ```
def count_up_to(n):
    if n == 0:
        return []
    elif n <= 1:
        return []

    primes = []
  
    for i in range(2, n + 1):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
        
        if len(primes) == n:
            return primes
    
    return primes[:n]
``` </pre>
###### canonical_solution
<pre>     primes = []
    for i in range(2, n):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes

 </pre>
###### test
<pre> def check(candidate):

    assert candidate(5) == [2,3]
    assert candidate(6) == [2,3,5]
    assert candidate(7) == [2,3,5]
    assert candidate(10) == [2,3,5,7]
    assert candidate(0) == []
    assert candidate(22) == [2,3,5,7,11,13,17,19]
    assert candidate(1) == []
    assert candidate(18) == [2,3,5,7,11,13,17]
    assert candidate(47) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]
    assert candidate(101) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

 </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 55
     50     assert candidate(47) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]
     51     assert candidate(101) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
---> 55 check(count_up_to)
Cell In[1], line 42, in check(candidate)
     40 def check(candidate):
---> 42     assert candidate(5) == [2,3]
     43     assert candidate(6) == [2,3,5]
     44     assert candidate(7) == [2,3,5]
AssertionError:  </pre>
### HumanEval/128
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.

def prod_signs(arr):
    """
    You are given an array arr of integers and you need to return
    sum of magnitudes of integers multiplied by product of all signs
    of each number in the array, represented by 1, -1 or 0.
    Note: return None for empty arr.

    Example:
    >>> prod_signs([1, 2, 2, -4]) == -9
    >>> prod_signs([0, 1]) == 0
    >>> prod_signs([]) == None
    """
 </pre>
###### answer
<pre> ```
def prod_signs(arr):
    if not arr:
        return None

    prod_of_signs = 1
    sum_of_magnitudes = 0

    for num in arr:
        if num == 0:
            continue
        elif num > 0:
            prod_of_signs *= 1
        else:
            prod_of_signs *= -1

        sum_of_magnitudes += abs(num)

    return sum_of_magnitudes * prod_of_signs
``` </pre>
###### canonical_solution
<pre>     if not arr: return None
    prod = 0 if 0 in arr else (-1) ** len(list(filter(lambda x: x < 0, arr)))
    return prod * sum([abs(i) for i in arr])
 </pre>
###### test
<pre> def check(candidate):

    # Check some simple cases
    assert True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate([1, 2, 2, -4]) == -9
    assert candidate([0, 1]) == 0
    assert candidate([1, 1, 1, 2, 3, -1, 1]) == -10
    assert candidate([]) == None
    assert candidate([2, 4,1, 2, -1, -1, 9]) == 20
    assert candidate([-1, 1, -1, 1]) == 4
    assert candidate([-1, 1, 1, 1]) == -4
    assert candidate([-1, 1, 1, 0]) == 0

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"

 </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 56
     51     # Check some edge cases that are easy to work out by hand.
     52     assert True, "This prints if this assert fails 2 (also good for debugging!)"
---> 56 check(prod_signs)
Cell In[1], line 43, in check(candidate)
     41 assert True, "This prints if this assert fails 1 (good for debugging!)"
     42 assert candidate([1, 2, 2, -4]) == -9
---> 43 assert candidate([0, 1]) == 0
     44 assert candidate([1, 1, 1, 2, 3, -1, 1]) == -10
     45 assert candidate([]) == None
AssertionError:  </pre>
### HumanEval/87
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.

def get_row(lst, x):
    """
    You are given a 2 dimensional data, as a nested lists,
    which is similar to matrix, however, unlike matrices,
    each row may contain a different number of columns.
    Given lst, and integer x, find integers x in the list,
    and return list of tuples, [(x1, y1), (x2, y2) ...] such that
    each tuple is a coordinate - (row, columns), starting with 0.
    Sort coordinates initially by rows in ascending order.
    Also, sort coordinates of the row by columns in descending order.
    
    Examples:
    get_row([
      [1,2,3,4,5,6],
      [1,2,3,4,1,6],
      [1,2,3,4,5,1]
    ], 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
    get_row([], 1) == []
    get_row([[], [1], [1, 2, 3]], 3) == [(2, 2)]
    """
 </pre>
###### answer
<pre> ```
def get_row(lst, x):
    result = []

    for i, row in enumerate(lst):
        if x in row:
            row_index = i
            column_index = row.index(x)
            result.append((row_index, column_index))

    return sorted(result, key=lambda x: (x[0], -x[1]))
``` </pre>
###### canonical_solution
<pre>     coords = [(i, j) for i in range(len(lst)) for j in range(len(lst[i])) if lst[i][j] == x]
    return sorted(sorted(coords, key=lambda x: x[1], reverse=True), key=lambda x: x[0])
 </pre>
###### test
<pre> def check(candidate):

    # Check some simple cases
    assert candidate([
        [1,2,3,4,5,6],
        [1,2,3,4,1,6],
        [1,2,3,4,5,1]
    ], 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
    assert candidate([
        [1,2,3,4,5,6],
        [1,2,3,4,5,6],
        [1,2,3,4,5,6],
        [1,2,3,4,5,6],
        [1,2,3,4,5,6],
        [1,2,3,4,5,6]
    ], 2) == [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1)]
    assert candidate([
        [1,2,3,4,5,6],
        [1,2,3,4,5,6],
        [1,1,3,4,5,6],
        [1,2,1,4,5,6],
        [1,2,3,1,5,6],
        [1,2,3,4,1,6],
        [1,2,3,4,5,1]
    ], 1) == [(0, 0), (1, 0), (2, 1), (2, 0), (3, 2), (3, 0), (4, 3), (4, 0), (5, 4), (5, 0), (6, 5), (6, 0)]
    assert candidate([], 1) == []
    assert candidate([[1]], 2) == []
    assert candidate([[], [1], [1, 2, 3]], 3) == [(2, 2)]

    # Check some edge cases that are easy to work out by hand.
    assert True

 </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 72
     67     # Check some edge cases that are easy to work out by hand.
     68     assert True
---> 72 check(get_row)
Cell In[1], line 41, in check(candidate)
     38 def check(candidate):
     39 
     40     # Check some simple cases
---> 41     assert candidate([
     42         [1,2,3,4,5,6],
     43         [1,2,3,4,1,6],
     44         [1,2,3,4,5,1]
     45     ], 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
     46     assert candidate([
     47         [1,2,3,4,5,6],
     48         [1,2,3,4,5,6],
   (...)
     52         [1,2,3,4,5,6]
     53     ], 2) == [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1)]
     54     assert candidate([
     55         [1,2,3,4,5,6],
     56         [1,2,3,4,5,6],
   (...)
     61         [1,2,3,4,5,1]
     62     ], 1) == [(0, 0), (1, 0), (2, 1), (2, 0), (3, 2), (3, 0), (4, 3), (4, 0), (5, 4), (5, 0), (6, 5), (6, 0)]
AssertionError:  </pre>
