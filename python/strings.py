# Write a program that accepts a string from the user and counts display the number of vowels
user = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0       
for char in user:
    if char in vowels:
        count += 1
print(f"Number of vowels in the string: {count}")

# All string methods and functions 
sample_string = " Hello, World! Welcome to Python programming. "
# 1. Changing case
print(sample_string.upper())  # Convert to uppercase
print(sample_string.lower())  # Convert to lowercase
print(sample_string.title())  # Convert to title case
# 2. Stripping whitespace
print(sample_string.strip())  # Remove leading and trailing whitespace
# 3. Replacing substrings
print(sample_string.replace("World", "Universe"))  # Replace 'World' with 'Universe
# 4. Splitting and joining
words = sample_string.split()  # Split string into a list of words
print(words)
joined_string = "-".join(words)  # Join list of words with hyphen
print(joined_string)
print(squares_even)  # Output: [4, 16, 36, 64, 100]
# 5. Finding substrings
index = sample_string.find("Python")  # Find the index of substring 'Python'
print(f"Index of 'Python': {index}")
# 6. Checking start and end
print(sample_string.startswith(" Hello"))  # Check if string starts with ' Hello'
print(sample_string.endswith("programming. "))  # Check if string ends with 'programming. '
# 7. Length of the string
print(len(sample_string))  # Get the length of the string       
# 8. Counting occurrences
count_o = sample_string.count("o")  # Count occurrences of 'o'
print(f"Occurrences of 'o': {count_o}")     
# 9. Slicing
substring = sample_string[7:12]  # Get substring from index 7 to 11
print(f"Substring (7-12): {substring}") 
# 10. Formatting
name = "Alice"
age = 30
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string) 
# 11. Checking alphanumeric
print(sample_string.isalnum())  # Check if all characters are alphanumeric
print(sample_string.isalpha())  # Check if all characters are alphabetic
print(sample_string.isdigit())  # Check if all characters are digits
print(sample_string.isspace())  # Check if all characters are whitespace
# 12. Reversing a string
reversed_string = sample_string[::-1]
print(f"Reversed string: {reversed_string}")            
# 13. Counting vowels and consonants
vowel_count = 0
consonant_count = 0
for char in sample_string:
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1    
print(f"Vowels: {vowel_count}, Consonants: {consonant_count}")  


#  Write a program that reads a string from keyboard and display 
# The number of uppercase letters in strings
# The number of lowercase letters in string 
# THe number of digits in the string 
# THe number of whitespace characters in the string 
newstring = input("Enter your string: ")
upper_case = 0
lower_case = 0
digit = 0
space = 0
for char in txt:
     if char.isUpper():
        upper_case += 1
     elif char.isLower():
        lower_case += 1
     elif char.isdigit():
        digit += 1
     elif char.isspace():
        space +=1 
print(f'
    Uppers: {upper_case}
    Lowers: {lower_case}')...

# Write a python program that accepts a string from user. Your program should create and display a new string
# where the first and last characters have been exchanged
string = input("Enter here: ")
new_string = ''
new_string += string[-1]+string[1:-1]+string[0]
print(new_string)
