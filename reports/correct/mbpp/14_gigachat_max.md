# mbpp / gigachat-max
### 59
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to find the nth octagonal number.

Your code should pass these tests:

assert is_octagonal(5) == 65
assert is_octagonal(10) == 280
assert is_octagonal(15) == 645

Your response should only contain the code for this function.

def is_octagonal(n): 
    ...


 </pre>
###### answer
<pre> ```python
def is_octagonal(n):
    return n * (3 * n - 2)
```

This function calculates the \(n\)-th octagonal number using the formula \(O_n = n \times (3n - 2)\). </pre>
###### canonical_solution
<pre> def is_octagonal(n): 
	return 3 * n * n - 2 * n  </pre>
###### test
<pre> assert is_octagonal(5) == 65
assert is_octagonal(10) == 280
assert is_octagonal(15) == 645 </pre>
### 161
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to remove all elements from a given list present in another list.

Your code should pass these tests:

assert remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]) == [1, 3, 5, 7, 9, 10]
assert remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 3, 5, 7]) == [2, 4, 6, 8, 9, 10]
assert remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [5, 7]) == [1, 2, 3, 4, 6, 8, 9, 10]

Your response should only contain the code for this function.

def remove_elements(list1, list2):
    ...


 </pre>
###### answer
<pre> ```python
def remove_elements(list1, list2):
    return [item for item in list1 if item not in set(list2)]
```

This implementation uses a list comprehension to filter out elements of `list1` that are also found in `list2`. Converting `list2` to a set improves the efficiency of checking whether an element is present in `list2`, making it more efficient than using a simple list. </pre>
###### canonical_solution
<pre> def remove_elements(list1, list2):
    result = [x for x in list1 if x not in list2]
    return result </pre>
###### test
<pre> assert remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]) == [1, 3, 5, 7, 9, 10]
assert remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 3, 5, 7]) == [2, 4, 6, 8, 9, 10]
assert remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [5, 7]) == [1, 2, 3, 4, 6, 8, 9, 10] </pre>
### 141
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to sort a list of elements.

Your code should pass these tests:

