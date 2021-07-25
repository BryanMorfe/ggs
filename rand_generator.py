import random

class RandIntGenerator(object):
    def __init__(self):
        super().__init__()

    def generate(min=0, max=99):
        return random.randint(min, max)
