class SomeClass:
    def __init__(self):
        print('class')

    @classmethod
    def some_method(cls):
        print(type(cls).__name__)
        print(cls.__name__)


if __name__ == '__main__':
    someClass = SomeClass()
    SomeClass.some_method()
    someClass.some_method()