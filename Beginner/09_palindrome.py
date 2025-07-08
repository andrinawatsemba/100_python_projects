# Palindrome Checker
# This is part of my 100 Python Projects challenge.

def is_palindrome(word):
    return word == word[::-1]

word = input("Enter a word to check if it's a palindrome: ").lower()

if is_palindrome(word):
    print(f"✅ '{word}' is a palindrome!")
else:
    print(f"❌ '{word}' is not a palindrome.")
