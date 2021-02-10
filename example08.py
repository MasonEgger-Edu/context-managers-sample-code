import contextlib


@contextlib.contextmanager
def whisper():
    import sys

    original_write = sys.stdout.write

    def whisper_write(text):
        original_write(text.lower())

    sys.stdout.write = whisper_write
    try:
        yield "whisper"
    except Exception:
        print("Exception happened")
    finally:
        sys.stdout.write = original_write