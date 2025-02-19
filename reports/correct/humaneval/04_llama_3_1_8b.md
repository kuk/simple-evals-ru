# humaneval / llama-3.1-8b
### HumanEval/13
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.


def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
 </pre>
###### answer
<pre> def greatest_common_divisor(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a </pre>
###### canonical_solution
<pre>     while b:
        a, b = b, a % b
    return a
 </pre>
###### test
<pre> 

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate(3, 7) == 1
    assert candidate(10, 15) == 5
    assert candidate(49, 14) == 7
    assert candidate(144, 60) == 12
 </pre>
### HumanEval/88
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.

def sort_array(array):
    """
    Given an array of non-negative integers, return a copy of the given array after sorting,
    you will sort the given array in ascending order if the sum( first index value, last index value) is odd,
    or sort it in descending order if the sum( first index value, last index value) is even.

    Note:
    * don't change the given array.

    Examples:
    * sort_array([]) => []
    * sort_array([5]) => [5]
    * sort_array([2, 4, 3, 0, 1, 5]) => [0, 1, 2, 3, 4, 5]
    * sort_array([2, 4, 3, 0, 1, 5, 6]) => [6, 5, 4, 3, 2, 1, 0]
    """
 </pre>
###### answer
<pre> ```python
def sort_array(array):
    """
    Given an array of non-negative integers, return a copy of the given array after sorting,
    you will sort the given array in ascending order if the sum( first index value, last index value) is odd,
    or sort it in descending order if the sum( first index value, last index value) is even.

    Note:
    * don't change the given array.

    Examples:
    * sort_array([]) => []
    * sort_array([5]) => [5]
    * sort_array([2, 4, 3, 0, 1, 5]) => [0, 1, 2, 3, 4, 5]
    * sort_array([2, 4, 3, 0, 1, 5, 6]) => [6, 5, 4, 3, 2, 1, 0]
    """
    if not array:
        return array

    first_index_value = array[0]
    last_index_value = array[-1]
    sum_of_first_last = first_index_value + last_index_value

    if sum_of_first_last % 2 == 0:
        return sorted(array, reverse=True)
    else:
        return sorted(array)
``` </pre>
###### canonical_solution
<pre>     return [] if len(array) == 0 else sorted(array, reverse= (array[0]+array[-1]) % 2 == 0) 
 </pre>
###### test
<pre> def check(candidate):

    # Check some simple cases
    assert True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate([]) == [], "Error"
    assert candidate([5]) == [5], "Error"
    assert candidate([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5], "Error"
    assert candidate([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0], "Error"

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"
    assert candidate([2, 1]) == [1, 2], "Error"
    assert candidate([15, 42, 87, 32 ,11, 0]) == [0, 11, 15, 32, 42, 87], "Error"
    assert candidate([21, 14, 23, 11]) == [23, 21, 14, 11], "Error"

 </pre>
### HumanEval/27
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.


def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
 </pre>
###### answer
<pre> def flip_case(string: str) -> str:
    return ''.join(c.upper() if c.islower() else c.lower() for c in string) </pre>
###### canonical_solution
<pre>     return string.swapcase()
 </pre>
###### test
<pre> 

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('') == ''
    assert candidate('Hello!') == 'hELLO!'
    assert candidate('These violent delights have violent ends') == 'tHESE VIOLENT DELIGHTS HAVE VIOLENT ENDS'
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
<pre> ```python
def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.
    """
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            for k in range(j+1, len(l)):
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
### HumanEval/78
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.

def hex_key(num):
    """You have been tasked to write a function that receives 
    a hexadecimal number as a string and counts the number of hexadecimal 
    digits that are primes (prime number, or a prime, is a natural number 
    greater than 1 that is not a product of two smaller natural numbers).
    Hexadecimal digits are 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F.
    Prime numbers are 2, 3, 5, 7, 11, 13, 17,...
    So you have to determine a number of the following digits: 2, 3, 5, 7, 
    B (=decimal 11), D (=decimal 13).
    Note: you may assume the input is always correct or empty string, 
    and symbols A,B,C,D,E,F are always uppercase.
    Examples:
    For num = "AB" the output should be 1.
    For num = "1077E" the output should be 2.
    For num = "ABED1A33" the output should be 4.
    For num = "123456789ABCDEF0" the output should be 6.
    For num = "2020" the output should be 2.
    """
 </pre>
###### answer
<pre> ```python
def hex_key(num):
    """
    Counts the number of hexadecimal digits that are primes.

    Args:
        num (str): A hexadecimal number as a string.

    Returns:
        int: The number of hexadecimal digits that are primes.
    """
    # Define a set of prime hexadecimal digits
    prime_hex_digits = {'2', '3', '5', '7', 'B', 'D'}

    # Initialize a counter for prime hexadecimal digits
    count = 0

    # Iterate over each character in the input string
    for char in num:
        # Check if the character is a prime hexadecimal digit
        if char in prime_hex_digits:
            # If it is, increment the counter
            count += 1

    # Return the count of prime hexadecimal digits
    return count
``` </pre>
###### canonical_solution
<pre>     primes = ('2', '3', '5', '7', 'B', 'D')
    total = 0
    for i in range(0, len(num)):
        if num[i] in primes:
            total += 1
    return total
 </pre>
###### test
<pre> def check(candidate):

    # Check some simple cases
    assert candidate("AB") == 1, "First test error: " + str(candidate("AB"))      
    assert candidate("1077E") == 2, "Second test error: " + str(candidate("1077E"))  
    assert candidate("ABED1A33") == 4, "Third test error: " + str(candidate("ABED1A33"))      
    assert candidate("2020") == 2, "Fourth test error: " + str(candidate("2020"))  
    assert candidate("123456789ABCDEF0") == 6, "Fifth test error: " + str(candidate("123456789ABCDEF0"))      
    assert candidate("112233445566778899AABBCCDDEEFF00") == 12, "Sixth test error: " + str(candidate("112233445566778899AABBCCDDEEFF00"))  


    # Check some edge cases that are easy to work out by hand.
    assert candidate([]) == 0

 </pre>
### HumanEval/2
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.


def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
 </pre>
###### answer
<pre> def truncate_number(number: float) -> float:
    return number - int(number) </pre>
###### canonical_solution
<pre>     return number % 1.0
 </pre>
###### test
<pre> 

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate(3.5) == 0.5
    assert abs(candidate(1.33) - 0.33) &lt; 1e-6
    assert abs(candidate(123.456) - 0.456) &lt; 1e-6
 </pre>
### HumanEval/148
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.

def bf(planet1, planet2):
    '''
    There are eight planets in our solar system: the closerst to the Sun 
    is Mercury, the next one is Venus, then Earth, Mars, Jupiter, Saturn, 
    Uranus, Neptune.
    Write a function that takes two planet names as strings planet1 and planet2. 
    The function should return a tuple containing all planets whose orbits are 
    located between the orbit of planet1 and the orbit of planet2, sorted by 
    the proximity to the sun. 
    The function should return an empty tuple if planet1 or planet2
    are not correct planet names. 
    Examples
    bf("Jupiter", "Neptune") ==> ("Saturn", "Uranus")
    bf("Earth", "Mercury") ==> ("Venus")
    bf("Mercury", "Uranus") ==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    '''
 </pre>
###### answer
<pre> ```python
def bf(planet1, planet2):
    '''
    There are eight planets in our solar system: the closerst to the Sun 
    is Mercury, the next one is Venus, then Earth, Mars, Jupiter, Saturn, 
    Uranus, Neptune.
    Write a function that takes two planet names as strings planet1 and planet2. 
    The function should return a tuple containing all planets whose orbits are 
    located between the orbit of planet1 and the orbit of planet2, sorted by 
    the proximity to the sun. 
    The function should return an empty tuple if planet1 or planet2
    are not correct planet names. 
    Examples
    bf("Jupiter", "Neptune") ==> ("Saturn", "Uranus")
    bf("Earth", "Mercury") ==> ("Venus")
    bf("Mercury", "Uranus") ==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    '''
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 not in planets or planet2 not in planets:
        return ()
    
    index1 = planets.index(planet1)
    index2 = planets.index(planet2)
    
    if index1 > index2:
        index1, index2 = index2, index1
    
    return tuple(planets[index1 + 1:index2])
``` </pre>
###### canonical_solution
<pre>     planet_names = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    if planet1 not in planet_names or planet2 not in planet_names or planet1 == planet2:
        return ()
    planet1_index = planet_names.index(planet1)
    planet2_index = planet_names.index(planet2)
    if planet1_index &lt; planet2_index:
        return (planet_names[planet1_index + 1: planet2_index])
    else:
        return (planet_names[planet2_index + 1 : planet1_index])
 </pre>
###### test
<pre> def check(candidate):

    # Check some simple cases
    assert candidate("Jupiter", "Neptune") == ("Saturn", "Uranus"), "First test error: " + str(len(candidate("Jupiter", "Neptune")))      
    assert candidate("Earth", "Mercury") == ("Venus",), "Second test error: " + str(candidate("Earth", "Mercury"))  
    assert candidate("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn"), "Third test error: " + str(candidate("Mercury", "Uranus"))      
    assert candidate("Neptune", "Venus") == ("Earth", "Mars", "Jupiter", "Saturn", "Uranus"), "Fourth test error: " + str(candidate("Neptune", "Venus"))  


    # Check some edge cases that are easy to work out by hand.
    assert candidate("Earth", "Earth") == ()
    assert candidate("Mars", "Earth") == ()
    assert candidate("Jupiter", "Makemake") == ()

 </pre>
### HumanEval/64
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.

FIX = """
Add more test cases.
"""

def vowels_count(s):
    """Write a function vowels_count which takes a string representing
    a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.

    Example:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """
 </pre>
###### answer
<pre> ```python
def vowels_count(s):
    """
    Write a function vowels_count which takes a string representing
    a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.

    Example:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """
    vowels = 'aeiou'
    count = 0
    for char in s:
        if char.lower() in vowels:
            count += 1
        elif char.lower() == 'y' and s.endswith(char):
            count += 1
    return count
``` </pre>
###### canonical_solution
<pre>     vowels = "aeiouAEIOU"
    n_vowels = sum(c in vowels for c in s)
    if s[-1] == 'y' or s[-1] == 'Y':
        n_vowels += 1
    return n_vowels
 </pre>
###### test
<pre> def check(candidate):

    # Check some simple cases
    assert candidate("abcde") == 2, "Test 1"
    assert candidate("Alone") == 3, "Test 2"
    assert candidate("key") == 2, "Test 3"
    assert candidate("bye") == 1, "Test 4"
    assert candidate("keY") == 2, "Test 5"
    assert candidate("bYe") == 1, "Test 6"
    assert candidate("ACEDY") == 3, "Test 7"

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"

 </pre>
### HumanEval/58
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.


def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
 </pre>
###### answer
<pre> def common(l1: list, l2: list):
    """
    Return sorted unique common elements for two lists.

    Args:
        l1 (list): The first list.
        l2 (list): The second list.

    Returns:
        list: A sorted list of unique common elements.
    """
    # Convert the lists to sets to remove duplicates and improve lookup efficiency
    set1 = set(l1)
    set2 = set(l2)
    
    # Find the intersection of the two sets (i.e., the common elements)
    common_elements = set1 & set2
    
    # Convert the set back to a list and sort it
    common_elements = sorted(list(common_elements))
    
    return common_elements </pre>
###### canonical_solution
<pre>     ret = set()
    for e1 in l1:
        for e2 in l2:
            if e1 == e2:
                ret.add(e1)
    return sorted(list(ret))
 </pre>
###### test
<pre> 

METADATA = {}


def check(candidate):
    assert candidate([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]) == [1, 5, 653]
    assert candidate([5, 3, 2, 8], [3, 2]) == [2, 3]
    assert candidate([4, 3, 2, 8], [3, 2, 4]) == [2, 3, 4]
    assert candidate([4, 3, 2, 8], []) == []

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
<pre> def sort_numbers(numbers: str) -> str:
    num_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    numbers_list = numbers.split()
    sorted_numbers = sorted(numbers_list, key=lambda x: num_dict[x])
    return ' '.join(sorted_numbers) </pre>
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
