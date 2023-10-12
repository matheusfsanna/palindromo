# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 17:44:19 2023

@author: Matheus
"""

def e_palindrome(number):
    return str(number) == str(number)[::-1]

def encontre_o_maior(num1, num2):
    if num1 < 1000 or num1 > 9999 or num2 < 1000 or num2 > 9999:
        raise ValueError("Ambos os números devem ter 4 dígitos")

    maior = 0
    for i in range(num1, num2, -1):
        for j in range(num1, num2, -1):
            produto = i * j
            if e_palindrome(produto) and produto > maior:
                maior = produto
    return maior
try:
    # Fornecer os dois números com 4 dígitos
    numero1 = int(input("Digite o primeiro número com 4 dígitos: "))
    numero2 = int(input("Digite o segundo número com 4 dígitos: "))

    resultado = encontre_o_maior(numero1, numero2)
    if resultado == 0:
        print("Não existem palindromos com a multiplicação desses dois números")
    else:
        print(f"O maior palíndromo entre {numero1} e {numero2} é: {resultado}")

except ValueError as e:
    print(f"Erro: {e}")
except Exception as e:
    print(f"Erro inesperado: {e}")