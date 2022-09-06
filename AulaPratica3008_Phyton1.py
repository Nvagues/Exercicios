# Conversão implicita - Interpretador converte automaticamente 

from configparser import Interpolation, InterpolationDepthError
from csv import list_dialects
from operator import index
import string
from traceback import print_list


a = 15
print (f' a variavel a é do tipo: {type(a)}')

b = 10.6
a = a+b
print(f'Valor sa oma : {a}')

print (f' a variavel a é so tipo:{type(a)}')

#função para conversão 
# int(a, base)Inteiro 
# float() float
# str() string
# dict() dicionario
# ord() caractere em Inteiro 
# hex() numero em string hexadecimal 
# oct() inteiro em octal 
# tupla: em tupla 

a = 1
print (type(a))

a = str(a)
print (type(a))

b = ["a" , "b" , "c" , "d"]
print(type(b))

b = tuple(b)
print(type (b))

print (b)

lista = ["banana", "limão","maça", "pera"]
print(type(lista))

lista = tuple(lista)
print(type(lista))
print(lista)

#lista = coleção ordenada de valor , onde cada um é identificado por indices. 

# lista = ["banana" , "Caju" , "Melao" , 5 , "Pera" , 10]
# #index usa o enumerate ( Loop com item/ percorre os elementos e os interaveis )
# for index, elemento in enumerate (lista) : 
#     print(index)
    
#como acessar dados em uma lista 
lista=['maça', 'banana','jaca','melão','abacaxi']
print(f'estou buscando a fruta : {lista[2]}')
print(f'estou buscando a fruta : {lista[-1]}')
print(f'estou buscando a fruta : {lista[0]}')

# pegar o ultimo numero na lista coloca o -1/tamanho da lista lenght
# f - formatar - concatenar 

#lista dentro de lista - para acessarmos a sublista é necessário que busquemos o indice de onde a mesma esta 
#lista = ['maça, [banana', 'jaca'], 'melão', 'abacaxi']
#sublista = lista[1]
#print( f'acessando a sublista:{'sublista'})

# output [banana, jaca]
#acessando item da sublista 
#print(f'acessando um item da sublista:{sublista[0]}')
#output[banana]

lista = [0,5,8,10,35,15,7,4,12,22,3,2,9,1,]
list_append = []
    
for i in lista :
    list_append.append(i+1)
print(f' Append:{list_append}') #output  [1, 6, 9, 11, 36, 16, 8, 5, 13, 23, 4, 3, 10, 2]   

list_append.extend([0,0,0,0])
print(f'Extend:{list_append}')#output Extend:[1, 6, 9, 11, 36, 16, 8, 5, 13, 23, 4, 3, 10, 2, 0, 0, 0, 0]

list_append.insert(8, 'meio')
print(f'Insert:{list_append}')#[1, 6, 9, 11, 36, 16, 8, 5, 'meio', 13, 23, 4, 3, 10, 2, 0, 0, 0, 0]

#remover os inteiros    

list_append.remove("meio")
print(f'remove:{list_append}')#outpu [1, 6, 9, 11, 36, 16, 8, 5, 13, 23, 4, 3, 10, 2, 0, 0, 0, 0]

list_append.pop(4)
print(f'Pop:{list_append}') #output resultados da lista:[1, 6, 9, 11, 16, 8, 5, 13, 23, 4, 3, 10, 2, 0, 0, 0, 0]

print(f'Index:{list_append.index(2)}') #output Index:12

list_append.sort()
print(f'sort: {list_append}')#output [0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 13, 16, 23]

list_append.reverse()
print(f'Reverse:{list_append}') #output [23, 16, 13, 11, 10, 9, 8, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0]

list_new = list_append.copy() #output[23, 16, 13, 11, 10, 9, 8, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0]
print(f'Copy:{list_new}')


lista = ["Banana" , "Caju" , "Melao" , 5, "Pera" , 10]
list_new = []

for elemento in lista:
    list_new = []
    if type(elemento) != int:
        list_new.append (elemento)
        print(list_new)
 
