from math import ceil, floor
"""ceil = arredonda para cima"""
"""floor = arredonda para cima, ex: 7.3 = 7"""

from fractions import Fraction
"""Contas com frações (IMMC)"""

from numpy import polyadd, polysub, polymul

def matematica():
    mais = 1 + 2
    menos = 7 - 3
    multiplicacao = 4*3
    divisao = 12 / 3
    potencia = 3**2
    raizQuadrada = 3**(1.0/2)

    print("1 + 2 = ", mais, "\n" \
    "7 - 3 = ", menos, "\n"
    "4 x 3 = ", multiplicacao, "\n"
    "12 / 3 = ", divisao, "\n"
    "3² ", potencia, "\n"
    "√3 = ", raizQuadrada)

def potencia():
    a = 2 
    b = 6

    a_quadrado = pow(a, 2)
    a_cubo = pow(a, 3)
    a_quarta = pow(a, 4)
    a_elevado_b = pow(a, b)

    print(u'Resultado das operações:\n' \
    'a = ', a, 
    '\nb = ', b,
    '\na ao quadrado = ', a_quadrado,
    '\na ao cubo = ', a_cubo,
    '\na à quarta = ', a_quarta, 
    '\na elevado a b = ', a_elevado_b)

def arredondando():
    """Arredondando"""
    print('\n' * 100)

    a = 3.456
    b = 7.8903

    piso_a = floor(a)
    teto_a = ceil(a)

    piso_b = floor(b)
    teto_b = ceil(b)

    print("Arredondando a para baixo: ", teto_a, 
          "\nArredondando a para cima: ", piso_a,
          "\nArredondando b para baixo: ", piso_b,
          "\nArredondando b para cima: ", teto_b)
    
    """Arredonda para o número inteiro mais próximo"""
    arredondandoA = round(a)
    arredondandoB = round(b)

    print("Arredondando a para o inteiro mais próximo: ", arredondandoA,
          "\nArredondando b para o inteiro mais próximo: ", arredondandoB)

def divisao():
    """Divisão"""
    divisaoInteiro = 7 // 3 # Parte inteira da divisão
    divisaoResto = 7 % 3 # Resto da divisão

    
    print("Divisão inteira: ", divisaoInteiro,
          "\nResto de Divisão : ", divisaoResto)

def fracoes():
    """Conta de Frações (MMC)"""
    a = Fraction(7, 31) # O mesmo que a fração 7/31
    b = Fraction(4, 15) # O mesmo que a fração 4/15

    soma = a + b
    subtracao = a - b
    multiplicacao = a * b
    divisao = a / b

    print('Operação de frações: ' \
    '\nFração 1 (a) = ', a,
    '\nFração 2 (b) = ', b,
    '\na + b = ', soma,
    '\na - b = ', subtracao,
    '\na x b = ', multiplicacao,
    '\na / b = ', divisao)

def polinomios():
    print('\n' * 100)

    coeficientes_pol1 = [3, 2, -1]
    coeficientes_pol2 = [4, -1, 3]

    resultado = polyadd(coeficientes_pol1, coeficientes_pol2)

    print('Coeficientes do resultado da suma entre: ' \
    '\n3x**2 + 2x - 1; e ' \
    '\n4x**2 - x + 3: ', 
    resultado)

    coeficientes_pol1 = [3, -2, 1]
    coeficientes_pol2 = [-2, 0, 4]

    resultado = polysub(coeficientes_pol1, coeficientes_pol2)

    print(u'\nCoeficientes do resultado da subtração entre: ' \
    '\n3x**2 - 2x + 1; e' \
    '\n2x**2 + 4: ',
    resultado)

    coeficientes_pol1 = [2, 4, 0.5]
    coeficientes_pol2 = [3, 2, 0]

    resultado1 = polymul(coeficientes_pol1, 2)
    resultado2 = polymul(coeficientes_pol2)

    print(u'Coeficientes do resultado da multiplicação de: ' \
    '\n2X**2 + 4x + 1 por 2: ', resultado1)

    print(u'\nCoeficientes do resultado da multiplicação de: ' \
    '\n2x**2 + 4x + 1/2')

    

def main():
    polinomios()

if __name__ == "__main__":
    main()
