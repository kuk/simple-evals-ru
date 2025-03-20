# mbpp / ruadapt-qwen-pro-32b
### 287
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a python function takes in an integer n and returns the sum of squares of first n even natural numbers.

Your code should pass these tests:

assert square_Sum(2) == 20
assert square_Sum(3) == 56
assert square_Sum(4) == 120

Your response should only contain the code for this function.

def square_Sum(n):  
    ...


 </pre>
###### answer
<pre> def square_Sum(n):
    return sum((2*i)**2 for i in range(1, n+1))
 </pre>
###### canonical_solution
<pre> def square_Sum(n):  
    return int(2*n*(n+1)*(2*n+1)/3) </pre>
###### test
<pre> assert square_Sum(2) == 20
assert square_Sum(3) == 56
assert square_Sum(4) == 120 </pre>
### 234
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to find the volume of a cube given its side length.

Your code should pass these tests:

assert volume_cube(3)==27
assert volume_cube(2)==8
assert volume_cube(5)==125

Your response should only contain the code for this function.

def volume_cube(l):
    ...


 </pre>
###### answer
<pre> def volume_cube(l):
    return l ** 3
 </pre>
###### canonical_solution
<pre> def volume_cube(l):
  volume = l * l * l
  return volume </pre>
###### test
<pre> assert volume_cube(3)==27
assert volume_cube(2)==8
assert volume_cube(5)==125 </pre>
### 421
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to concatenate each element of tuple by the delimiter.

Your code should pass these tests:

assert concatenate_tuple(("ID", "is", 4, "UTS") ) == 'ID-is-4-UTS'
assert concatenate_tuple(("QWE", "is", 4, "RTY") ) == 'QWE-is-4-RTY'
assert concatenate_tuple(("ZEN", "is", 4, "OP") ) == 'ZEN-is-4-OP'

Your response should only contain the code for this function.

def concatenate_tuple(test_tup):
    ...


 </pre>
###### answer
<pre> ```python
def concatenate_tuple(test_tup):
    return '-'.join(str(element) for element in test_tup)
``` </pre>
###### canonical_solution
<pre> def concatenate_tuple(test_tup):
    delim = "-"
    res = ''.join([str(ele) + delim for ele in test_tup])
    res = res[ : len(res) - len(delim)]
    return (str(res))  </pre>
###### test
<pre> assert concatenate_tuple(("ID", "is", 4, "UTS") ) == 'ID-is-4-UTS'
assert concatenate_tuple(("QWE", "is", 4, "RTY") ) == 'QWE-is-4-RTY'
assert concatenate_tuple(("ZEN", "is", 4, "OP") ) == 'ZEN-is-4-OP' </pre>
### 90
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a python function to find the length of the longest word.

Your code should pass these tests:

assert len_log(["python","PHP","bigdata"]) == 7
assert len_log(["a","ab","abc"]) == 3
assert len_log(["small","big","tall"]) == 5

Your response should only contain the code for this function.

def len_log(list1):
    ...


 </pre>
###### answer
<pre> ```python
def len_log(list1):
    return max(len(word) for word in list1)
```

``` </pre>
###### canonical_solution
<pre> def len_log(list1):
    max=len(list1[0])
    for i in list1:
        if len(i)>max:
            max=len(i)
    return max </pre>
###### test
<pre> assert len_log(["python","PHP","bigdata"]) == 7
assert len_log(["a","ab","abc"]) == 3
assert len_log(["small","big","tall"]) == 5 </pre>
### 409
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to find the minimum product from the pairs of tuples within a given list.

Your code should pass these tests:

assert min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)] )==8
assert min_product_tuple([(10,20), (15,2), (5,10)] )==30
assert min_product_tuple([(11,44), (10,15), (20,5), (12, 9)] )==100

Your response should only contain the code for this function.

def min_product_tuple(list1):
    ...


 </pre>
###### answer
<pre> ```python
def min_product_tuple(list1):
    # Calculate the product of each tuple pair
    products = [a * b for a, b in list1]
    # Return the minimum product
    return min(products)
```

``` </pre>
###### canonical_solution
<pre> def min_product_tuple(list1):
    result_min = min([abs(x * y) for x, y in list1] )
    return result_min </pre>
