#!/usr/bin/env python
# coding: utf-8

# In[5]:


import re
import pandas as pd


# In[6]:


text='Python Exercise,PHP exercise.'
print(text)
text=text.replace(" ",":").replace(",",":").replace(".",":")
print(text)


# In[24]:


dic={'SUMMARY':['hello,world!','XXXXX test','123four,five:;six...']}
df= pd.DataFrame(dic)
pattern = r'[^\w\s]'
df['SUMMARY'].apply(lambda x: re.sub(pattern,'', x))
print(df)


# In[2]:


def find_words_at_least_four_chars(text):
    pattern=re.compile(r"\b\w{4,}\b")
    return pattern.findall(text)

text='The quick brown fox jumps over the lazy dog.'
print(find_words_at_least_four_chars(text))




# In[3]:


def find_words(text):
    pattern=re.compile(r"\b\w{3,5}\b")
    return pattern.findall(text)

text='the quick brown fox jumps over the lazy dog'
print(find_words(text))



# In[8]:


def remove_parentheses(strings):
    pattern=re.compile(r"\s*\(.*?\)")
    return[pattern.sub("",s) for s in strings]

tex=["example (.com)","hr@fliprobo (.com)","github (.com)"," Hello (Data Science World)","Data (Scientist)"]
print(remove_parentheses(tex))


# In[33]:


import re

# Open the text file and read the contents
with open("C:\Users\rudra\OneDrive\Desktop\hello.txt", 'r') as f:
    text = f.read()

# Remove the leading and trailing square brackets
text = text.strip('[]')

# Split the text into a list of strings
strings = [s.strip().strip('"') for s in text.split(',')]

# Use Regular Expressions to remove the parenthesis area from each string
pattern = re.compile(r'\s*\([^)]*\)')
output = [pattern.sub('', s) for s in strings]

# Print the output
print('[' + ', '.join(f'"{s}"' for s in output) + ']')


# In[39]:


text = "ImportanceOfRegularExpressionsInPython"
pattern = re.compile(r'(?=[A-Z])')
output = pattern.split(text)
print(output)


# In[40]:


def insert_spaces(text):
    return re.sub(r'(\d)([A-Za-z])', r'\1 \2', text)
text = "RegularExpression1IsAn2ImportantTopic3InPython"
output = insert_spaces(text)
print(output)


# In[41]:


def insert_spaces(text):
    return re.sub(r'([A-Z]|\d)([a-z])', r'\1 \2', text)
text = "RegularExpression1IsAn2ImportantTopic3InPython"
output = insert_spaces(text)
print(output)


# In[ ]:





# In[42]:


import pandas as pd

url = "https://raw.githubusercontent.com/dsrscientist/DSData/master/happiness_score_dataset.csv"
df = pd.read_csv(url)

df['first_six_letters'] = df['Country'].apply(lambda x: x[:6])

print(df.head())


# In[43]:


def match_string(s):
    pattern = r'^[a-zA-Z0-9_]+$'
    if re.match(pattern, s):
        return True
    else:
        return False
strings = [
    "Hello_World",
    "hello123",
    "ABC_DEF",
    "abcdef",
    "123abc",
    "_hello_",
    "hello world", 
    "hello!",  
    "hello@world",  
]
for s in strings:
    if match_string(s):
        print(f"'{s}' matches the pattern")
    else:
        print(f"'{s}' does not match the pattern")


# In[44]:


def starts_with_number(s, num):
    if s.startswith(str(num)):
        return True
    else:
        return False
    strings = [
    "123abc",
    "123def",
    "234abc",
    "234def",
]

num = 123

for s in strings:
    if starts_with_number(s, num):
        print(f"'{s}' starts with {num}")
    else:
        print(f"'{s}' does not start with {num}")


# In[45]:


def remove_leading_zeros(ip_address):
    octets = ip_address.split(".")
    new_octets = [str(int(octet)) for octet in octets]
    new_ip_address = ".".join(new_octets)
    return new_ip_address
ip_addresses = [
    "010.012.013.014",
    "192.168.001.001",
    "255.255.012.034",
]
for ip_address in ip_addresses:
    print(f"Original IP address: {ip_address}")
    print(f"IP address without leading zeros: {remove_leading_zeros(ip_address)}")
    print()


# In[ ]:





# In[2]:


def search_literals(text, literals):
    for literal in literals:
        if literal in text:
            print(f"Found '{literal}' in the text.")
        else:
            print(f"'{literal}' not found in the text.")
