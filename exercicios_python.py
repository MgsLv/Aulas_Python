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

def 
def main():
    listaOrganizada()
    
if __name__ == "__main__":
    main()
