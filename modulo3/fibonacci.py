
def fib(n):
    a, b = 0, 1
    while n > 0:
        n -= 1
        a, b = b, a+b  # Recursión de la serie de fibonacci
        print(a, end=' ')


print(fib(35))


def es_primo(numero):
    resultado = True
    for divisor in range(2, numero):
        if(numero % divisor) == 0:
            resultado = False
            break
    return resultado


print(es_primo(13))
