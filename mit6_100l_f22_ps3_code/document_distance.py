# 6.100A Fall 2022
# Problem Set 3
# Written by: sylvant, muneezap, charz, anabell, nhung, wang19k, asinelni, shahul, jcsands

# Problem Set 3
# Name:
# Collaborators:

# Purpose: Check for similarity between two texts by comparing different kinds of word statistics.

import string
import math


### DO NOT MODIFY THIS FUNCTION
def load_file(filename):
    """
    Args:
        filename: string, name of file to read
    Returns:
        string, contains file contents
    """
    # print("Loading file %s" % filename)
    inFile = open(filename, 'r')
    line = inFile.read().strip()
    for char in string.punctuation:
        line = line.replace(char, "")
    inFile.close()
    return line.lower()


### Problem 0: Prep Data ###
def text_to_list(input_text):
    """
    Args:
        input_text: string representation of text from file.
                    assume the string is made of lowercase characters
    Returns:
        list representation of input_text, where each word is a different element in the list
    """
    output_list =[]
    output_list = input_text.split()

    return output_list


### Problem 1: Get Frequency ###
def get_frequencies(input_iterable):
    """
    Args:
        input_iterable: a string or a list of strings, all are made of lowercase characters
    Returns:
        dictionary that maps string:int where each string
        is a letter or word in input_iterable and the corresponding int
        is the frequency of the letter or word in input_iterable
    Note: 
        You can assume that the only kinds of white space in the text documents we provide will be new lines or space(s) between words (i.e. there are no tabs)
    """

    if type(input_iterable) == str:
        input_iterable=list(input_iterable)
    
    if type(input_iterable) == list:    
        input_iterable.sort()
        
        count={}
        for item in input_iterable:
            count[item] =input_iterable.count(item)
    else:
        return 0
        
    return count


### Problem 2: Letter Frequencies ###
def get_letter_frequencies(word):
    """
    Args:
        word: word as a string
    Returns:
        dictionary that maps string:int where each string
        is a letter in word and the corresponding int
        is the frequency of the letter in word
    """
    
    if type(word) == str:
        word=list(word)
        count=get_frequencies(word)
    else:
        return 0
    
    return count



### Problem 3: Similarity ###
def calculate_similarity_score(freq_dict1, freq_dict2):
    """
    The keys of dict1 and dict2 are all lowercase,
    you will NOT need to worry about case sensitivity.

    Args:
        freq_dict1: frequency dictionary of letters of word1 or words of text1
        freq_dict2: frequency dictionary of letters of word2 or words of text2
    Returns:
        float, a number between 0 and 1, inclusive
        representing how similar the words/texts are to each other

        The difference in words/text frequencies = DIFF sums words
        from these three scenarios:
        * If an element occurs in dict1 and dict2 then
          get the difference in frequencies
        * If an element occurs only in dict1 then take the
          frequency from dict1
        * If an element occurs only in dict2 then take the
          frequency from dict2
         The total frequencies = ALL is calculated by summing
         all frequencies in both dict1 and dict2.
        Return 1-(DIFF/ALL) rounded to 2 decimal places
    """

    # string2="electrons paired with neutrons is evidence that the so name god lives with you"
    # string1="rehearse the feeling paired with the evidence that will make you good"


    # dict1 = get_frequencies(string1.split())
    # dict2 = get_frequencies(string2.split())
    dict1 = freq_dict1
    dict2 = freq_dict2

    key_1 = sorted(list(dict1.keys()))
    
    key_2 = sorted(list(dict2.keys()))
    unique = key_1
    
    for key in key_2:
        if key not in key_1:
            unique.append(key)

    count_L1 =0
    count_L2 =0
    
    delta={}
    sigma={}

    for uniq in unique:
                if uniq not in dict1:     
                    count_L1 =0
                else:
                    count_L1 =dict1[uniq]
                    
                
                if uniq not in dict2:
                    count_L2 =0
                else:
                    count_L2 =dict2[uniq]
                    
                delta[uniq] = abs(count_L1 - count_L2)
                sigma[uniq] = count_L1 + count_L2
                
    
    delta_total=0
    sigma_total=0
    
    for u in delta.values():
        delta_total +=u
    for u in sigma.values():
        sigma_total +=u
    
    
    similarity= 1 -(delta_total/sigma_total)

    return similarity

