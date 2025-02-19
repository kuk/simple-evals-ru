# humaneval / gigachat-max
### HumanEval/77
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.

def iscube(a):
    '''
    Write a function that takes an integer a and returns True 
    if this ingeger is a cube of some integer number.
    Note: you may assume the input is always valid.
    Examples:
    iscube(1) ==> True
    iscube(2) ==> False
    iscube(-1) ==> True
    iscube(64) ==> True
    iscube(0) ==> True
    iscube(180) ==> False
    '''
 </pre>
###### answer
<pre> ```python
import math

def iscube(a):
    # Check if the absolute value of 'a' is a perfect cube by taking its cube root
    cube_root = abs(a) ** (1/3)
    
    # Check if the cube root is an integer
    return cube_root.is_integer()
``` </pre>
###### canonical_solution
<pre>     a = abs(a)
    return int(round(a ** (1. / 3))) ** 3 == a
 </pre>
###### test
<pre> def check(candidate):

    # Check some simple cases
    assert candidate(1) == True, "First test error: " + str(candidate(1))
    assert candidate(2) == False, "Second test error: " + str(candidate(2))
    assert candidate(-1) == True, "Third test error: " + str(candidate(-1))
    assert candidate(64) == True, "Fourth test error: " + str(candidate(64))
    assert candidate(180) == False, "Fifth test error: " + str(candidate(180))
    assert candidate(1000) == True, "Sixth test error: " + str(candidate(1000))


    # Check some edge cases that are easy to work out by hand.
    assert candidate(0) == True, "1st edge test error: " + str(candidate(0))
    assert candidate(1729) == False, "2nd edge test error: " + str(candidate(1728))

 </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 46
     41     assert candidate(0) == True, "1st edge test error: " + str(candidate(0))
     42     assert candidate(1729) == False, "2nd edge test error: " + str(candidate(1728))
---> 46 check(iscube)
Cell In[1], line 35, in check(candidate)
     33 assert candidate(2) == False, "Second test error: " + str(candidate(2))
     34 assert candidate(-1) == True, "Third test error: " + str(candidate(-1))
---> 35 assert candidate(64) == True, "Fourth test error: " + str(candidate(64))
     36 assert candidate(180) == False, "Fifth test error: " + str(candidate(180))
     37 assert candidate(1000) == True, "Sixth test error: " + str(candidate(1000))
AssertionError: Fourth test error: False </pre>
### HumanEval/95
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.

def check_dict_case(dict):
    """
    Given a dictionary, return True if all keys are strings in lower 
    case or all keys are strings in upper case, else return False.
    The function should return False is the given dictionary is empty.
    Examples:
    check_dict_case({"a":"apple", "b":"banana"}) should return True.
    check_dict_case({"a":"apple", "A":"banana", "B":"banana"}) should return False.
    check_dict_case({"a":"apple", 8:"banana", "a":"apple"}) should return False.
    check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}) should return False.
    check_dict_case({"STATE":"NC", "ZIP":"12345" }) should return True.
    """
 </pre>
###### answer
<pre> ```python
def check_dict_case(dict):
    # Check if the dictionary is empty
    if not dict:
        return False

    # Get the first key to determine its case (upper or lower)
    first_key = next(iter(dict))
    
    # Determine the expected case based on the first key
    expected_case = str.islower(first_key) if isinstance(first_key, str) else None

    # Iterate through the remaining keys to ensure they match the expected case
    for key in dict.keys():
        if isinstance(key, str):
            if expected_case == 'lower':
                if not key.islower():
                    return False
            elif expected_case == 'upper':
                if not key.isupper():
                    return False
            else:
                return False
        else:
            return False

    # If no mismatches found, return True
    return True
``` </pre>
###### canonical_solution
<pre>     if len(dict.keys()) == 0:
        return False
    else:
        state = "start"
        for key in dict.keys():

            if isinstance(key, str) == False:
                state = "mixed"
                break
            if state == "start":
                if key.isupper():
                    state = "upper"
                elif key.islower():
                    state = "lower"
                else:
                    break
            elif (state == "upper" and not key.isupper()) or (state == "lower" and not key.islower()):
                    state = "mixed"
                    break
            else:
                break
        return state == "upper" or state == "lower" 
 </pre>
