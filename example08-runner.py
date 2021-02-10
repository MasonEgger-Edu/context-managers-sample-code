from example08 import whisper

with whisper() as w:
    print("THIS SHOULD BE WHISPERED")
    raise Exception

print("THIS IS NOT WHISPERED")