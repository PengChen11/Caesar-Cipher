from caesar_cipher.caesar_cipher import *

def test_encyption():
    shift_key = 31
    test = encrypt('It was the best of times, it was the worst of times.',shift_key)
    expected = 'nY bFX YMJ GJXY TK YNRJX, NY bFX YMJ bTWXY TK YNRJX.'
    assert test == expected


def test_decyption():
    shift_key = 31
    test = decrypt('nY bFX YMJ GJXY TK YNRJX, NY bFX YMJ bTWXY TK YNRJX.',shift_key)
    expected = 'It was the best of times, it was the worst of times.'
    assert test == expected


def test_crack_it():
    test = crack('nY bFX YMJ GJXY TK YNRJX, NY bFX YMJ bTWXY TK YNRJX.')
    expected = 'It was the best of times, it was the worst of times.'
    assert test == expected
