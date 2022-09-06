from ast import Lambda
from operator import truediv

# tipos basicos 
idade =27
ano =1995

print(type(idade))
print(type(ano))

nome = 'Alyce'
idade = 25
altura = 1.75
feriado = True

print(type(nome))
print(type(idade))
print(type(altura))
print(type(feriado))
print(type(feriado),(altura))

seis = 6
dez = 10

soma = seis+dez
print (soma)

subtração = seis-dez
print (subtração)

divisão = soma / dez
print (divisão)

multiplicação = subtração*dez
print (multiplicação)

Divisão_interna = seis // dez
print (Divisão_interna)

modulo = seis % dez
print (modulo)

exponenciacao = seis ** dez
print (exponenciacao)

var1 = 4.12
var2 = 5.34
divisao_interna = var2 // var1
print(divisao_interna)

#igual a 
variavel = 5



#operadores de comparação
variavel = 5

#igual a 
if variavel == 5:
    print ('os valores são iguais')
# diferente de     
if variavel != 7:
    print ('o valor da variavel não é igual a 7')   
# maior que     
if variavel > 2:
    print ('o valor da variavel é maior que 2')
#maior ou igual a    
if variavel >= 5:
    print ('o valor da variavel é maior ou igual 5')
#menor ou igual     
if variavel < 7:
    print ('o valor da variavel é menor ou igual a 7')
#menor     
if variavel <= 5:
    print ('o valor da variavel é menor que 5')  
    
    
    # = equivale a x=1 
numero = 5

numero += 7
print(numero) #soma 5+7= 12 (atribui)

# -= equivale a x=x-1
numero = 5
    
numero -=3
print(numero)# 5-3 =2 

# *= equivale a x=x*1
numero = 5

numero*=2
print(numero)#5*2 =10

# /= equivale a x=x/1
numero = 5

numero /=4
print(numero) #5/4 

# %= equivale a x=x%1
numero = 5

numero %=2
print(numero) 

num1 = 7
num2 = 4

#exemplo operador and : Retorna True se ambas condições forem verdadeiras
if num1 > 3 and num2 <8:
    print('as duas condições são verdadeiras')     

# exemplo operador or : Retorna True se uma das condições forem verdadeiras
if num1 > 4 or num2 <=8:
    print(' uma ou duas condições são verdadeiras') 

#exemplo operador not   : Retorna falso se o valor for verdadeiro    
if num1 > 30 and num2 > 8 :
    print( 'inverte o resultado da condição entre os parametros')
    
#exemplo de NOT

a = ['a', 'b', 'c', 'd']

lista = ['a', 'b', 'c', 'd'] 
if 'e' not in lista:
    print('não tem o c na lista')
else:
    print('tem o c na lista')

#not(True) = False e not(False) = True
    