assert pancake_sort([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79]
assert pancake_sort([98, 12, 54, 36, 85]) == [12, 36, 54, 85, 98]
assert pancake_sort([41, 42, 32, 12, 23]) == [12, 23, 32, 41, 42]

Your response should only contain the code for this function.

def pancake_sort(nums):
    ...


 </pre>
###### answer
<pre> ```python
def pancake_sort(nums):
    n = len(nums)
    
    # Iterate through all elements in the array
    for i in range(n-1, 0, -1):
        max_idx = find_max_index(nums, i + 1)  # Find index of the maximum element in nums[:i+1]
        
        if max_idx != i:
            flip(nums, max_idx)                # Flip to bring the max element to the front
            flip(nums, i)                      # Flip again to move the max element to its correct position
            
    return nums


# Helper function to find the index of the maximum value in nums[:end]
def find_max_index(nums, end):
    max_val = float('-inf')
    max_idx = None
    
    for j in range(end):
        if nums[j] > max_val:
            max_val = nums[j]
            max_idx = j
    
    return max_idx


# Helper function to reverse nums[:k+1]
def flip(nums, k):
    start = 0
    while start &lt; k:
        nums[start], nums[k] = nums[k], nums[start]
        start += 1
        k -= 1
```

This implementation follows the Pancake Sort algorithm. The `pancake_sort` function sorts the input list by repeatedly finding the maximum element within a subarray and flipping it into place using two helper functions: `find_max_index` and `flip`. </pre>
###### canonical_solution
<pre> def pancake_sort(nums):
    arr_len = len(nums)
    while arr_len > 1:
        mi = nums.index(max(nums[0:arr_len]))
        nums = nums[mi::-1] + nums[mi+1:len(nums)]
        nums = nums[arr_len-1::-1] + nums[arr_len:len(nums)]
        arr_len -= 1
    return nums </pre>
###### test
<pre> assert pancake_sort([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79]
assert pancake_sort([98, 12, 54, 36, 85]) == [12, 36, 54, 85, 98]
assert pancake_sort([41, 42, 32, 12, 23]) == [12, 23, 32, 41, 42] </pre>
### 276
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function that takes in the radius and height of a cylinder and returns the the volume.

Your code should pass these tests:

import math

assert math.isclose(volume_cylinder(10,5), 1570.7500000000002, rel_tol=0.001)
assert math.isclose(volume_cylinder(4,5), 251.32000000000002, rel_tol=0.001)
assert math.isclose(volume_cylinder(4,10), 502.64000000000004, rel_tol=0.001)

Your response should only contain the code for this function.

def volume_cylinder(r,h):
    ...


 </pre>
###### answer
<pre> ```python
def volume_cylinder(r, h):
    return math.pi * r**2 * h
``` </pre>
###### canonical_solution
<pre> def volume_cylinder(r,h):
  volume=3.1415*r*r*h
  return volume </pre>
###### test
<pre> import math

assert math.isclose(volume_cylinder(10,5), 1570.7500000000002, rel_tol=0.001)
assert math.isclose(volume_cylinder(4,5), 251.32000000000002, rel_tol=0.001)
assert math.isclose(volume_cylinder(4,10), 502.64000000000004, rel_tol=0.001) </pre>
### 131
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a python function to reverse only the vowels of a given string (where y is not a vowel).

Your code should pass these tests:

assert reverse_vowels("Python") == "Python"
assert reverse_vowels("USA") == "ASU"
assert reverse_vowels("ab") == "ab"

Your response should only contain the code for this function.

def reverse_vowels(str1):
    ...


 </pre>
###### answer
<pre> ```python
def reverse_vowels(s):
    vowels = 'aeiouAEIOU'
    string_list = list(s)
    i, j = 0, len(string_list) - 1
    
    while i &lt; j:
        if string_list[i] in vowels and string_list[j] in vowels:
            string_list[i], string_list[j] = string_list[j], string_list[i]
            i += 1
            j -= 1
        elif string_list[i] not in vowels:
            i += 1
        elif string_list[j] not in vowels:
            j -= 1
            
    return ''.join(string_list)
``` </pre>
###### canonical_solution
<pre> def reverse_vowels(str1):
	vowels = ""
	for char in str1:
		if char in "aeiouAEIOU":
			vowels += char
	result_string = ""
	for char in str1:
		if char in "aeiouAEIOU":
			result_string += vowels[-1]
			vowels = vowels[:-1]
		else:
			result_string += char
	return result_string </pre>
###### test
<pre> assert reverse_vowels("Python") == "Python"
assert reverse_vowels("USA") == "ASU"
assert reverse_vowels("ab") == "ab" </pre>
### 105
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a python function to count true booleans in the given list.

Your code should pass these tests:

assert count([True,False,True]) == 2
assert count([False,False]) == 0
assert count([True,True,True]) == 3

Your response should only contain the code for this function.

def count(lst):   
    ...


 </pre>
###### answer
<pre> ```python
def count(lst):
    return sum(1 for x in lst if x)
```

This function uses a generator expression to iterate over the list `lst` and counts each element that evaluates to `True`. The `sum()` function then adds up all these elements to give the total number of `True` values in the list. </pre>
###### canonical_solution
<pre> def count(lst):   
    return sum(lst)  </pre>
###### test
<pre> assert count([True,False,True]) == 2
assert count([False,False]) == 0
assert count([True,True,True]) == 3 </pre>
### 294
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to find the maximum value in a given heterogeneous list.

Your code should pass these tests:

assert max_val(['Python', 3, 2, 4, 5, 'version'])==5
assert max_val(['Python', 15, 20, 25])==25
assert max_val(['Python', 30, 20, 40, 50, 'version'])==50

Your response should only contain the code for this function.

def max_val(listval):
    ...


 </pre>
###### answer
<pre> ```python
def max_val(listval):
    # Filter out non-numeric values from the list
    numeric_values = [x for x in listval if isinstance(x, (int, float))]
    
    # Return the maximum of the filtered list or None if no numeric values are found
    return max(numeric_values) if numeric_values else None
```

This implementation filters out all non-numeric values from the input list using `isinstance` to check for integers and floats. It then returns the maximum value from the remaining numeric values using the built-in `max()` function. If there are no numeric values in the list, it returns `None`. </pre>
###### canonical_solution
<pre> def max_val(listval):
     max_val = max(i for i in listval if isinstance(i, int)) 
     return(max_val) </pre>
###### test
<pre> assert max_val(['Python', 3, 2, 4, 5, 'version'])==5
assert max_val(['Python', 15, 20, 25])==25
assert max_val(['Python', 30, 20, 40, 50, 'version'])==50 </pre>
### 450
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to extract specified size of strings from a given list of string values.

Your code should pass these tests:

assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,8)==['practice', 'solution']
assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,6)==['Python']
assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,9)==['exercises']

