"""============================================================="""
"""Python intensivo 1-5"""
"""============================================================="""

def saudacao():
    print('Hello World!')

def nome():
    """Variável do tipo String"""
    primeiro_nome = "Miguel"
    sobre_nome = "Soares de Sousa"
    nome_completo = primeiro_nome + " " + sobre_nome
    
    """Concatenação de variáveis e texto simpples"""
    """O comando 'title' faz com que a primeira letra 
    de todas as palavras sejam sempre maiúscula"""
    mensagem = "Olá, " + nome_completo.title() + "!"
    print(mensagem)
    
    """Deixa todas as letras em maiúsculo"""
    print(nome_completo.upper())
    
    """Deixa todas as letras em minúsculo"""
    print(nome_completo.lower())

def quebraDeLinha():
    """O comando \n faz a quebra de linha de um texto, 
    enviando o texto após ele para a próxima linha, 
    enquanto que \t coloca o espaço de um 'tab' antes 
    do texto"""
    print("Linguagens:\n\tPython\n\tC\n\tJavaScript")
    
def semEspaco():
    frase = '   Posso te      ajudar?'
    
    """O comando 'rstrip' tira o espaço
    após o texto"""
    """print(frase.rstrip())"""
    
    """O comando 'lstrip' remove o espaço
    antes do texto"""
    """print(frase.lstrip())"""
    
    """O comando 'strip' remove todos os espaços,
    antes e depois do texto, porém não os do meio"""
    print(frase.strip())

def matematica():
    soma = 1+2
    subtracao = 5-3
    multiplicacao = 10*4
    divisao = 15/5
    potencia = 2**3
    prioridade = (2+3)*4
    arredondando = 3//2
    
    print(soma) 
    print(subtracao) 
    print(multiplicacao)
    print(divisao) 
    print(potencia)
    print(prioridade)
    print(arredondando)
    
def concatenacaoString():
    idade = 17
    mensagem = "Feliz " + str(idade) + "° Aniversávio!"
    
    print(mensagem)

def lista():
    carros = ['Fusca', 'Ford K', 'Palio', 'Uno', 'Logan']
    mensagem = "Meu primeiro carro foi um " + carros[0]. title() + "."
    
    print(mensagem)
    
    motos = ['Honda', 'Yamaha', 'Suzuki', 'Ducati']
    print('\nLista original:')
    print(motos)
    
    print('\nRemovendo um elemento da lista')
    mais_caro = 'Ducati'
    motos.remove(mais_caro)
    print(motos)
    print('\nA moto ' + mais_caro.title() + ' é cara demais para mim.')
    
    print('\nInserindo ao fim da lista')
    motos.append('Bmw')
    print(motos)
    
    print('\nInserindo em qualquer posição')
    motos.insert(1, 'Kawasaki')
    print(motos)
    
    print('\nRetirando do final da lista')
    popped = motos.pop()
    print(motos)

def listaOrganizada():
    carros = ['Bmw', 'Audi', 'Toyota', 'Subaru']
    
    print('Essa é a lista original:')
    print(carros)
    print('\nEssa é a lista em ordem alfabética:')
    print(sorted(carros))
    
    print('\nEssa é a lista na ordem alfabética ao contrário:')
    print(sorted(carros, reverse=True))
    
    print('\nEssa é a lista original de novo:')
    print(carros)
    
    print('\nO tamanho da lista (número de elementos) é de:')
    print(len(carros))

def usosListas():
    jogadores = ['João', 'Manuela', 'Alice', 'Daniel']
    for jogador in jogadores:
        print(jogador.title() + ', essa foi uma boa jogada!')
        print("Eu mal posso esperar para ver você jogar de novo, " + jogador.title() + ".\n")
        
    print('Obrigado, esse foi realmente um bom jogo!')

def listaNumeros():
    """Cria uma lista com todos os números, a partir de 1 e
    antes de 6"""
    numeros = list(range(1,6))
    print(numeros)
    
    """Cria uma lista com todos os números, a partir de 2, antes
    de 11 e com o espaçamento de 2 números entre cada um"""
    numeros_pares = list(range(2,11,2))
    print(numeros_pares)
    
    """Cria uma lista das raizes de todos os números
    (ex: raiz quadrada de 4 = 2, então 4 está no lugar
    de 2 na lista)"""
    raizes = []
    for valor in range(1,11):
        raiz = valor**2
        raizes.append(raiz)
        
    print(raizes)
    
    digitos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    """Imprime o menor número da lista"""
    print(min(digitos))
    
    """Imprime o maior número da lista"""
    print(max(digitos))
    
    """Imprime a soma de todos os números da lista"""
    print(sum(digitos))
    
def compreensaoLista():
    """Cria uma lista como se fosse com um for, mas de forma simplificada"""
    """Passa o valor de todas as raizes de todos os números,
    a partir de 1 e antes de 11, na variável 'raizes'"""
    raizes = [valor**2 for valor in range(1,11)]
    
    print(raizes)
    
