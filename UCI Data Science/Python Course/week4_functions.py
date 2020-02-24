#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def multiply_numbers(tuple_of_numbers):
    total = 1
    for i in tuple_of_numbers:
        total = i * total
    return(total)


# In[ ]:


def filter_list(string_list, string):
    filtered_string = []
    for i in string_list:
        if i != string:
            filtered_string.append(i)
    return(filtered_string)


# In[ ]:


def longest_word(list_of_words):
    for i in list_of_words:
        longestlength = 0
        longword = 0
        if len(i) > longestlength:
            longestlength = len(i)
            longword = i
    return(longword)


# In[ ]:


def list_to_unique(input_list):
    uniquelist = []
    for i in input_list:
        if i not in uniquelist:
                uniquelist.append(i)
    return(uniquelist)

