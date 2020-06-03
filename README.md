# Lab: Cryptography
[click here to see the code](caesar_cipher/caesar_cipher.py)

[click here to see the tester code](tests/test_caesar_cipher.py)
## Overview
Today we’ll be tackling a crytographic classic - the Caesar Cipher.

Your job will be to devise a method to encrypt a message that can then be decrypted when supplied with the corresponding key.

But don’t stop there! You’ll also need to devise a way to decipher the encrypted message event when you do NOT have the key!

## Feature Tasks and Requirements
- Create an **encrypt** function that takes in a plain text phrase and a numeric shift.
    - the phrase will then be **shifted** that many letters.
E.g. encrypt(‘abc’,1) would return ‘bcd’ = E.g. ecrypt(‘acb’, 10) would return ‘klm’
    - shifts that exceed 26 should wrap around
E.g. encrypt(‘abc’,27) would return ‘bcd’
- Create a **decrypt** method that takes in encrypted text and numeric shift which will restore the encrypted text back to its original form **as long as correct key is supplied**.
- Break the ciphter so that an encrypted message can be transformed into its original state **WITHOUT** access to the key.
- Devise a method for the computer to determine if code was broken with minimal human guidance.

## Implementation Notes

- In order to accomplish this task you’ll need access to a **corpus** of English words.
- A search on something like **python list of english words** should get you going.

## User Acceptance Tests

The application must…

- encrypt a string with a given shift
- decrypt a previously encrypted string with the same shift
- encryption should handle upper and lower case letters
- encryption should allow non-alpha characters but ignore them, including white space
- decrypt encrypted version of ```It was the best of times, it was the worst of times.``` **WITHOUT** knowing the shift used.