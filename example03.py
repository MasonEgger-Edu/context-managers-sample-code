class YellingText:
    def __enter__(self):
        import sys

        self.stdout = sys.stdout.write
        sys.stdout.write = self.yell
        return "YELLING"

    def yell(self, text):
        self.stdout(text.upper())

    def __exit__(self, exc_type, exc_value, traceback):
        pass