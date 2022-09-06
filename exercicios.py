#1) O Python trabalha tipos de valores. Com os valores abaixo, dê o nome de seus tipos:


#2) Digite cada linha abaixo no shell do Python e informe quais estão corretos e quais
#apresentam erro:


# 1
# 1a
# a1
# 1.
# .2
# -.3
# 'agua"limpa'
# "agua""
# """teste 1 2 3"""

# a inteiro 
# b float 
# c boleano
# d boleano 
# e float
# f float
# g string
# h string

#operadores aritmeticos 

#a. Operadores matemáticos

from email.mime import base
from msilib.schema import Media


Valor1 = 10
Valor2 = 3
Valor3 = 3.0


# #soma

soma = Valor1+Valor2    
print (soma)

# #subtracao

subtracao = Valor1-Valor2
print (subtracao)

# #multiplicação 

multiplicacao = Valor1*Valor2   
print (multiplicacao)

divisao = Valor1/Valor2
print(divisao)

divisao2 = Valor1/Valor3
print (divisao2)

divisao3 = soma/Valor2
print (divisao3)

divisao4 = soma/Valor3
print (divisao4)

divisao_inteiros = soma/Valor3
print (divisao3)

# #Ordem dos operadores

v1 = 5
v2 = 30
v3 = 20


exemplo1 = v1+v2*v3
print(exemplo1)

exemplo2 = (v1+v2)*v3
print(exemplo2)

exemplo3 = ((v1+v2)*v3)/(v2-v3)
print(exemplo3)

exemplo4 = v1+v2*v3/(v2-v3)
print(exemplo4)


# c. Operadores comparação


if 2 < 3: 
 print( 'dois e menor que três')

if 9 > 8:
 print( 'nove e maior que oito')
    
if 1 == 1:    
  print('os valores são iguais')
    
if 1!= 2:
  print('os valores são diferentes')  

if 1!=1:
   print('os valores são diferentes')      

if 4<=4:
    print('quatro é menor ou igual a quatro')    

if 5>=6:
   print('cinco e maior ou igual a seis')  

if 1<2<3:
   print('um e menor que dois e menor que três')    

if 1<2<2:
    print('um é menor que dois e dois e menor que dois')

if 1+2<25/5:
   print('um mais dois e menor que vinte e cinco dividido por cinco')          

#Mais operadores matemáticos:

dois = 2
quatro = 4
vinte_e_seis = 26
cinco = 5

exponecial = dois ** quatro
print(exponecial)

modulo = vinte_e_seis % cinco
print(modulo)

# 4) Qual será o valor final de x?

x=10

x=x+10   # 20
x=100-x  # 100-20
print(x)

#. Calcule a área de um quadrado cujo lado seja 2 cm.
L_medida  =2 
expoente =2

Area_quadrado = L_medida ** expoente
print(Area_quadrado)


#Uma mala custa R$120,00. Esta recebeu 5% de desconto. Quanto você irá pagar por ela 

valor = 120
desconto = 5
desconto = desconto/100

valor_mala = valor - desconto
print (valor_mala)

#Um carro está viajando a uma velocidade média de 100 Km/h, o trecho de viagem será 200 Km. 
# Quantas horas irá demorar a viagem.

velocidade_carro = 100
trecho = 200

hora_viagem = velocidade_carro/trecho
print(hora_viagem,'hora'),

# João tem 2 pirulitos, Maria 3 pirulitos e Sofia 1 pirulito. Calcule o total de pirulitos e
# sua média.

Joao = 2
Maria = 3
Sofia = 1

Pirulitos = Joao+Maria+Sofia
print(Pirulitos)

# Davi tem 13 anos e sua irmã tem 7 anos. Guarde na variável eh_mais_velho a
# verificação se a idade de Davi é maior que a idade de sua irmã. OK 

Davi = 13
Irma = 7
eh_mais_velho = (Davi > Irma)
print(eh_mais_velho) 


# Qual será o valor de z? Qual seria outra forma de escrever este trecho de código?

z = 3  #3
z += 2  # 3+2 =5
z *= 6 #5*6 = 30
z /= 5 #30/5 

print(z)

# Considere as seguintes variáveis: AJUDA
# ovo = 3.4
# caju = 12.4
# # Qual será o valor de resposta em cada linha:

# ovo = 3.4
# caju = 12.4



# Qual é o resultado deste problema? Qual é o valor final da variável fim?

ab = 10
Ab = 20
aB = 30
AB = ab + Ab - aB
fim = AB + 1
print(fim)

