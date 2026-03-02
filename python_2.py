"""// ??"""

"""Input para receber valores do usuário em variáveis"""
def saudacao(name):
    prompt = "If you tell us who you are, we can personalize the messages you see."
    prompt += "\nWhat is youre name?"
    name = input(prompt)
    print("Hello " + name + ":D")

"""Condicionais e Repetição"""
def cond(number):
    if number % 2 == 0:
        print('par')
    else:
        print('impar')

def repetir(current_number):
    while current_number <= 5:
        print(current_number)
        current_number += 1

def mult():
    current_number = 0
    while current_number < 100:
        current_number += 1
        if current_number % 17 == 0:
            continue
        print(current_number)
def mountain():
    polling_active = True
    while polling_active:
        name = input("What's your name?")
        response = input("Which mountain would you like to clinb someday?")

        responses[name] = response

        resp = input('Do you want to continue (yes or no)')



"""
Códigos do beecrowd

A = float(input())
B = float(input())
C = float(input())

result=(A*2+B*3+C*5)/10

print("MEDIA = %.1f" % result)
===============================================
N = float(input())

cem = N/100
N = N%100
cinq = N/50
N = N%50
vinte = N/20
N = N%20
dez = N%10
N = N%10
cinco = N/5
N = N%5
dois = N/2
N = N%2

um = N
cinquentaCent = N/0.50
N = N%0.50
vinteCincoCent = N/0.25
N = N%0.25
dezCent = N/0.10
N = N%0.10
cincoCent = N/0.05
N = N%0.05
umCent = N/0.01

print('NOTAS\n ' + cem + 'nota(s) de R$ 100')"""

def notas(N):
    N = float(N)

    cem = N//100
    N = N%100
    cinq = N//50
    N = N%50
    vinte = N//20
    N = N%20
    dez = N//10
    N = N%10
    cinco = N//5
    N = N%5
    dois = N//2
    N = N%2

    um = N
    cinquentaCent = N//0.50
    N = N%0.50
    vinteCincoCent = N//0.25
    N = N%0.25
    dezCent = N//0.10
    N = N%0.10
    cincoCent = N//0.05
    N = N%0.05
    umCent = N//0.01

    print(f"""
        NOTAS:
        {int(cem)} nota(s) de R$ 100.00
        {int(cinq)} nota(s) de R$ 50.00
        {int(vinte)} nota(s) de R$ 20.00
        {int(dez)} nota(s) de R$ 10.00
        {int(cinco)} nota(s) de R$ 5.00
        {int(dois)} nota(s) de R$ 2.00
        MOEDAS:
        {int(um)} moeda(s) de R$ 1.00
        {int(cinquentaCent)} moeda(s) de R$ 0.50
        {int(vinteCincoCent)} moeda(s) de R$ 0.25
        {int(dezCent)} moeda(s) de R$ 0.10
        {int(cincoCent)} moeda(s) de R$ 0.05
        {int(umCent)} moeda(s) de R$ 0.01
        """)

def main ():
    notas(553.75)

if __name__ == "__main__":
    main()