from example07 import whisper

with whisper() as w:
    print("THIS SHOULD BE WHISPERED")

print("THIS IS NOT WHISPERED")