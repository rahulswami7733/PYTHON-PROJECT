# Q. Preprocessing of dataset
import nltk
import string
import re
# text lowercase
def  text_lowercase(text):
    print(text.lower())
input_str="Hello ALL of you"
text_lowercase(input_str)

# rmove number

def remove_number(text):
    result=re.sub(r'\d+','',text)
    print (result)
inpute_str="there 33:bages, and 44 pen"
print(inpute_str)
remove_number(inpute_str) 


