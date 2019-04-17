from threading import Thread


class RunDemo(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name
    def run(self):
        pass



if __name__ == "__main__":
    pass