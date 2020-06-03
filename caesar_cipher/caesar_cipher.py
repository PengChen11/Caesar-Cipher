import string
import pysnooper
import re
import nltk
nltk.download('words')
from nltk.corpus import words
english_word_list = words.words()

def encrypt(text,shift):
    """Function to encrypt the text string. It is case sensitive"""
    encrypted_text = ''
    alphabet = string.ascii_uppercase+string.ascii_lowercase
    
    for char in text:
        if alphabet.find(char) == -1:#handles non alphabetic characters
            shifted_char = char
        else:
            shifted_index = (alphabet.find(char) + shift)%52
            shifted_char = alphabet[shifted_index]
        encrypted_text += shifted_char
    
    return encrypted_text

def decrypt(text,shift):
    """function to decrypt the text string. It is case sensitive"""
    decrypted_text = ''
    alphabet = string.ascii_uppercase+string.ascii_lowercase

    for char in text:
        if alphabet.find(char) == -1:#handle non alphabetic characters
            shifted_char = char
        else:
            shifted_index = (alphabet.find(char) - shift)%52
            shifted_char = alphabet[shifted_index]
        decrypted_text += shifted_char
    
    return decrypted_text

def crack(text):
    """function to crack the encrypted text string. It is case sensitive"""
    for i in range(52):
        shifted_text = decrypt(text,i)
        pure_shifted_text = re.sub('[^a-zA-Z]+', ' ', shifted_text)#use regex to replace all non alphabetic characters with a space
        word_list = [word for word in pure_shifted_text.split()]

        crack_checker = 0
        for word in word_list:
            if word in english_word_list:
                crack_checker += 1

        if crack_checker / len(word_list) >= 0.8:#if over 80% of the words in decrypted string is english words, consider it as a success. 
            return shifted_text
    


if __name__ == "__main__":
    shift_key = 31
    test = encrypt('It was the best of times, it was the worst of times.',shift_key)
    print(test)

    reverse = decrypt(test,shift_key)
    print(reverse)

    crack_test = crack(test)
    print(crack_test)