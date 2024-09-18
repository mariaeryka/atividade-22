# Crie um programa que receba vários números do usuário e some-os até que o número 0 seja digitado, momento em que o programa deve exibir o valor total.

soma = 0

while (numero := float(input("Digite um número (ou 0 para sair): "))) != 0:
    soma += numero

print("A soma total é:", soma)