def fatiandoListas():
    jogadores = ['Carlos', 'Maria', 'Miguel', 'Fernanda', 'Eliel']
    
    """Imprime os elementos entre 1 e 4"""
    print(jogadores[1:4])
    
    """Imprime os elementos entre o começo até 
    antes dos dois últimos"""
    print(jogadores[:-2])
    
    """Imprime todos os números entre o terceiro 
    até o final"""
    print(jogadores[-3:])
    
def copiandoListas():
    minhas_comidas = ['Pizza', 'Hamburger', 'Bolo de Cenoura']
    comidas_amigos = minhas_comidas[:]
    
    minhas_comidas.append('Bolo de Chocolate')
    comidas_amigos.append('Sorvete')
    
    print('Minhas comidas favoritas são:')
    print(minhas_comidas)
    
    print('\nAs comidas favoritas dos meus amigos são:')
    print(comidas_amigos)
    
def tuplas():
    """Tuplas são listas que não podem ser alteradas, muito 
    usadas para definir padrões, como constantes matemáticas 
    (pi = 3,14, etc)"""
    
    dimensoes = (200, 50)
    print('Dimensões originais:')
    for dimensao in dimensoes:
        print(dimensoes)
    
    dimensoes = (400, 100)
    print('\nDimensões modificadas:')
    for dimensao in dimensoes:
        print(dimensoes)
    """Se tentar alterar algum elemento de uma tupla, gera o erro:
    Traceback (most recent call last):
        File '<pyshell#14>', line 1, in <module>
            dimensoes[0]=250
        TypeError: 'tuple' object does not support item assignment"""
    """dimensoes[0]=250"""
    
def instrucoesIf():
    carros = ['audi', 'bmw', 'subaru', 'toyota']
    
    for carro in carros:
        if carro == 'bmw':
            print(carro.upper())
        else:
            print(carro.title())

def diferenca():
    carros = ['audi', 'bmw', 'subaru', 'toyota']
    
    for carro in carros:
        if carro != 'bmw':
            print(carro.upper())
        else:
            print(carro.title())
            
    resposta = 17
    
def operadoresRelacionaisLogicos():
    """idade = 18
    idade > 20 (false)
    idade >= 18 (true)
    idade < 15 (false)
    idade <= 18 (true)
    idade >= 15 and idade <= 21 (true)
    idade < 15 or idade 21 (false)"""
    
    """condimentos = ['Ketchup', 'Mostarda', 'Maionese']
    'Ketchup' in condimentos (true)
    'cebola' in condimentos (false)"""

def condicional():
    idade = 17
    if idade >= 18:
        print("Você é velho o bastante para votar!")
        print("Você já registrou o seu voto?")
    else:
        print("Desculpe, você é novo demais para votar.")
        print("Por favor, registre o seu voto em breve, quando for maior de 18!")

    idade = 12
    
    if idade < 4:
        preco = 2
    elif idade < 18:
        preco = 5
    elif idade < 65:
        preco = 10
    else:
        preco = 5
        
    print("O custo da sua admissão é de R$ " + str(preco) + ".")
    
    condimentosDisponiveis = ['Ketchup', 'Mostarda', 'Maionese',
                                'Shoyo', 'Pimenta', 'Alho']
    
    condimentosPedidos = ['Ketchup', 'Mostarda', 'Alho']
    
    for condimentoPedido in condimentosPedidos:
        if condimentoPedido in condimentosDisponiveis:
            print("Adicionando " + condimentoPedido + ".")
        else:
            print("Desculpe, nós não temos " + condimentoPedido + ".")
    
    print("\nFinalizando o seu pedido!")

def dicionario():
    carro = {'cor': 'verde', 'hp': 5}

    print(carro['cor'])

    """Adicionando novos pares chave-valor"""
    carro['preco'] = 19000
    carro['ano'] = 2012

    print(carro)

    """Modificando um dicionário"""
    if carro['ano'] >= 2010:
        desvalorizacao = -1000
    elif carro['ano'] >= 2000:
        desvalorizacao = -2000
    else:
        desvalorizacao = -4000

    carro['preco'] = carro['preco'] + desvalorizacao
    
    print("Novo valor do preco: " + str(carro['preco']))

    """Removendo pares chave-valor"""
    del carro['hp']
    print(carro)

    videogames_favoritos = {
        'Daniel': 'N64',
        'Sarah': 'PS Vita',
        'José': 'PS4',
        'Rebeca': 'XBOX One'
    }

    for nome, videogame in videogames_favoritos.items():
        print("O videogame favorito de " + nome.title(0) + " É: " + videogame.title() + ".")
    
def main():
    dicionario()

if __name__ == "__main__":
    main()
