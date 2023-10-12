"""Programa com ajuda do chat GPT"""

def eh_palindromo(num):
    return str(num) == str(num)[::-1]

def encontrar_maior_palindromo(num1, num2):
    maior_palindromo = 0

    for i in range(num1, num1 + 10000):
        for j in range(num2, num2 + 10000):
            produto = i * j
            if eh_palindromo(produto) and produto > maior_palindromo:
                maior_palindromo = produto

    return maior_palindromo

try:
    # Solicitar ao usuário para inserir os dois números de quatro dígitos
    num1 = int(input("Digite o primeiro número de quatro dígitos: "))
    num2 = int(input("Digite o segundo número de quatro dígitos: "))

    maior_palindromo = encontrar_maior_palindromo(num1, num2)

    if maior_palindromo != 0:
        print(f"O maior palíndromo na multiplicação de {num1} e {num2} é: {maior_palindromo}")
    else:
        print(f"Não foi encontrado nenhum palíndromo na multiplicação de {num1} e {num2}.")

except ValueError:
    print("Por favor, insira números válidos.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
finally:
    print("Programa encerrado.")
