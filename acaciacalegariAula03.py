#Acacia C. Calegari
#lista03

#1- Funcao q retorna o valor absoluto d um numero fornecido
def absoluto(numero):
    '''funcao q retorna o valo absoluto de um numero
    float - float'''
    if numero < 0:
        return numero * -1
    else:
        return numero


#2- funcao q retorna quantas são as raizes reais de uma equacao do segundo grau importando a funcao delta da aula anterior
from acaciacalegarilista02 import delta

#funcao q calcula quantas sao as raizes reais
def qntsraizes (a, b, c):
    '''funcao q recebe valores e retorna a quantidade de raízes reais da equacao d segundo grau
    float,float,float - str'''
    determinante = delta(a, b, c)
    if determinante > 0:
        return "A equacao possui 2 raizes reais"
    elif determinante < 0:
        return "Nenhuma raiz real "
    else:
        return "A equacao possui 1 raiz real."


#3- Funcao q retorna a palavra digitada repetidamente pela quantidade desejada
def palavras (p, x):
    ''' funcao q retorna a mensagem digitada pela quantidade de vezes tambem digitada
    str,int - str'''
    return  str(p * x)

#4- Funcao q recebe tres numeros inteiros, e retorna  uma sequencia no formato de data DD/MM/AAAA
def data (d,m,a):
    '''funcao q recebe 3 nums, e retorna no formato de data dd/mm/aaaa
    int,int,int - str'''
    return str(d) + str('/')  + str(m) + str('/') + str(a)


#5- Funcao q tem o comportamento da figura matematica
def fig (x):
    '''funcao q tem o comportamento da figura
    float - float'''
    if 0<=x<2:
        return x
    if 2<=x<=3.5:
        return 2
    if 3.5<x<=5:
        return 3
    if x>5:
        return (x**2) - (10*x) + 28
    

#6- a)funcao q calcula e retorna a taxa de desconto de imposto de INSS de acordo com a tabela do INSS, 6% p salario bruto ate $2000.00, 8% até $3000.00 e 10% acima de $3000.00
def salariobruto (cash):
    '''funcao q recebe um valor e retorna a taxa de desconto do inss
    float - float'''
    if cash <= 2000.00:
        return (cash)*0.06
    elif cash <=3000.00:
        return (cash)*0.08
    else:
        return (cash)*0.10


#6- b)funcao q calcula e retorna a taxa de desconto ir, 11% ate $2500.00 , 15% ate $5000.00 e 22% acima de 5000.00
def ir (cash):
    '''funcao q recebe um valor e retorna a taxa de desconto do inss
    float - float'''
    if cash <= 2500.00:
        return (cash)*0.11
    elif cash <=5000.00:
        return (cash)*0.15
    else:
        return (cash)*0.22


#6- b)funcao q calcula e retorna o salario liquido , usando as funcoes 6-a) e 6-b)
def salarioliqd(cash):
    '''funcao q recebe um valor e retorna o salario liquido descontado pelas taxas acima
    float - float'''
    return cash - salariobruto(cash) - ir(cash)







    
    
    




    

