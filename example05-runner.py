from example05 import YellingText

with YellingText() as cm:
    print("Hello")
    raise Exception

print("I should not be yelling.")