###### test
<pre> def check(candidate):

    # Check some simple cases
    assert candidate({"p":"pineapple", "b":"banana"}) == True, "First test error: " + str(candidate({"p":"pineapple", "b":"banana"}))
    assert candidate({"p":"pineapple", "A":"banana", "B":"banana"}) == False, "Second test error: " + str(candidate({"p":"pineapple", "A":"banana", "B":"banana"}))
    assert candidate({"p":"pineapple", 5:"banana", "a":"apple"}) == False, "Third test error: " + str(candidate({"p":"pineapple", 5:"banana", "a":"apple"}))
    assert candidate({"Name":"John", "Age":"36", "City":"Houston"}) == False, "Fourth test error: " + str(candidate({"Name":"John", "Age":"36", "City":"Houston"}))
    assert candidate({"STATE":"NC", "ZIP":"12345" }) == True, "Fifth test error: " + str(candidate({"STATE":"NC", "ZIP":"12345" }))      
    assert candidate({"fruit":"Orange", "taste":"Sweet" }) == True, "Fourth test error: " + str(candidate({"fruit":"Orange", "taste":"Sweet" }))      


    # Check some edge cases that are easy to work out by hand.
    assert candidate({}) == False, "1st edge test error: " + str(candidate({}))

 </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 63
     58     # Check some edge cases that are easy to work out by hand.
     59     assert candidate({}) == False, "1st edge test error: " + str(candidate({}))
---> 63 check(check_dict_case)
Cell In[1], line 50, in check(candidate)
     47 def check(candidate):
     48 
     49     # Check some simple cases
---> 50     assert candidate({"p":"pineapple", "b":"banana"}) == True, "First test error: " + str(candidate({"p":"pineapple", "b":"banana"}))
     51     assert candidate({"p":"pineapple", "A":"banana", "B":"banana"}) == False, "Second test error: " + str(candidate({"p":"pineapple", "A":"banana", "B":"banana"}))
     52     assert candidate({"p":"pineapple", 5:"banana", "a":"apple"}) == False, "Third test error: " + str(candidate({"p":"pineapple", 5:"banana", "a":"apple"}))
AssertionError: First test error: False </pre>
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
    # Make a copy of the original array to avoid modifying it
    sorted_array = array.copy()
    
    # Calculate the sum of the first and last elements
    first_last_sum = sorted_array[0] + sorted_array[-1]
    
    # Sort the copied array based on whether the sum is odd or even
    if first_last_sum % 2 == 1:
        sorted_array.sort()  # Ascending order
    else:
        sorted_array.sort(reverse=True)  # Descending order

    return sorted_array
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
###### traceback
<pre> ---------------------------------------------------------------------------IndexError                                Traceback (most recent call last)Cell In[1], line 54
     49     assert candidate([15, 42, 87, 32 ,11, 0]) == [0, 11, 15, 32, 42, 87], "Error"
     50     assert candidate([21, 14, 23, 11]) == [23, 21, 14, 11], "Error"
---> 54 check(sort_array)
Cell In[1], line 41, in check(candidate)
     37 def check(candidate):
     38 
     39     # Check some simple cases
     40     assert True, "This prints if this assert fails 1 (good for debugging!)"
