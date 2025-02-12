# humaneval / llama-3.1-8b:yandex
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
<pre> ```python
def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    """
    return sorted(s0) == sorted(s1)
``` </pre>
###### pred
<pre> 
def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    """
    return sorted(s0) == sorted(s1)
 </pre>
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
###### traceback
<pre> ---------------------------------------------------------------------------AssertionError                            Traceback (most recent call last)Cell In[1], line 46
     41     assert candidate('eabcdzzzz', 'dddzzzzzzzddddabc') == False
     42     assert candidate('aabb', 'aaccc') == False
---> 46 check(same_chars)
Cell In[1], line 36, in check(candidate)
     35 def check(candidate):
---> 36     assert candidate('eabcdzzzz', 'dddzzzzzzzddeddabc') == True
     37     assert candidate('abcd', 'dddddddabc') == True
     38     assert candidate('dddddddabc', 'abcd') == True
AssertionError:  </pre>
