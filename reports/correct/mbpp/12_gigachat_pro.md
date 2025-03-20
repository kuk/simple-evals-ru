# mbpp / gigachat-pro
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
    while n > 0:
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
### 167
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a python function to find the smallest power of 2 greater than or equal to n.

Your code should pass these tests:

assert next_power_of_2(0) == 1
assert next_power_of_2(5) == 8
assert next_power_of_2(17) == 32

Your response should only contain the code for this function.

def next_power_of_2(n): 
    ...


 </pre>
###### answer
<pre> ```python
def next_power_of_2(n):
    if n &lt;= 0:
        return 1
    
    result = 1
    while result &lt; n:
        result &lt;&lt;= 1  # equivalent to result = result * 2
        
    return result
``` </pre>
###### canonical_solution
<pre> def next_power_of_2(n): 
  if n and not n & (n - 1):
    return n

  count = 0
  while n != 0: 
    n >>= 1
    count += 1

  return 1 &lt;&lt; count;  </pre>
###### test
<pre> assert next_power_of_2(0) == 1
assert next_power_of_2(5) == 8
assert next_power_of_2(17) == 32 </pre>
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
    return char.join(str1.split())
``` </pre>
###### canonical_solution
<pre> def replace_blank(str1,char):
 str2 = str1.replace(' ', char)
 return str2 </pre>
###### test
<pre> assert replace_blank("hello people",'@')==("hello@people")
assert replace_blank("python program language",'$')==("python$program$language")
assert replace_blank("blank space","-")==("blank-space") </pre>
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
    return {k: v for k, v in dict1.items() if v is not None}
``` </pre>
###### canonical_solution
<pre> def drop_empty(dict1):
  dict1 = {key:value for (key, value) in dict1.items() if value is not None}
  return dict1 </pre>
###### test
<pre> assert drop_empty({'c1': 'Red', 'c2': 'Green', 'c3':None})=={'c1': 'Red', 'c2': 'Green'}
assert drop_empty({'c1': 'Red', 'c2': None, 'c3':None})=={'c1': 'Red'}
assert drop_empty({'c1': None, 'c2': 'Green', 'c3':None})=={ 'c2': 'Green'} </pre>
### 455
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to check whether the given month number contains 31 days or not.

Your code should pass these tests:

assert check_monthnumb_number(5)==True
assert check_monthnumb_number(2)==False
assert check_monthnumb_number(6)==False

Your response should only contain the code for this function.

def check_monthnumb_number(monthnum2):
    ...


 </pre>
###### answer
<pre> ```python
def check_monthnumb_number(monthnum2):
    if monthnum2 in {1, 3, 5, 7, 8, 10, 12}:
        return True
    else:
        return False
``` </pre>
###### canonical_solution
<pre> def check_monthnumb_number(monthnum2):
  if(monthnum2==1 or monthnum2==3 or monthnum2==5 or monthnum2==7 or monthnum2==8 or monthnum2==10 or monthnum2==12):
    return True
  else:
    return False </pre>
###### test
<pre> assert check_monthnumb_number(5)==True
assert check_monthnumb_number(2)==False
assert check_monthnumb_number(6)==False </pre>
### 66
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a python function to count the number of positive numbers in a list.

Your code should pass these tests:

assert pos_count([1,-2,3,-4]) == 2
assert pos_count([3,4,5,-1]) == 3
assert pos_count([1,2,3,4]) == 4

Your response should only contain the code for this function.

def pos_count(list):
    ...


 </pre>
###### answer
<pre> ```python
def pos_count(lst):
    return len([num for num in lst if num > 0])
``` </pre>
###### canonical_solution
<pre> def pos_count(list):
  pos_count= 0
  for num in list: 
    if num >= 0: 
      pos_count += 1
  return pos_count  </pre>
###### test
<pre> assert pos_count([1,-2,3,-4]) == 2
assert pos_count([3,4,5,-1]) == 3
assert pos_count([1,2,3,4]) == 4 </pre>
### 87
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to merge three dictionaries into a single dictionary.

Your code should pass these tests:

assert merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" }, { "G": "Green", "W": "White" },{ "O": "Orange", "W": "White", "B": "Black" })=={'B': 'Black', 'R': 'Red', 'P': 'Pink', 'G': 'Green', 'W': 'White', 'O': 'Orange'}
assert merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" }, { "G": "Green", "W": "White" },{"L":"lavender","B":"Blue"})=={'W': 'White', 'P': 'Pink', 'B': 'Black', 'R': 'Red', 'G': 'Green', 'L': 'lavender'}
assert merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" },{"L":"lavender","B":"Blue"},{ "G": "Green", "W": "White" })=={'B': 'Black', 'P': 'Pink', 'R': 'Red', 'G': 'Green', 'L': 'lavender', 'W': 'White'}

