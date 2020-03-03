from figuraCopa import albumCopa

def teste_albumCopa():
    assert albumCopa(10, 2, 5) == 1
    assert albumCopa(4, 7) == 1
    assert albumCopa(7, 1, 2, 8, 3) == 1

def teste_albumCopa2():
    assert albumCopa(10, 2, 6) == 0
    assert albumCopa(4, 7) == 0
    assert albumCopa(7, 1, 8, 9, 3) == 0

def teste_albumCopa3():
    assert albumCopa(8, 4, 10) == 4
    assert albumCopa(2, 4, 6, 8) == 4
    assert albumCopa(3, 1, 1, 5, 3, 1, 7, 7, 1, 1) == 4