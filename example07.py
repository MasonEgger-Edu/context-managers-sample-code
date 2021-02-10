import contextlib


@contextlib.contextmanager
def whisper():
    import sys

    original_write = sys.stdout.write

    def whisper_write(text):
        original_write(text.lower())

    sys.stdout.write = whisper_write
    yield "whisper"
    sys.stdout.write = original_write