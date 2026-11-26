# Problem Set 4C
# Name:
# Collaborators:

import json
import ps4b # Importing your work from Part B

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing
    the list of words to load

    Returns: a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    # inFile: file
    with open(file_name, 'r') as inFile:
        # wordlist: list of strings
        wordlist = []
        for line in inFile:
            wordlist.extend([word.lower() for word in line.split(' ')])
        return wordlist


def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.

    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"").lower()
    return word in word_list


def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story[:-1]


def get_story_pads():
    with open('pads.txt') as json_file:
        return json.load(json_file)


WORDLIST_FILENAME = 'words.txt'
### END HELPER CODE ###


def decrypt_message_try_pads(ciphertext, pads):
    '''
    Given a string ciphertext and a list of possible pads
    used to create it find the pad used to create the ciphertext

    We will consider the pad used to create it the pad which
    when used to decrypt ciphertext results in a plaintext
    with the most valid English words. In the event of ties return
    the last pad that results in the maximum number of valid English words.

    ciphertext (EncryptedMessage): The ciphertext
    pads (list of lists of ints): A list of pads which might have been used to encrypt the ciphertext

    Returns: (PlaintextMessage) A message with the decrypted ciphertext and the best pad
    '''

    plaintext_story     = []
    plaintext_story_tmp = ""
    decript             = ciphertext # cipher text is an EncryptedMessage object, use methods to access it's attributes XD 
    real_english_words  = []
    word_dict           = load_words(WORDLIST_FILENAME)
    
    best_pad =0
    best_pad_idx = 0
    word_count =0 
    for pad_n in pads: 
            plaintext_story_tmp=decript.decrypt_message(pad_n) # decript message returns a PlainTextMessage object 
            plaintext_story.append(plaintext_story_tmp.get_text())
            
            
            real_english_words.append(0)
            plaint_story_words=plaintext_story_tmp.get_text().split(" ")
            for word in plaint_story_words:
                real_english_words[word_count] += 1 if is_word(word_dict,word) else 0
            
            if real_english_words[word_count] > best_pad:
                best_pad = real_english_words[word_count]
                best_pad_idx = word_count
            elif real_english_words[word_count] == 0 and best_pad == 0:
                best_pad = real_english_words[word_count]
                best_pad_idx = word_count
            word_count += 1
            
            
    return ps4b.PlaintextMessage(plaintext_story[best_pad_idx], pads[best_pad_idx])
    
    
    # raise NotImplementedError  # delete this line and replace with your code here


def decode_story():
    '''
    Write your code here to decode Bob's story using a list of possible pads
    Hint: use the helper functions get_story_string and get_story_pads and your EncryptedMessage class.

    Returns: (string) the decoded story

    '''
    # raise NotImplementedError  # delete this line and re place with your code here



if __name__ == '__main__':
    # # Uncomment these lines to try running decode_story()
    
    story = get_story_string()
    story_pads = get_story_pads()
    encripted_story_obj = ps4b.EncryptedMessage(story)


    plain_text_obj = decrypt_message_try_pads(encripted_story_obj,story_pads)
    
    print(plain_text_obj.get_text())
    my_message = ps4b.Message("My Message!")
    # print(my_message.get_text())
    
    
    
    # story = decode_story()
    # print("Decoded story: ", story)
 