Your response should only contain the code for this function.

def extract_string(str, l):
    ...


 </pre>
###### answer
<pre> ```python
def extract_string(strings, length):
    return [string for string in strings if len(string) == length]
```

This function takes a list of strings (`strings`) and an integer (`length`), then returns a new list containing all strings whose length matches the provided `length`. </pre>
###### canonical_solution
<pre> def extract_string(str, l):
    result = [e for e in str if len(e) == l] 
    return result </pre>
###### test
<pre> assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,8)==['practice', 'solution']
assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,6)==['Python']
assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,9)==['exercises'] </pre>
### 456
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to reverse each string in a given list of string values.

Your code should pass these tests:

assert reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black'])==['deR', 'neerG', 'eulB', 'etihW', 'kcalB']
assert reverse_string_list(['john','amal','joel','george'])==['nhoj','lama','leoj','egroeg']
assert reverse_string_list(['jack','john','mary'])==['kcaj','nhoj','yram']

Your response should only contain the code for this function.

def reverse_string_list(stringlist):
    ...


 </pre>
###### answer
<pre> ```python
def reverse_string_list(stringlist):
    reversed_strings = []
    for s in stringlist:
        reversed_strings.append(s[::-1])
    return reversed_strings
``` </pre>
###### canonical_solution
<pre> def reverse_string_list(stringlist):
    result = [x[::-1] for x in stringlist]
    return result </pre>
###### test
<pre> assert reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black'])==['deR', 'neerG', 'eulB', 'etihW', 'kcalB']
assert reverse_string_list(['john','amal','joel','george'])==['nhoj','lama','leoj','egroeg']
assert reverse_string_list(['jack','john','mary'])==['kcaj','nhoj','yram'] </pre>
### 280
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function that takes in an array and element and returns a tuple containing a boolean that indicates if the element is in the array and the index position of the element (or -1 if the element is not found).

Your code should pass these tests:

assert sequential_search([11,23,58,31,56,77,43,12,65,19],31) == (True, 3)
assert sequential_search([12, 32, 45, 62, 35, 47, 44, 61],61) == (True, 7)
assert sequential_search([9, 10, 17, 19, 22, 39, 48, 56],48) == (True, 6)

Your response should only contain the code for this function.

def sequential_search(dlist, item):
    ...


 </pre>
###### answer
<pre> ```python
def sequential_search(dlist, item):
    for i in range(len(dlist)):
        if dlist[i] == item:
            return True, i
    return False, -1
``` </pre>
###### canonical_solution
<pre> def sequential_search(dlist, item):
    pos = 0
    found = False
    while pos &lt; len(dlist) and not found:
        if dlist[pos] == item:
            found = True
        else:
            pos = pos + 1
    return found, pos </pre>
###### test
<pre> assert sequential_search([11,23,58,31,56,77,43,12,65,19],31) == (True, 3)
assert sequential_search([12, 32, 45, 62, 35, 47, 44, 61],61) == (True, 7)
assert sequential_search([9, 10, 17, 19, 22, 39, 48, 56],48) == (True, 6) </pre>