---> 41     assert candidate([]) == [], "Error"
     42     assert candidate([5]) == [5], "Error"
     43     assert candidate([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5], "Error"
Cell In[1], line 26, in sort_array(array)
     23 sorted_array = array.copy()
     25 # Calculate the sum of the first and last elements
---> 26 first_last_sum = sorted_array[0] + sorted_array[-1]
     28 # Sort the copied array based on whether the sum is odd or even
     29 if first_last_sum % 2 == 1:
IndexError: list index out of range </pre>
### HumanEval/84
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.

def solve(N):
    """Given a positive integer N, return the total sum of its digits in binary.
    
    Example
        For N = 1000, the sum of digits will be 1 the output should be "1".
        For N = 150, the sum of digits will be 6 the output should be "110".
        For N = 147, the sum of digits will be 12 the output should be "1100".
    
    Variables:
        @N integer
             Constraints: 0 ≤ N ≤ 10000.
    Output:
         a string of binary number
    """
 </pre>
###### answer
<pre> ```python
def solve(N):
    # Convert N to binary format as a string
    binary_representation = bin(N)[2:]
    
    # Calculate the sum of all digits in the binary representation
    digit_sum = sum(int(digit) for digit in binary_representation)
    
    # Return the sum converted back to binary format as a string
    return bin(digit_sum)[2:]
``` </pre>
###### canonical_solution
<pre>     return bin(sum(int(i) for i in str(N)))[2:]
 </pre>
###### test
<pre> def check(candidate):

    # Check some simple cases
    assert True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate(1000) == "1", "Error"
    assert candidate(150) == "110", "Error"
    assert candidate(147) == "1100", "Error"

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"
    assert candidate(333) == "1001", "Error"
    assert candidate(963) == "10010", "Error"

 </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 46
     41     assert candidate(333) == "1001", "Error"
     42     assert candidate(963) == "10010", "Error"
---> 46 check(solve)
Cell In[1], line 35, in check(candidate)
     31 def check(candidate):
     32 
     33     # Check some simple cases
     34     assert True, "This prints if this assert fails 1 (good for debugging!)"
---> 35     assert candidate(1000) == "1", "Error"
     36     assert candidate(150) == "110", "Error"
     37     assert candidate(147) == "1100", "Error"
AssertionError: Error </pre>
### HumanEval/122
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.

def add_elements(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:

        Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4
        Output: 24 # sum of 21 + 3

    Constraints:
        1. 1 &lt;= len(arr) &lt;= 100
        2. 1 &lt;= k &lt;= len(arr)
    """
 </pre>
###### answer
<pre> ```python
def add_elements(arr, k):
    total_sum = 0
    
    for i in range(k):
        if 10 &lt;= arr[i] &lt; 100:
            total_sum += arr[i]
            
    return total_sum
``` </pre>
###### canonical_solution
<pre>     return sum(elem for elem in arr[:k] if len(str(elem)) &lt;= 2)
 </pre>
###### test
<pre> def check(candidate):

    # Check some simple cases
    assert candidate([1,-2,-3,41,57,76,87,88,99], 3) == -4
    assert candidate([111,121,3,4000,5,6], 2) == 0
    assert candidate([11,21,3,90,5,6,7,8,9], 4) == 125
    assert candidate([111,21,3,4000,5,6,7,8,9], 4) == 24, "This prints if this assert fails 1 (good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    assert candidate([1], 1) == 1, "This prints if this assert fails 2 (also good for debugging!)"

 </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 43
     38     # Check some edge cases that are easy to work out by hand.
     39     assert candidate([1], 1) == 1, "This prints if this assert fails 2 (also good for debugging!)"
---> 43 check(add_elements)
Cell In[1], line 33, in check(candidate)
     30 def check(candidate):
     31 
     32     # Check some simple cases
---> 33     assert candidate([1,-2,-3,41,57,76,87,88,99], 3) == -4
     34     assert candidate([111,121,3,4000,5,6], 2) == 0
     35     assert candidate([11,21,3,90,5,6,7,8,9], 4) == 125
AssertionError:  </pre>
### HumanEval/125
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.

def split_words(txt):
    '''
    Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
    should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the
    alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
    Examples
    split_words("Hello world!") ➞ ["Hello", "world!"]
    split_words("Hello,world!") ➞ ["Hello", "world!"]
    split_words("abcdef") == 3 
    '''
 </pre>
###### answer
<pre> ```python
def split_words(txt):
    # Split by whitespace first
    words = txt.split()
    
    # If there are no whitespaces, try splitting by commas
    if len(words) == 1:
        words = txt.split(',')
        
        # If still one word after splitting by commas, count lowercase letters with odd order in the alphabet
        if len(words) == 1:
            count = sum(1 for c in txt.lower() if (ord(c) - ord('a')) % 2 != 0)
            return count
    
    return words
``` </pre>
###### canonical_solution
<pre>     if " " in txt:
        return txt.split()
    elif "," in txt:
        return txt.replace(',',' ').split()
    else:
        return len([i for i in txt if i.islower() and ord(i)%2 == 0])
 </pre>
###### test
<pre> def check(candidate):

    assert candidate("Hello world!") == ["Hello","world!"]
    assert candidate("Hello,world!") == ["Hello","world!"]
    assert candidate("Hello world,!") == ["Hello","world,!"]
    assert candidate("Hello,Hello,world !") == ["Hello,Hello,world","!"]
    assert candidate("abcdef") == 3
    assert candidate("aaabb") == 2
    assert candidate("aaaBb") == 1
    assert candidate("") == 0
 </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 44
     40     assert candidate("aaaBb") == 1
     41     assert candidate("") == 0
---> 44 check(split_words)
Cell In[1], line 40, in check(candidate)
     38 assert candidate("abcdef") == 3
     39 assert candidate("aaabb") == 2
---> 40 assert candidate("aaaBb") == 1
     41 assert candidate("") == 0
AssertionError:  </pre>
### HumanEval/102
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.

def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
 </pre>
###### answer
<pre> ```python
def choose_num(x, y):
    # Ensure x &lt;= y by swapping if necessary
    if x > y:
        x, y = y, x

    # Iterate through the range from y to x (inclusive)
    for num in range(y, x-1, -1):
        # Check if the current number is even
        if num % 2 == 0:
            return num

    # If no even number found within the range, return -1
    return -1
``` </pre>
###### canonical_solution
<pre>     if x > y:
        return -1
    if y % 2 == 0:
        return y
    if x == y:
        return -1
    return y - 1
 </pre>
###### test
<pre> def check(candidate):

    # Check some simple cases
    assert candidate(12, 15) == 14
    assert candidate(13, 12) == -1
    assert candidate(33, 12354) == 12354
    assert candidate(5234, 5233) == -1
    assert candidate(6, 29) == 28
    assert candidate(27, 10) == -1

    # Check some edge cases that are easy to work out by hand.
    assert candidate(7, 7) == -1
    assert candidate(546, 546) == 546

 </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 46
     41     assert candidate(7, 7) == -1
     42     assert candidate(546, 546) == 546
---> 46 check(choose_num)
Cell In[1], line 34, in check(candidate)
     30 def check(candidate):
     31 
     32     # Check some simple cases
     33     assert candidate(12, 15) == 14
---> 34     assert candidate(13, 12) == -1
     35     assert candidate(33, 12354) == 12354
     36     assert candidate(5234, 5233) == -1
AssertionError:  </pre>
### HumanEval/93
###### instruction
<pre> Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.

def encode(message):
    """
    Write a function that takes a message, and encodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. 
    Assume only letters. 
    
    Examples:
    >>> encode('test')
    'TGST'
    >>> encode('This is a message')
    'tHKS KS C MGSSCGG'
    """
 </pre>
###### answer
<pre> ```python
def encode(message):
    encoded_message = []
    vowels = {'a': 'c', 'e': 'g', 'i': 'k', 'o': 'q', 'u': 'w'}
    
    for char in message:
        if char.isalpha():
            # Swap case
            if char.islower():
                encoded_char = char.upper()
            else:
                encoded_char = char.lower()
            
            # Replace vowels
            if char.lower() in vowels:
                encoded_char = vowels[char.lower()]
                
            encoded_message.append(encoded_char)
        else:
            encoded_message.append(char)
    
    return ''.join(encoded_message)
```

This implementation follows the instructions provided by the docstring. It swaps the case of each character and replaces vowels with the corresponding letter two positions ahead in the English alphabet. </pre>
###### canonical_solution
<pre>     vowels = "aeiouAEIOU"
    vowels_replace = dict([(i, chr(ord(i) + 2)) for i in vowels])
    message = message.swapcase()
    return ''.join([vowels_replace[i] if i in vowels else i for i in message])
 </pre>
###### test
<pre> def check(candidate):

    # Check some simple cases
    assert candidate('TEST') == 'tgst', "This prints if this assert fails 1 (good for debugging!)"
    assert candidate('Mudasir') == 'mWDCSKR', "This prints if this assert fails 2 (good for debugging!)"
    assert candidate('YES') == 'ygs', "This prints if this assert fails 3 (good for debugging!)"
    
    # Check some edge cases that are easy to work out by hand.
    assert candidate('This is a message') == 'tHKS KS C MGSSCGG', "This prints if this assert fails 2 (also good for debugging!)"
    assert candidate("I DoNt KnOw WhAt tO WrItE") == 'k dQnT kNqW wHcT Tq wRkTg', "This prints if this assert fails 2 (also good for debugging!)"

 </pre>
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 56
     51     assert candidate('This is a message') == 'tHKS KS C MGSSCGG', "This prints if this assert fails 2 (also good for debugging!)"
     52     assert candidate("I DoNt KnOw WhAt tO WrItE") == 'k dQnT kNqW wHcT Tq wRkTg', "This prints if this assert fails 2 (also good for debugging!)"
---> 56 check(encode)
Cell In[1], line 47, in check(candidate)
     43 def check(candidate):
     44 
     45     # Check some simple cases
     46     assert candidate('TEST') == 'tgst', "This prints if this assert fails 1 (good for debugging!)"
---> 47     assert candidate('Mudasir') == 'mWDCSKR', "This prints if this assert fails 2 (good for debugging!)"
     48     assert candidate('YES') == 'ygs', "This prints if this assert fails 3 (good for debugging!)"
     50     # Check some edge cases that are easy to work out by hand.
AssertionError: This prints if this assert fails 2 (good for debugging!) </pre>
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
<pre> ```python
def compare_one(a, b):
    # Convert both arguments to float, handling possible commas as decimal points
    try:
        a_float = float(a.replace(',', '.'))
        b_float = float(b.replace(',', '.'))
        
        if a_float > b_float:
            return a
        elif b_float > a_float:
            return b
        else:
            return None
    except ValueError:
        raise TypeError("Arguments must be integers, floats, or strings representing real numbers.")
```

This implementation handles the cases where either `a` or `b` can be an integer, float, or string representation of a real number (with either `.` or `,` as the decimal separator). It converts both inputs to floats, compares them, and returns the larger value in its original form. If the values are equal, it returns `None`. </pre>
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
<pre> ---------------------------------------------------------------------------AttributeError                            Traceback (most recent call last)Cell In[1], line 51
     46     # Check some edge cases that are easy to work out by hand.
     47     assert True
---> 51 check(compare_one)
Cell In[1], line 37, in check(candidate)
     34 def check(candidate):
     35 
     36     # Check some simple cases
---> 37     assert candidate(1, 2) == 2
     38     assert candidate(1, 2.5) == 2.5
     39     assert candidate(2, 3) == 3
Cell In[1], line 21, in compare_one(a, b)
     18 def compare_one(a, b):
     19     # Convert both arguments to float, handling possible commas as decimal points
     20     try:
---> 21         a_float = float(a.replace(',', '.'))
     22         b_float = float(b.replace(',', '.'))
     24         if a_float > b_float:
AttributeError: 'int' object has no attribute 'replace' </pre>
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
<pre> ```python
from functools import cmp_to_key

def digit_sum(n):
    return sum(int(digit) for digit in str(abs(n)))

def order_by_points(nums):
    def compare(a, b):
        sum_a = digit_sum(a)
        sum_b = digit_sum(b)
        
        if sum_a != sum_b:
            return sum_a - sum_b
        else:
            # If sums are equal, maintain original order
            return nums.index(a) - nums.index(b)
    
    sorted_nums = sorted(nums, key=cmp_to_key(compare))
    return sorted_nums
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
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 52
     47     # Check some edge cases that are easy to work out by hand.
     48     assert True, "This prints if this assert fails 2 (also good for debugging!)"
---> 52 check(order_by_points)
Cell In[1], line 40, in check(candidate)
     37 def check(candidate):
     38 
     39     # Check some simple cases
---> 40     assert candidate([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
     41     assert candidate([1234,423,463,145,2,423,423,53,6,37,3457,3,56,0,46]) == [0, 2, 3, 6, 53, 423, 423, 423, 1234, 145, 37, 46, 56, 463, 3457]
     42     assert candidate([]) == []
AssertionError:  </pre>
