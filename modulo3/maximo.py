
def maximo_2(a,b):
    "Devuelve el máximo entre 2 numeros"
    maximo = a
    if b > a:
        maximo= b
    return maximo

def maximo_3(a ,b, c):
    return maximo_2(a, maximo_2(b, c))

print(maximo_2(2 , 5))
print(maximo_3(6, 2, 8))