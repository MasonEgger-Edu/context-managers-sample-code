class MyContextManager:
    def __enter__(self):
        return "Here"

    def __exit__(self, exc_type, exc_value, traceback):
        pass