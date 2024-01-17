# This function returns you a list of all the prime numbers there are below any given number.
def primos(x):
    numeros = list(range(2, x+1))
    i = 0
    while numeros[i]**2 <= x:
        for n in numeros:
            if n != numeros[i]:
                if n % numeros[i] == 0:
                    numeros.remove(n)
        i += 1
    return numeros


print(primos(int(input("Ingrese un numero y te regresare una lista de primos por debajo de el: "))))
