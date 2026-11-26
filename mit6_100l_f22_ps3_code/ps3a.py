# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 22:51:32 2026

@author: ioseth ibis pegueros lepe
"""
from document_distance import *

def main():
    print('ps3 document distance ')
     
    text = load_file("tests\student_tests\hello_world.txt") # text files will be found in the same directory as this file

    print(text)
    # print(type(text))
    test_directory ="tests\student_tests\\"  # text files will be found in the same directory as this file
    hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')

    world, friend             = text_to_list(hello_world), text_to_list(hello_friend)
    
    


    ## Tests Problem 0: Prep Data
    world, friend = text_to_list(hello_world), text_to_list(hello_friend)
    print(world)      # should print ['hello', 'world', 'hello']
    print(friend)     # should print ['hello', 'friends']

    ## Tests Problem 1: Get Frequencies
    world, friend = text_to_list(hello_world), text_to_list(hello_friend)
    world_word_freq = get_frequencies(world)
    friend_word_freq = get_frequencies(friend)
    print(world_word_freq)    # should print {'hello': 2, 'world': 1}
    print(friend_word_freq)   # should print {'hello': 1, 'friends': 1}    
    
    ## Tests Problem 2: Get Letter Frequencies
    freq1 = get_letter_frequencies('hello')
    freq2 = get_letter_frequencies('that')
    print(freq1)      #  should print {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    print(freq2)      #  should print {'t': 2, 'h': 1, 'a': 1}
    


    ## Tests Problem 3: Similarity
    friend_word_freq = get_frequencies(friend)
    word1_freq = get_letter_frequencies('toes')
    word2_freq = get_letter_frequencies('that')
    word3_freq = get_frequencies('nah')
    word_similarity1 = calculate_similarity_score(word1_freq, word1_freq)
    word_similarity2 = calculate_similarity_score(word1_freq, word2_freq)
    word_similarity3 = calculate_similarity_score(word1_freq, word3_freq)
    word_similarity4 = calculate_similarity_score(world_word_freq, friend_word_freq)
    print(word_similarity1)       # should print 1.0
    print(word_similarity2)       # should print 0.25
    print(word_similarity3)       # should print 0.0
    print(word_similarity4)       # should print 0.4


    ## Tests Problem 4: Most Frequent Word(s)
    freq_dict1, freq_dict2 = {"hello": 5, "world": 1}, {"hello": 1, "world": 5}
    most_frequent = get_most_frequent_words(freq_dict1, freq_dict2)
    print("main in document_distance",most_frequent)      # should print ["hello", "world"]


    ## Tests Problem 5: Find TF-IDF
    tf_text_file = test_directory + 'hello_world.txt'
    idf_text_files = [test_directory + 'hello_world.txt', test_directory + 'hello_friends.txt']
    tf = get_tf(tf_text_file)
    idf = get_idf(idf_text_files)

    tf_idf = get_tfidf(tf_text_file, idf_text_files)
    
    print("tf ", tf)
    print("idf", idf)
    print("tf_idf",tf_idf) 
    


if __name__ == '__main__':
    main()