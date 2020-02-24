#!/usr/bin/env python
# coding: utf-8

# In[ ]:


my_word_list = ['apple', 'orange', 'banana']
my_new_word_list = list(map(lambda x: '_' + x, my_word_list))
print(my_new_word_list)


# In[ ]:


my_state_list = ['CA','OR','NY','OR']
my_new_state_list = list(filter(lambda x: x in ['CA', 'NY'],my_state_list))
print(my_new_state_list)


# In[ ]:


my_number_list = [1,2,3,4,5]
my_new_number_list = [x * 3 for x in my_number_list]
print(my_new_number_list)


# In[ ]:


list_of_words = ['love', 'the', 'outdoors', 'with', 'passion']
wordsToRemove = ['the','with','of','a']
new_words_list = [x for x in list_of_words if x not in wordsToRemove]
print(new_words_list)

