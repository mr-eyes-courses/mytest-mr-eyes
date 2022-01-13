from mimetypes import init


class Excercise:
    def __init__(self) -> None:
        self.message = ""
        
    def hello(self):
        print(self.message)