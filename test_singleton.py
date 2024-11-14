import pytest
from singleton import singleton

@singleton
class SingletonClass:
    def __init__(self, value):
        self.value = value

@singleton
class AnotherSingletonClass:
    def __init__(self, name):
        self.name = name
        

def test_singleton_same_instance():
    obj1 = SingletonClass(42)
    obj2 = SingletonClass(99)

    assert obj1 is obj2 
    assert obj1.value == 42  
    assert obj2.value == 42  


def test_singleton_different_classes():
    obj1 = SingletonClass(52)
    obj2 = AnotherSingletonClass("Test")

    assert obj1 is not obj2  
    assert obj1.value == 42
    assert obj2.name == "Test"


if __name__ == "__main__":
    pytest.main()
