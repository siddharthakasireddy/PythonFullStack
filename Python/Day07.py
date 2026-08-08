#Operations on String
# Concatenation
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result) # Output: Hello World
# Repetition
print("Python! " * 3) # Output: Python! Python! Python!
# Indexing
text = "Python"
print(text[0]) # Output: P (1st character)
print(text[-1]) # Output: n (last character)
# Slicing
print(text[0:3]) # Output: Pyt (from index 0 to 2)
print(text[:4]) # Output: Pyth (default start is 0)
print(text[2:]) # Output: thon (from index 2 to end)
# Membership
print('Pyt' in text) # Output: True
print('Java' not in text) # Output: True

#Builtin String Functions

# 1. len()
text = "Hello World"
print(len(text)) # Output: 11
# 2. max() and min()
print(max("abcXYZ")) # Output: 'c' (highest ASCII value)
print(min("abcXYZ")) # Output: 'X' (lowest ASCII value)
# 3. sorted()
print(sorted("python")) # Output: ['h', 'n', 'o', 'p', 't', 'y'] (sorted characters in ascending order)
# 4. chr() and ord()
print(ord('A')) # Output: 65 (ASCII value of 'A')
print(chr(97)) # Output: 'a' (character for ASCII value 97)
