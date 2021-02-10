from example06 import FileOpen

with FileOpen("file.txt", "r") as fh:
    text = fh.read()

print(text)