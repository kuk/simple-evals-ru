# mbpp / yandexgpt-5-lite
### 422
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a python function to find the average of cubes of first n natural numbers.

Your code should pass these tests:

assert find_Average_Of_Cube(2) == 4.5
assert find_Average_Of_Cube(3) == 12
assert find_Average_Of_Cube(1) == 1

Your response should only contain the code for this function.

def find_Average_Of_Cube(n):  
    ...


 </pre>
###### answer
<pre> ```
def find_Average_Of_Cube(n):
    sum_of_cubes = 0
    for i in range(1, n+1):
        sum_of_cubes += i**3
    average = sum_of_cubes / n
    return average
``` </pre>
###### canonical_solution
<pre> def find_Average_Of_Cube(n):  
    sum = 0
    for i in range(1, n + 1): 
        sum += i * i * i  
    return round(sum / n, 6)  </pre>
###### test
<pre> assert find_Average_Of_Cube(2) == 4.5
assert find_Average_Of_Cube(3) == 12
assert find_Average_Of_Cube(1) == 1 </pre>
### 16
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to that returns true if the input string contains sequences of lowercase letters joined with an underscore and false otherwise.

Your code should pass these tests:

assert text_lowercase_underscore("aab_cbbbc")==(True)
assert text_lowercase_underscore("aab_Abbbc")==(False)
assert text_lowercase_underscore("Aaab_abbbc")==(False)

Your response should only contain the code for this function.

def text_lowercase_underscore(text):
    ...


 </pre>
###### answer
<pre> ```
def text_lowercase_underscore(text):
    return all(c.islower() for c in text if c != '_') and '_'.join(c for c in text if c != '_').islower()
``` </pre>
###### canonical_solution
<pre> import re
def text_lowercase_underscore(text):
        patterns = '^[a-z]+_[a-z]+$'
        if re.search(patterns,  text):
                return True
        else:
                return False </pre>
###### test
<pre> assert text_lowercase_underscore("aab_cbbbc")==(True)
assert text_lowercase_underscore("aab_Abbbc")==(False)
assert text_lowercase_underscore("Aaab_abbbc")==(False) </pre>
### 441
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to find the surface area of a cube of a given size.

Your code should pass these tests:

assert surfacearea_cube(5)==150
assert surfacearea_cube(3)==54
assert surfacearea_cube(10)==600

Your response should only contain the code for this function.

def surfacearea_cube(l):
    ...


 </pre>
###### answer
<pre> ```
def surfacearea_cube(l):
    return 6 * l ** 2
``` </pre>
###### canonical_solution
<pre> def surfacearea_cube(l):
  surfacearea= 6*l*l
  return surfacearea </pre>
###### test
<pre> assert surfacearea_cube(5)==150
assert surfacearea_cube(3)==54
assert surfacearea_cube(10)==600 </pre>
### 232
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function that takes in a list and an integer n and returns a list containing the n largest items from the list.

Your code should pass these tests:

assert set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2))==set([100,90])
assert set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],5))==set([100,90,80,70,60])
assert set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],3))==set([100,90,80])

Your response should only contain the code for this function.

def larg_nnum(list1,n):
    ...


 </pre>
###### answer
<pre> ```
def larg_nnum(list1, n):
    return sorted(list1, reverse=True)[:n]
``` </pre>
###### canonical_solution
<pre> import heapq
def larg_nnum(list1,n):
 largest=heapq.nlargest(n,list1)
 return largest </pre>
###### test
<pre> assert set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2))==set([100,90])
assert set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],5))==set([100,90,80,70,60])
assert set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],3))==set([100,90,80]) </pre>
### 18
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to remove characters from the first string which are present in the second string.

Your code should pass these tests:

assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'
assert remove_dirty_chars("digitalindia", "talent") == 'digiidi'
assert remove_dirty_chars("exoticmiles", "toxic") == 'emles'

Your response should only contain the code for this function.

def str_to_list(string): 
    ...


 </pre>
###### answer
<pre> ```
def remove_dirty_chars(s1, s2):
    result = ''.join([c for c in s1 if c not in s2])
    return result
``` </pre>
###### canonical_solution
<pre> NO_OF_CHARS = 256
def str_to_list(string): 
	temp = [] 
	for x in string: 
		temp.append(x) 
	return temp 
