from example03 import YellingText

with YellingText() as cm:
    print("Hello")

print("I should not be yelling.")