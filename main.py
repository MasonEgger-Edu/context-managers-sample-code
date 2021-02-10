class LeetText:
    def __enter__(self):
        import sys

        self.stdout = sys.stdout.write
        sys.stdout.write = self.yell
        return "L33T"

    def leet_write(self, text):
        leet_text = (
            text.replace("e", "3").replace("E", "3").replace("o", "0").replace("o", "0")
        )
        self.stdout(leet_text)

    def yell(self, text):
        self.stdout(text.upper())

    def __exit__(self, exc_type, exc_value, traceback):
        import sys

        sys.stdout.write = self.stdout