### Problem 4: Most Frequent Word(s) ###
def get_most_frequent_words(freq_dict1, freq_dict2):
    """
    The keys of dict1 and dict2 are all lowercase,
    you will NOT need to worry about case sensitivity.

    Args:
        freq_dict1: frequency dictionary for one text
        freq_dict2: frequency dictionary for another text
    Returns:
        list of the most frequent word(s) in the input dictionaries

    The most frequent word:
        * is based on the combined word frequencies across both dictionaries.
          If a word occurs in both dictionaries, consider the sum the
          freqencies as the combined word frequency.
        * need not be in both dictionaries, i.e it can be exclusively in
          dict1, dict2, or shared by dict1 and dict2.
    If multiple words are tied (i.e. share the same highest frequency),
    return an alphabetically ordered list of all these words.
    """
    
    most_frequent_words=[]
    
    current_max1 = ["",0]
    current_max2 = ["",0]
    
    
    for key in freq_dict1:
        if freq_dict1[key] > current_max1[1]:
            current_max1[0]=key #freq_dict1[key] 
            current_max1[1]=freq_dict1[key] 

    for key in freq_dict2:
        if freq_dict2[key] > current_max2[1]:
            current_max2[0]=key #freq_dict1[key] 
            current_max2[1]=freq_dict2[key]


        most_frequent_words=[current_max1[0],current_max2[0]]
        
        
    print(current_max1[1],current_max2[1])
    
    return most_frequent_words



### Problem 5: Finding TF-IDF ###
def get_tf(file_path):
    """
    Args:
        file_path: name of file in the form of a string
    Returns:
        a dictionary mapping each word to its TF

    * TF is calculatd as TF(i) = (number times word *i* appears
        in the document) / (total number of words in the document)
    * Think about how we can use get_frequencies from earlier
    """
    text = text_to_list(load_file(file_path))

    words_freq = get_frequencies(text)

    TF =[]
    TF1 =words_freq
    number_of_words=sum(words_freq.values())
    # for item in words_freq:
    #     number_of_words += words_freq[item]

    # for item in words_freq:
    #     TF.append(words_freq[item]/number_of_words)
    #     #print("item ",  item, "words_freq[item]  ",words_freq[item])

    for item in TF1:
        TF1[item]=words_freq[item]/number_of_words
        

    return TF1


def get_idf(file_paths):
    """
    Args:
        file_paths: list of names of files, where each file name is a string
    Returns:
       a dictionary mapping each word to its IDF

    * IDF is calculated as IDF(i) = log_10(total number of documents / number of
    documents with word *i* in it), where log_10 is log base 10 and can be called
    with math.log10()

    """
    files      =[]
    file_list  =[]
    words_freq =[]

    for file in file_paths:
        files.append(load_file(file))

    for file in files:
        file_list.append(text_to_list(file))


    for file in file_list:
        words_freq.append(get_frequencies(file))

    all_words=[]

    for dicts in range(len(words_freq)):
        all_words +=list(words_freq[dicts].keys())

    all_words=sorted(all_words)

    unique = all_words
    count  = []
    for word in all_words:
        if all_words.count(word) > 1:
            unique.remove(word)
            
    for i in range(len(unique)):
        count.append(0)
        
    unique_dict = dict(zip(unique,count))

    numbr_of_files=len(files)

    documents_with_word ={}
    word_count=[]
    words={}
    
    
    

    for dict_index in range(len(words_freq)):
        for word in unique_dict.keys():
            if word in  words_freq[dict_index].keys():
                unique_dict[word] += 1
    
    
    idf = unique_dict
    for w in unique_dict:
        idf[w] = math.log10(numbr_of_files/unique_dict[w])


    return  idf

def get_tfidf(tf_file_path, idf_file_paths):
    """
        Args:
            tf_file_path: name of file in the form of a string (used to calculate TF)
            idf_file_paths: list of names of files, where each file name is a string
            (used to calculate IDF)
        Returns:
           a sorted list of tuples (in increasing TF-IDF score), where each tuple is
           of the form (word, TF-IDF). In case of words with the same TF-IDF, the
           words should be sorted in increasing alphabetical order.
        * TF-IDF(i) = TF(i) * IDF(i)
        """
    TF_IDF=[]
    TF  =get_tf(tf_file_path)
    IDF =get_idf(idf_file_paths)
    IFW=[]
    
    for TFW in TF:
        IDFW=IDF[TFW]
        TF_IDF.append((TFW,TF[TFW]*IDFW))
        
    
    return TF_IDF