# for index, elemento  in enumerate(lista):
#     if elemento = int:
#         lista.pop()
#     print(index)        

lista = [0,5,8,10,35,15,7,4,12,22,3,2,9,1]
lista_numeros_maior_10=[] #criou essa lista vazia pois vai atribuir todos os numeros maior que 10 dentro dela 
#utiliza o append para inserir os numeros maior que dez nessa lista 

for i in lista:
    if i > 10:
        lista_numeros_maior_10.append(i)
        print(f'resultados da lista:{lista_numeros_maior_10}')
        
        #tbm pode ser feito assim :
        
lista_numeros_maior_10 = [i for i in lista if i > 10]
print(f'resultados da lista:{lista_numeros_maior_10}')        

#lista comprehensions - Mais otimizada de criar uma lista atraves de outra 
lista = [1,2,3,4,5,6,7,8,9,10]
lista = [i for i in range(18) if i%2 != 0]
print(lista)
#output [0,2,4,6,8] range = variavel de 0 a 10


#não tão bom 
i=0 
lista = []
while i < 10:
    if i%2 == 10:
        lista.append(i)
        print(lista )
        
        #% quando o traz o numero par 
        
        #tupla = Imutavel 
   
tupla = (('MG', 'Minas Gerais'), ('SP', 'São Paulo'),[0,1,2,3])
print(f'Remove o ultimo elemento da lista da tupla e retorna :{tupla[2].pop()}') #remover o ultimo item na lista no caso o 3

    
#output = 3
 #output [0,1,2,]a tupla não altera somente a lista       
    
#MAP  #dada uma lista retornar outra lista contendo a soma do elemento por ele mesmo 
#map() - Syntax  map(função, iteraveis)
#Uma operação especifica para transforma los em outra coisa 
   
lista = [0,1,2,3,4,5,6,7,8,9]
lista_somada = map(lambda x: x+x, lista) #map esta percorrendo o elemento que é o X, o x == X+X
print(list(lista_somada))
#Output : 0,2,4,6,8,10,12,14,16,18

#FILTER 
#filter() - Syntax filter(função, iteraveis) - Quando precisamos filtar elementos da lista
#retornar apenas os pares :
# lista = [0,1,2,3,4,5,6,7,8,9]
# pares = filter(Lambda x:x%2 == 0,lista)
# print(list(pares))
#output [0,2,4,6,8]

#REDUCE
#reduce() - Syntax reduce(função, iteraveis) todos os elementos da lista sera reduzido apenas a um elemento
#precisa importar o modulo functools

from functools import reduce 

#somar os itens da lista 

lista = [0,1,2,3,4,5,6,7,8,9]
soma = reduce( lambda x,y:x+y,lista,0) #x vale 0 y vale 1, depois o x vale 1 e o y 2, depois o x vale 3 e o y 3..
print(soma)
#Output: 45


#criar função :

#def foo(value):argumento parametro valor 
#print('f Olá, esse é o parametro:{value}') vou imprimir valor 
# foo ('LuizaCode')

#Parametros

def calcula_salario(valor, horas=220):
    return valor*horas
print(calcula_salario(35))   
#output (7700)                                        
                                
#LAMBDA
lista = [1,2,3,4,5,6,7,8,9]
pares = []
def func_par():#percorre a lista pega p resultado da divisão por 2 =0 e coloca na lista de pares 
    for i in lista:
        if i in lista:
            if i%2 == 0:
                pares.append(i)
    return pares
print(func_par())
#output:[2,4,6,8]

# print(list(filter(lambda x%2 ==0,lista)))    
# #output [2,4,6,8]




#mais exemplo de Map 

lista = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

def calcula_elemento_por_ele_mesmo(elemento):
    return elemento + elemento
lista = map(calcula_elemento_por_ele_mesmo, lista)#como se ele tivesse fazendo um for na lista 
print(list(lista))

#lambda
# def calcula_elemento_por_ele_mesmo(elemento):
#     return elemento + elemento
# lista = map(lambda elemento : elemento + elemento , lista)#como se ele tivesse fazendo um for na lista 
# print(list(lista))


#filter 

