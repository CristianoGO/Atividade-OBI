def pisoEscola(l, c):
    if l <= 1 and c <= 100:
        ji.append(str(l*c)*((c-1)*(l-1)))
        jp.append(str((c-1)*2)+((l-1)*2))
        print(ji)
        print(jp)

pisoEscola(int(input()))