###### test
<pre> assert min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)] )==8
assert min_product_tuple([(10,20), (15,2), (5,10)] )==30
assert min_product_tuple([(11,44), (10,15), (20,5), (12, 9)] )==100 </pre>
### 412
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a python function to remove odd numbers from a given list.

Your code should pass these tests:

assert remove_odd([1,2,3]) == [2]
assert remove_odd([2,4,6]) == [2,4,6]
assert remove_odd([10,20,3]) == [10,20]

Your response should only contain the code for this function.

def remove_odd(l):
    ...


 </pre>
###### answer
<pre> def remove_odd(l):
    return [x for x in l if x % 2 == 0] </pre>
###### canonical_solution
<pre> def remove_odd(l):
    for i in l:
        if i % 2 != 0:
            l.remove(i)
    return l </pre>
###### test
<pre> assert remove_odd([1,2,3]) == [2]
assert remove_odd([2,4,6]) == [2,4,6]
assert remove_odd([10,20,3]) == [10,20] </pre>
### 125
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to find the maximum difference between the number of 0s and number of 1s in any sub-string of the given binary string.

Your code should pass these tests:

assert find_length("11000010001") == 6
assert find_length("10111") == 1
assert find_length("11011101100101") == 2

Your response should only contain the code for this function.

def find_length(string): 
    ...


 </pre>
###### answer
<pre> def find_length(string):
    max_diff = 0
    current_diff = 0
    for char in string:
        if char == '0':
            current_diff += 1
        else:
            current_diff -= 1
        if current_diff &lt; 0:
            current_diff = 0
        max_diff = max(max_diff, current_diff)
    return max_diff </pre>
###### canonical_solution
<pre> def find_length(string): 
	n = len(string)
	current_sum = 0
	max_sum = 0
	for i in range(n): 
		current_sum += (1 if string[i] == '0' else -1) 
		if current_sum &lt; 0: 
			current_sum = 0
		max_sum = max(current_sum, max_sum) 
	return max_sum if max_sum else 0 </pre>
###### test
<pre> assert find_length("11000010001") == 6
assert find_length("10111") == 1
assert find_length("11011101100101") == 2 </pre>
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
    return [s[::-1] for s in stringlist]
```

``` </pre>
###### canonical_solution
<pre> def reverse_string_list(stringlist):
    result = [x[::-1] for x in stringlist]
    return result </pre>
###### test
<pre> assert reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black'])==['deR', 'neerG', 'eulB', 'etihW', 'kcalB']
assert reverse_string_list(['john','amal','joel','george'])==['nhoj','lama','leoj','egroeg']
assert reverse_string_list(['jack','john','mary'])==['kcaj','nhoj','yram'] </pre>
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
```

``` </pre>
###### canonical_solution
<pre> def drop_empty(dict1):
  dict1 = {key:value for (key, value) in dict1.items() if value is not None}
  return dict1 </pre>
###### test
<pre> assert drop_empty({'c1': 'Red', 'c2': 'Green', 'c3':None})=={'c1': 'Red', 'c2': 'Green'}
assert drop_empty({'c1': 'Red', 'c2': None, 'c3':None})=={'c1': 'Red'}
assert drop_empty({'c1': None, 'c2': 'Green', 'c3':None})=={ 'c2': 'Green'} </pre>
### 432
###### instruction
<pre> Read the following instruction and fully implement the function described.

Write a function to find the median length of a trapezium.

Your code should pass these tests:

assert median_trapezium(15,25,35)==20
assert median_trapezium(10,20,30)==15
assert median_trapezium(6,9,4)==7.5

Your response should only contain the code for this function.

def median_trapezium(base1,base2,height):
    ...


 </pre>
###### answer
<pre> def median_trapezium(base1, base2, height):
    # The median length of a trapezium is the average of the lengths of the two bases
    median_length = (base1 + base2) / 2
    return median_length </pre>
###### canonical_solution
<pre> def median_trapezium(base1,base2,height):
 median = 0.5 * (base1+ base2)
 return median </pre>
###### test
<pre> assert median_trapezium(15,25,35)==20
assert median_trapezium(10,20,30)==15
assert median_trapezium(6,9,4)==7.5 </pre>
