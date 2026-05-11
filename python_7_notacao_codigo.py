import time

def loopForSoma(valor):
    inicio = time.time()
    soma = 0
    for i in range(valor + 1):
        soma += i
    print(soma)
    fim = time.time()
    print(f"Tempo gasto: {fim - inicio} segundos")

def formula(valor):
    inicio = time.time()
    soma = (valor * (valor + 1)) // 2
    print(soma)
    fim = time.time()
    print(f"Tempo gasto: {fim - inicio} segundos")

def main ():
    formula(1000000000)

if __name__ == "__main__":
    main()