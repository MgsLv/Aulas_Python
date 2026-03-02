a = 1           # int
b = 1.1         # float/double
c = "abcd"      # String
d = [1,2,3,4,5] # Vetor -- Lista
e = (1,2,3,4,5) # Tupla (não pode alterar)

cars = ["audi", "bmw", "subari", "volkswagen"]

# Condicionais

for car in cars:
    if car == 'bmw' or car =='subari':
        print(car.upper())
    else:
        print(car.lower())

# Dicionario: indexar os valores da lista

esp = ', '

carro = {'nome':'Bugatti' + esp + ' Fusca' + esp + ' Ferrari', 'cor':'azul' + esp + 'amarelo' + esp + 'branco', 'preco':'12000' + esp + '50000000' + esp + '14000', 'hp':'200'}
# print(carro['color'])
# print(carro['hp'])

for nome, color in carro.items():
    print(nome + ' ' + color) 

# Conjunto

lista = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,5,5,5]

lista = list[set(lista)]
print(lista)