'''
Escreva um programa que calcula e escreva a tabela de graus Centígrados em função
dos graus Farenheit que variem entre 1 e 150 de 1 em 1 conforme a fórmula a seguir:

C = 5/9*(F-32)
'''

def calcDegreeCentigrade(limit):
    for i in range(1, limit+1, 1):
        c = 5/9*(i - 32)
        print(c)

calcDegreeCentigrade(150)