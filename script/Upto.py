n = int(input("type a number: "))

"""Nota: Você pode usar a primeira ou a segunda função, elas fazem a mesma tarefa mas de diferentes formas.
Sendo que a segunda função foca na simplicidade e objectividade do código."""

"""def calc():
    total = 0
    l = 0
    while total != n:
        total +=1
        l = l+total

    print(l)    
calc()"""

def calc2():
    r = n * (n + 1) /2
    print(int(r))
calc2()
