class FileOpen:
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode
        self.file_handle = None

    def __enter__(self):
        self.file_handle = open(self.name, self.mode)
        return self.file_handle

    def __exit__(self, exc_type, exc_value, traceback):
        self.file_handle.close()
