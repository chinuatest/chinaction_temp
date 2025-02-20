from greet_script import greet

def test_greet():
    assert greet("World") == "Hello, World!"
    assert greet("GitHub") == "Hello, GitHub!"
    assert greet("") == "Hello, !"

if __name__ == "__main__":
    import pytest
    pytest.main()