def lst_to_string(List): 
	return ''.join(List) 
def get_char_count_array(string): 
	count = [0] * NO_OF_CHARS 
	for i in string: 
		count[ord(i)] += 1
	return count 
def remove_dirty_chars(string, second_string): 
	count = get_char_count_array(second_string) 
	ip_ind = 0
	res_ind = 0
	temp = '' 
	str_list = str_to_list(string) 
	while ip_ind != len(str_list): 
		temp = str_list[ip_ind] 
		if count[ord(temp)] == 0: 
			str_list[res_ind] = str_list[ip_ind] 
			res_ind += 1
		ip_ind+=1
	return lst_to_string(str_list[0:res_ind])  </pre>
###### test
<pre> assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'
assert remove_dirty_chars("digitalindia", "talent") == 'digiidi'
assert remove_dirty_chars("exoticmiles", "toxic") == 'emles' </pre>
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
    return ''.join([char for char in str1 if not char.isupper()])
``` </pre>
###### canonical_solution
<pre> import re
def remove_uppercase(str1):
  return re.sub('[A-Z]', '', str1) </pre>
###### test
<pre> assert remove_uppercase('cAstyoUrFavoRitETVshoWs') == 'cstyoravoitshos'
assert remove_uppercase('wAtchTheinTernEtrAdIo') == 'wtchheinerntrdo'
assert remove_uppercase('VoicESeaRchAndreComMendaTionS') == 'oiceachndreomendaion' </pre>
### 127
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to multiply two integers.

Your code should pass these tests:

assert multiply_int(10,20)==200
assert multiply_int(5,10)==50
assert multiply_int(4,8)==32

Your response should only contain the code for this function.

def multiply_int(x, y):
    ...


 </pre>
###### answer
<pre> def multiply_int(x, y):
    return x * y </pre>
###### canonical_solution
<pre> def multiply_int(x, y):
    if y &lt; 0:
        return -multiply_int(x, -y)
    elif y == 0:
        return 0
    elif y == 1:
        return x
    else:
        return x + multiply_int(x, y - 1) </pre>
###### test
<pre> assert multiply_int(10,20)==200
assert multiply_int(5,10)==50
assert multiply_int(4,8)==32 </pre>
### 479
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a python function to find the first digit of a given number.

Your code should pass these tests:

assert first_Digit(123) == 1
assert first_Digit(456) == 4
assert first_Digit(12) == 1

Your response should only contain the code for this function.

def first_Digit(n) :  
    ...


 </pre>
###### answer
<pre> ```
def first_Digit(n):
    return int(str(n)[0])
``` </pre>
###### canonical_solution
<pre> def first_Digit(n) :  
    while n >= 10:  
        n = n / 10 
    return int(n)  </pre>
###### test
<pre> assert first_Digit(123) == 1
assert first_Digit(456) == 4
assert first_Digit(12) == 1 </pre>
### 390
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to apply a given format string to all of the elements in a list.

Your code should pass these tests:

assert add_string([1,2,3,4],'temp{0}')==['temp1', 'temp2', 'temp3', 'temp4']
assert add_string(['a','b','c','d'], 'python{0}')==[ 'pythona', 'pythonb', 'pythonc', 'pythond']
assert add_string([5,6,7,8],'string{0}')==['string5', 'string6', 'string7', 'string8']

Your response should only contain the code for this function.

def add_string(list_, string):
    ...


 </pre>
###### answer
<pre> ```
def add_string(list_, string):
    return [string.format(elem) for elem in list_]
``` </pre>
###### canonical_solution
<pre> def add_string(list_, string):
 add_string=[string.format(i) for i in  list_]
 return add_string </pre>
###### test
<pre> assert add_string([1,2,3,4],'temp{0}')==['temp1', 'temp2', 'temp3', 'temp4']
assert add_string(['a','b','c','d'], 'python{0}')==[ 'pythona', 'pythonb', 'pythonc', 'pythond']
assert add_string([5,6,7,8],'string{0}')==['string5', 'string6', 'string7', 'string8'] </pre>
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
