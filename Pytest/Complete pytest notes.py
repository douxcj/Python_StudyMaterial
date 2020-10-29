import pytest

# Basic unit testings

def add(x, y):
    return x + y

def test_add1():
    assert 2 == add(1,1)

def test_add2():
    assert 1 != add(1,1)

# pytest -vv test_examples.py
# pytest --durations=0 -vv test_examples.py

 

# Raise Error

def func(x):
    if x == 0:
        raise ValueError("value error!")
    else:
        pass

def test_error1():  # check if raise error
    with pytest.raises(ValueError):
        func(0)

def test_error2():
    assert func(1) == None  #pass, not pass if 0

 

# Test same function but use different parameters
# Same add function as above

@pytest.mark.parametrize(
    "x, y, expected",
    [
        (1,1,2),
        (2,2,4),
        (10,10,20),
    ]
)

def test_add3(x, y, expected):
    assert add(x,y) == expected

 

# Classification testings
# pytest --markers
# pytest.ini  add markers g1 and g2

@pytest.mark.g1
def test_func1():
    pass

@pytest.mark.g2
def test_func2():
    pass

# pytest -vv -m g1

 

# Fixtures
@pytest.fixture
def numbers():
    a = 10
    b = 20
    c = 30
    return [a,b,c]


def test_fixture1(numbers):
    x = 10
    assert numbers[0] ==x

def test_fixture2(numbers):
    y = 20
    assert numbers[1] ==y

def test_fixture3(numbers):
    z = 30
    assert numbers[2] ==z