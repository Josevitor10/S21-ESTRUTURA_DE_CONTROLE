idade = int(input("Digite sua idade: ")) # Digite um número inteiro.
"""
Este programa mostra a faixa etária
"""

if idade < 18: # Esta é a primeira Condição.
    print("Menor de idade") # Menor de idade.
elif 18 <= idade < 60: # Esta é a segunda condição.
    print("Adulto") # Já é considerado Adulto.
else:# Maior que essa idade.
    print("Idoso") # Já é considerado idoso.