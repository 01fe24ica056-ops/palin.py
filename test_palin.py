def is_palindrome(text):
    return text == text[::-1]

def test_palindrome():
    assert is_palindrome("madam") is True