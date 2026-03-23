def lerArquivo():
    filename = 'pi_digitos.txt'

    with open(filename) as file_objects:
        lines = file_objects.readlines() # Lê todas as linhas e as compila em uma lista com todas as linhas

    for line in lines:
        print(line.rstrip()) # remove todos os espaços das linhas à direita

    """
    Tipos de leitura:
        - r - Abrir
        - a - Adiciona novas informações ao arquivo (edita)
        - w - Criar um novo arquivo (se não existir)
    """

def lerArquivoGrande():

    filename = 'Treasure_islando.txt'
    try: 
        with open(filename, encoding='UTF-8') as f_obj:
            contents = f_obj.read()
    except FileExistsError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print("O arquivo " + filename + " tem por volta de " + str(num_words) + " palavras.")

def main():
    lerArquivoGrande()

if __name__ == "__main__":
    main()