text = 'The quick brown fox jumps over the lazy dog.'


literals = ['fox', 'dog', 'horse']

search_literals(text, literals)


# In[3]:


def search_literal_with_location(text, literal):
    index = text.lower().find(literal.lower())
    if index != -1:
        return f"Found '{literal}' at position {index} in the text."
    else:
        return f"'{literal}' not found in the text."


text = 'The quick brown fox jumps over the lazy dog.'
literal = 'fox'

print(search_literal_with_location(text, literal))


# In[4]:


def find_substrings(text, pattern):
    indices = [i for i in range(len(text)) if text.startswith(pattern, i)]
    return [(i, i + len(pattern)) for i in indices]


text = 'Python exercises, PHP exercises, C# exercises'


pattern = 'exercises'
for start, end in find_substrings(text, pattern):
    print(f"Found '{pattern}' at indices [{start}:{end}]")


# In[6]:


text = 'Python exercises, PHP exercises,C# exercises'
pattern = 'exercises'
for match in re.finditer(pattern, text):
    start = match.start()
    end = match.end()
    print(f'Found "{pattern}" at {start} with length {end - start}')


# In[7]:


date = '2022-03-01'
year, month, day = date.split('-')
converted_date = '-'.join([day, month, year])
print(converted_date)


# In[10]:


def find_decimals(text):
    pattern = re.compile(r'\b\d{1,2}(\.\d{1,2})?\b')
    matches = pattern.findall(text)
    return matches

text = '01.12 0132.123 2.31875 145.8 3.01 27.25 0.25'
print(find_decimals(text))


# In[13]:


text = "the sun set bhind the hill and i saw beautiful nature and there are 10 hill,20 deep trench."

for match in re.finditer(r'\d+', text):
    print(match.group(0))
    print("Index position:", match.start())


# In[14]:


text = 'My marks in each semester are: 947, 896, 926, 524, 734, 950, 642'

numbers = re.findall(r'\d+', text)
numbers = [int(num) for num in numbers]
max_num = max(numbers)

print(max_num)



# In[15]:


def insert_spaces(text):
    words = re.findall(r'[A-Z][a-z]*|[^A-Z]*', text)
    return ' '.join(words)

text = 'RegularExpressionIsAnImportantTopicInPython'
result = insert_spaces(text)
print(result)


# In[17]:


def find_sequences(text):
    pattern = r'[A-Z][a-z]+'
    matches = re.findall(pattern, text)
    return matches

text = "RegularExpressionIsAnImportantTopicInPython"
sequences = find_sequences(text)
print(sequences)


# In[18]:


def remove_duplicates(sentence):
    return re.sub(r'\b(\w+)\s+\1\b', r'\1', sentence)

sentence = "Hello hello world world"
result = remove_duplicates(sentence)
print(result)


# In[19]:


def accept_alphanumeric(string):
    pattern = r'[a-zA-Z0-9]*[a-zA-Z0-9]$'
    if re.search(pattern, string):
        return True
    else:
        return False

string1 = "Hello123"
string2 = "Hello123!"
if accept_alphanumeric(string1):
    print(string1, "ends with an alphanumeric character.")
else:
    print(string1, "does not end with an alphanumeric character.")

if accept_alphanumeric(string2):
    print(string2, "ends with an alphanumeric character.")
else:
    print(string2, "does not end with an alphanumeric character.")


# In[20]:


def extract_hashtags(text):
    pattern = r'#\w+'
    hashtags = re.findall(pattern, text)
    return hashtags

text = "RT @kapil_kausik: #Doltiwal I mean #xyzabc is \"hurt\" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> \"acquired funds\" No wo"
hashtags = extract_hashtags(text)
print(hashtags)


# In[38]:


import re

def extract_dates(file_name):
    with open(file_name, 'r') as file:
        text = file.read()
        pattern = r'\d{1,2}-\d{1,2}-\d{4}'
        matches = re.findall(pattern, text)
        return matches

file_name = "sample.txt"
dates = extract_dates(file_name)
print(dates)


# In[28]:


def remove_words_of_length_between_2_and_4(text):
    pattern = re.compile(r'\b\w{2,4}\b')
    text = pattern.sub('', text)
    return text

text = "&quot;The following example creates an ArrayList with a capacity of 50 elements. 4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly.&quot;"
text = remove_words_of_length_between_2_and_4(text)
print(text)


# In[ ]:





# In[ ]:




