# string is an object that represents a sequence of characters in Python.
# Strings are enclosed in either single quotes (' ') or double quotes (" ").
message = """
This is a multi-line string.
It can span multiple lines."""
print(message)

myname = "Rishabh"
print(len(myname))  # len() function returns the length of the string   
print(myname[0])    # Accessing first character of the string using indexing
print(myname[-1])   # Accessing last character of the string using negative indexing
print(myname[0:4])  # Slicing the string from index 0 to 3
print(myname[4:6])  # Slicing the string from index 4 to 5
print(myname[1:6:2]) # Slicing with a step of 2
print(myname[:2]) # Slicing from start to index 1
print(myname[::2]) # Slicing with a step of 2 from start to end

# string methods
myname.upper()  # Converts string to uppercase
myname.lower()  # Converts string to lowercase
myname.replace("Rishabh", "Rishu")  # Replaces substring with another substring
newname = "uttrakhand"
newname.replace("Uttar", "Uttarak")  # Replaces substring with another substring
print(newname) # prints "uttrakhand" as strings are immutable
myname.index(newname) # Returns the index of the first occurrence of the substring
myname.count("h")  # Counts the occurrences of a substring in the string
myname.find("h")  # Returns the index of the first occurrence of the substring "h" in myname    
print(myname.rfind("h"))    # Returns the index of the last occurrence of the substring "h" in myname
myname.join("Hello") # Joins the elements of the iterable with myname as the separator
myname.split("h") # Splits the string at each occurrence of "h" 


str1 = "Ranger"
str2 = "Power"
# Concatenation
str3 = str1 + " " + str2
print(str3)  # Output: Ranger Power
# String formatting 
print(f"My name is {myname} and I am from {newname}")
print("My name is {} and I am from {}".format(myname, newname)) # Using format() method for string formatting
print("My name is %s and I am from %s" % (myname, newname)) # Using % operator for string formatting