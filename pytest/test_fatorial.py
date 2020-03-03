from fatorial import fatorial

def test_fa():
    assert fatorial(2) == 2

def test_fa2():
    assert fatorial(3) == 6

def test_fa3():
    assert fatorial(4) == 24

def test_fa4():
    assert fatorial(5) == 120

def test_fa5():
    assert fatorial(-1) == 1
