# mbpp / yandexgpt-4-lite
### 459
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to remove uppercase substrings from a given string.

Your code should pass these tests:

assert remove_uppercase('cAstyoUrFavoRitETVshoWs') == 'cstyoravoitshos'
assert remove_uppercase('wAtchTheinTernEtrAdIo') == 'wtchheinerntrdo'
assert remove_uppercase('VoicESeaRchAndreComMendaTionS') == 'oiceachndreomendaion'

Your response should only contain the code for this function.

def remove_uppercase(str1):
    ...


 </pre>
###### answer
<pre> ```
def remove_uppercase(str1):
    return ''.join(c for c in str1 if not c.isupper())
``` </pre>
###### canonical_solution
<pre> import re
def remove_uppercase(str1):
  return re.sub('[A-Z]', '', str1) </pre>
###### test
<pre> assert remove_uppercase('cAstyoUrFavoRitETVshoWs') == 'cstyoravoitshos'
assert remove_uppercase('wAtchTheinTernEtrAdIo') == 'wtchheinerntrdo'
assert remove_uppercase('VoicESeaRchAndreComMendaTionS') == 'oiceachndreomendaion' </pre>
### 406
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a python function to find whether the parity of a given number is odd.

Your code should pass these tests:

assert find_Parity(12) == False
assert find_Parity(7) == True
assert find_Parity(10) == False

Your response should only contain the code for this function.

def find_Parity(x): 
    ...


 </pre>
###### answer
<pre> ```
def find_Parity(x):
    if x % 2 == 1:
        return True
    else:
        return False
``` </pre>
###### canonical_solution
<pre> def find_Parity(x): 
    y = x ^ (x >> 1); 
    y = y ^ (y >> 2); 
    y = y ^ (y >> 4); 
    y = y ^ (y >> 8); 
    y = y ^ (y >> 16); 
    if (y & 1): 
        return True
    return False </pre>
###### test
<pre> assert find_Parity(12) == False
assert find_Parity(7) == True
assert find_Parity(10) == False </pre>
### 460
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a python function to get the first element of each sublist.

Your code should pass these tests:

assert Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]]) == [1, 3, 6]
assert Extract([[1,2,3],[4, 5]]) == [1,4]
assert Extract([[9,8,1],[1,2]]) == [9,1]

Your response should only contain the code for this function.

def Extract(lst): 
    ...


 </pre>
###### answer
<pre> ```
def Extract(lst):
    return [sublist[0] for sublist in lst]
``` </pre>
###### canonical_solution
<pre> def Extract(lst): 
    return [item[0] for item in lst]  </pre>
###### test
<pre> assert Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]]) == [1, 3, 6]
assert Extract([[1,2,3],[4, 5]]) == [1,4]
assert Extract([[9,8,1],[1,2]]) == [9,1] </pre>
### 113
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to check if a string represents an integer or not.

Your code should pass these tests:

assert check_integer("python")==False
assert check_integer("1")==True
assert check_integer("12345")==True

Your response should only contain the code for this function.

def check_integer(text):
    ...


 </pre>
###### answer
<pre> ```
def check_integer(text):
    try:
        int(text)
        return True
    except ValueError:
        return False
``` </pre>
###### canonical_solution
<pre> def check_integer(text):
 text = text.strip()
 if len(text) &lt; 1:
    return None
 else:
     if all(text[i] in "0123456789" for i in range(len(text))):
          return True
     elif (text[0] in "+-") and \
         all(text[i] in "0123456789" for i in range(1,len(text))):
         return True
     else:
        return False </pre>
###### test
<pre> assert check_integer("python")==False
assert check_integer("1")==True
assert check_integer("12345")==True </pre>
### 464
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to check if all values are same in a dictionary.

Your code should pass these tests:

