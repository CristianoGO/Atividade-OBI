def  albumCopa(n, c, m, x, y):
    album = [100]
    carimbada = [100]
    res = 0
    i = 1
    j = 0

    for i in n:
        carimbada[i] = album[i] = 0
    
    for j in c:
        x = input()
        carimbada[x] = 1

    for j in m:
        y = input()
        carimbada[y] = 1

    for i in n:
        if album[i] == 0 and carimbada[i] == 1
        res = res + 1

    print(res)

albumCopa(int(input()))
    