#  Qual é o resultado de cada linha de comando do Python? Siga a ordem dos comandos. AJUDA

valor = input("Informe um valor:") #PERGUNTA O VALOR PARA O USUARIO 
print("Valor informado: ", valor) #VALOR INFORMADO : O VALOR QUE ELE COLOCOU 
tipo = type(valor) #ARMAZENADO QUAL O TIPO DA VARIAVEL VALOR 
x_str = "123" #VARIAVEL TEXTO QUE VALE 1,2,3,
x = int(x) #VAI SER CONVERTIDA EM INTEIRO 
xf = float(x) #XF VARIAVEL CONVERTENDO EM FLOAT 
sao_iguais = x == xf #ATRIBUINDO O RESULTADO DA CONDIÇÃO X ==XF A VARIAVEL SÃO IGUAIS 
print("Um float é igual a um int?", sao_iguais) #PRINTAR A INFORMAÇÃO 

# 10) Crie o seguinte programa Python no arquivo lista03_02.py: Colete o nome da
# pessoa, a cidade de nascimento dela, e o ano em que ela nasceu. Depois você irá mostrar
# os dados coletados em linhas diferentes. E também, deverá informar quantos anos a
# pessoa terá no ano 2030.

nome_da_pessoa = input("Informar o nome:")
cidade_de_nascimento = input("Informar a cidade de nascimento:")
ano_de_nascimento = int(input("ano de nascimento:"))
ano = 2030

print(nome_da_pessoa)
print(cidade_de_nascimento)
print(ano_de_nascimento)

idade_em_2030 = ano - ano_de_nascimento
print(idade_em_2030)

# 11) Programa Python no arquivo ex11.py: Este programa irá calcular a área de um
# quadrado. Peça para a pessoa informar a medida numérica de um lado do quadrado. E
# depois informe-lhe o valor da área do quadrado

area = float(input('valor da area do quadrado:'))
medida = float(input('medida numerica:'))

area_total = area * medida
print(area_total)


# 15). Para o programa Python no arquivo ex15.py: Em uma casa, uma família decidiu dividir
# o valor da conta de energia entre os moradores da casa. No programa eles informam o
# valor da conta de energia e quantos que irão pagar a conta no mês. O programa calculará
# quanto cada um deverá contribuir com a conta de energia.

valor_energia = float(input("Imforme o valor da conta de energia"))
print(type(valor_energia))

qtd_moradores = input("Quantos moradores:")
qtd_moradores = int(qtd_moradores)

print(type(qtd_moradores))

valor_para_cada = valor_energia/qtd_moradores
print(valor_para_cada)


#12) Programa Python no arquivo ex12.py: Este programa irá calcular a área de um
# triângulo. Peça para a pessoa informar a medida numérica da base do triângulo, depois
# colete o valor da altura. Apresente o valor da área do triângulo

base_do_triangulo = int(input("Base do triangulo:"))

area_total = base_do_triangulo * 3
print(area_total)

#13). Crie o seguinte programa Python no arquivo ex13.py: Colete a idade de 3 pessoas e
#mostre a média de suas idades.

idade_individuo1= input("informe sua idade :")
idade_individuo2= input("informe sua idade :")
idade_individuo3= input("informe sua idade :")

media=idade_individuo1+idade_individuo2+idade_individuo3/3

# 14) Crie o seguinte programa Python no arquivo ex14.py: Colete a idade de duas pessoas.
# E informe se a primeira idade é maior do que a da primeira. Neste aqui, basta responder
# True para informar que a primeira idade é maior que a primeira.

Idade_Ana = int(input("Informe sua idade:"))
Idade_Maria = int(input("Informe sua idade:"))

Ana_mais_velha = (Idade_Ana > Idade_Maria)
print(True)

# 16). Programa ex16.py: Estou tentando entender os juros do meu banco. Para isto, ele me
# informou esta fórmula:
# valor_final = valor_emprestimo + (valor_emprestimo * taxa * tempo)
# onde que:
# ● valor_emprestimo: É o valor que pegarei emprestado.
# ● taxa: É o valor da taxa por mês. Por exemplo: se for 4% ao mês, o valor será 0.04.
# ● tempo: Quantidade de meses que irei pagar o empréstimo.
# Crie um programa que colete cada um destes valores para calcular o valor final que estarei
# pagando ao banco.

Valor_do_emprestimo = float(input("Valor do emprestimo:")
Taxa                            
                            
                            )

