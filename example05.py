class YellingText:
    def __enter__(self):
        import sys

        self.stdout = sys.stdout.write
        sys.stdout.write = self.yell
        return "Yelling"

    def yell(self, text):
        self.stdout(text.upper())

    def __exit__(self, exc_type, exc_value, traceback):
        import sys

        sys.stdout.write = self.stdout
        if exc_type is Exception:
            print("There was an exception")
            return True