assert check_value({'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12},10)==False
assert check_value({'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12},12)==True
assert check_value({'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12},5)==False

Your response should only contain the code for this function.

def check_value(dict, n):
    ...


 </pre>
###### answer
<pre> ```
def check_value(dict, n):
    return all(value == n for value in dict.values())
``` </pre>
###### canonical_solution
<pre> def check_value(dict, n):
    result = all(x == n for x in dict.values()) 
    return result </pre>
###### test
<pre> assert check_value({'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12},10)==False
assert check_value({'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12},12)==True
assert check_value({'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12},5)==False </pre>
### 272
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function that takes in a list of tuples and returns a list containing the rear element of each tuple.

Your code should pass these tests:

assert rear_extract([(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]) == [21, 20, 19]
assert rear_extract([(1, 'Sai', 36), (2, 'Ayesha', 25), (3, 'Salman', 45)]) == [36, 25, 45]
assert rear_extract([(1, 'Sudeep', 14), (2, 'Vandana', 36), (3, 'Dawood', 56)]) == [14, 36, 56]

Your response should only contain the code for this function.

def rear_extract(test_list):
    ...


 </pre>
###### answer
<pre> ```
def rear_extract(test_list):
    return [tuple[2] for tuple in test_list]
``` </pre>
###### canonical_solution
<pre> def rear_extract(test_list):
  res = [lis[-1] for lis in test_list]
  return (res)  </pre>
###### test
<pre> assert rear_extract([(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]) == [21, 20, 19]
assert rear_extract([(1, 'Sai', 36), (2, 'Ayesha', 25), (3, 'Salman', 45)]) == [36, 25, 45]
assert rear_extract([(1, 'Sudeep', 14), (2, 'Vandana', 36), (3, 'Dawood', 56)]) == [14, 36, 56] </pre>
### 253
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a python function that returns the number of integer elements in a given list.

Your code should pass these tests:

assert count_integer([1,2,'abc',1.2]) == 2
assert count_integer([1,2,3]) == 3
assert count_integer([1,1.2,4,5.1]) == 2

Your response should only contain the code for this function.

def count_integer(list1):
    ...


 </pre>
###### answer
<pre> ```
def count_integer(list1):
    count = 0
    for num in list1:
        if isinstance(num, int):
            count += 1
    return count
``` </pre>
###### canonical_solution
<pre> def count_integer(list1):
    ctr = 0
    for i in list1:
        if isinstance(i, int):
            ctr = ctr + 1
    return ctr </pre>
###### test
<pre> assert count_integer([1,2,'abc',1.2]) == 2
assert count_integer([1,2,3]) == 3
assert count_integer([1,1.2,4,5.1]) == 2 </pre>
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
<pre> ```
def sequential_search(dlist, item):
    for i in range(len(dlist)):
        if dlist[i] == item:
            return (True, i)
    return (False, -1)
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
### 58
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a python function to check whether the given two integers have opposite sign or not.

Your code should pass these tests:

assert opposite_Signs(1,-2) == True
assert opposite_Signs(3,2) == False
assert opposite_Signs(-10,-10) == False
assert opposite_Signs(-2,2) == True

Your response should only contain the code for this function.

def opposite_Signs(x,y): 
    ...


 </pre>
###### answer
<pre> ```
def opposite_Signs(x, y):
    return (x * y &lt; 0)
``` </pre>
###### canonical_solution
<pre> def opposite_Signs(x,y): 
    return ((x ^ y) &lt; 0);  </pre>
###### test
<pre> assert opposite_Signs(1,-2) == True
assert opposite_Signs(3,2) == False
assert opposite_Signs(-10,-10) == False
assert opposite_Signs(-2,2) == True </pre>
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
<pre> ```
def remove_elements(list1, list2):
    return [x for x in list1 if x not in list2]
``` </pre>
###### canonical_solution
<pre> def remove_elements(list1, list2):
    result = [x for x in list1 if x not in list2]
    return result </pre>
###### test
<pre> assert remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]) == [1, 3, 5, 7, 9, 10]
assert remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 3, 5, 7]) == [2, 4, 6, 8, 9, 10]
assert remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [5, 7]) == [1, 2, 3, 4, 6, 8, 9, 10] </pre>
