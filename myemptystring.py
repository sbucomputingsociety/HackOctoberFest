# This is my code to check if given string is empty or blank
import re
from collections import Counter
 
sentence = 'Canada is located in the northern part of North America'
# Example I
counter = len(re.findall("a", sentence))
print(counter)
 
# Example II
counter = sentence.count('a')
print(counter)
 
# Example III
counter = Counter(sentence)
print(counter['a'])