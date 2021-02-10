from example02 import MyContextManager

with MyContextManager() as cm:
    print("Hello")

print(cm)