Your response should only contain the code for this function.

def merge_dictionaries_three(dict1,dict2, dict3):
    ...


 </pre>
###### answer
<pre> ```python
def merge_dictionaries_three(dict1, dict2, dict3):
    # Initialize an empty list to store all keys from the input dictionaries
    all_keys = set(dict1.keys()) | set(dict2.keys()) | set(dict3.keys())
    
    # Initialize a new dictionary to hold the merged result
    result = {}
    
    # Iterate over each key in the set of all keys
    for key in all_keys:
        # Retrieve values from respective dictionaries if present, otherwise default to None
        value1 = dict1.get(key, None)
        value2 = dict2.get(key, None)
        value3 = dict3.get(key, None)
        
        # Choose the non-None value among the three dictionaries (prioritize based on your logic)
        final_value = value1 or value2 or value3
        
        # Add the key-value pair to the result dictionary
        result[key] = final_value
    
    return result
``` </pre>
###### canonical_solution
<pre> import collections as ct
def merge_dictionaries_three(dict1,dict2, dict3):
    merged_dict = dict(ct.ChainMap({},dict1,dict2,dict3))
    return merged_dict </pre>
###### test
<pre> assert merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" }, { "G": "Green", "W": "White" },{ "O": "Orange", "W": "White", "B": "Black" })=={'B': 'Black', 'R': 'Red', 'P': 'Pink', 'G': 'Green', 'W': 'White', 'O': 'Orange'}
assert merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" }, { "G": "Green", "W": "White" },{"L":"lavender","B":"Blue"})=={'W': 'White', 'P': 'Pink', 'B': 'Black', 'R': 'Red', 'G': 'Green', 'L': 'lavender'}
assert merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" },{"L":"lavender","B":"Blue"},{ "G": "Green", "W": "White" })=={'B': 'Black', 'P': 'Pink', 'R': 'Red', 'G': 'Green', 'L': 'lavender', 'W': 'White'} </pre>
### 56
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a python function to check if a given number is one less than twice its reverse.

Your code should pass these tests:

assert check(70) == False
assert check(23) == False
assert check(73) == True

Your response should only contain the code for this function.

def rev(num):    
    ...


 </pre>
###### answer
<pre> ```python
def rev(num): 
    return int(str(abs(num))[::-1])  # Function to reverse the number

def check(number): 
    revered_number = rev(number) 
    return (revered_number &lt; number) and ((number + 1) == revered_number * 2) 
``` </pre>
###### canonical_solution
<pre> def rev(num):    
    rev_num = 0
    while (num > 0):  
        rev_num = (rev_num * 10 + num % 10) 
        num = num // 10  
    return rev_num  
def check(n):    
    return (2 * rev(n) == n + 1)   </pre>
###### test
<pre> assert check(70) == False
assert check(23) == False
assert check(73) == True </pre>
### 118
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to convert a string to a list of strings split on the space character.

Your code should pass these tests:

assert string_to_list("python programming")==['python','programming']
assert string_to_list("lists tuples strings")==['lists','tuples','strings']
assert string_to_list("write a program")==['write','a','program']

Your response should only contain the code for this function.

def string_to_list(string): 
    ...


 </pre>
###### answer
<pre> ```python
def string_to_list(string): 
    return string.split()
``` </pre>
###### canonical_solution
<pre> def string_to_list(string): 
    lst = list(string.split(" ")) 
    return lst </pre>
###### test
<pre> assert string_to_list("python programming")==['python','programming']
assert string_to_list("lists tuples strings")==['lists','tuples','strings']
assert string_to_list("write a program")==['write','a','program'] </pre>
### 82
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to find the volume of a sphere.

Your code should pass these tests:

import math

assert math.isclose(volume_sphere(10), 4188.790204786391, rel_tol=0.001)
assert math.isclose(volume_sphere(25), 65449.84694978735, rel_tol=0.001)
assert math.isclose(volume_sphere(20), 33510.32163829113, rel_tol=0.001)

Your response should only contain the code for this function.

def volume_sphere(r):
    ...


 </pre>
###### answer
<pre> ```python
def volume_sphere(r):
    return (4/3) * math.pi * r**3
``` </pre>
###### canonical_solution
<pre> import math
def volume_sphere(r):
  volume=(4/3)*math.pi*r*r*r
  return volume </pre>
###### test
<pre> import math

assert math.isclose(volume_sphere(10), 4188.790204786391, rel_tol=0.001)
assert math.isclose(volume_sphere(25), 65449.84694978735, rel_tol=0.001)
assert math.isclose(volume_sphere(20), 33510.32163829113, rel_tol=0.001) </pre>
