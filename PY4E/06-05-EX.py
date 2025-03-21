# Ex6.5 Take the following Python code that stores a string.
# Use 'find' and string slicing to extract the portion of the string after the colon character
# and then use the float function to convert the extracted string into a floating point number.
str = 'X-DSPAM-Confidence: 0.8475 '
start = str.find(":")
print(start)
mystring = str[start+1:]
print(mystring)
myfloat = print(float(mystring))
