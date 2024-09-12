import random

numero_sorteado = random.randint(1, 10) # Será escolhido um número de 1 a 10
tentativas = 3 # Você tem 3 tentativas para acerta.

while tentativas > 0: # Enquanto a tentativas for mais que 0.
    palpite = int(input("Adivinhe um número de 1 a 10: "))
    
    if palpite == numero_sorteado: # Se o palpite for o mesmo número sorteado.
        print("Parabéns, você acertou!") # Aparecerá "Parabens, você acertou".
        break # È o sistema para. 
    elif palpite > numero_sorteado: # Se o palpite for maior do que o número sorteado.
        print("O número é menor.") # Aparecerá que o número sorteado é menor.
    else: # Caso o contrário.
        print("O número é maior.") # Aparecerá que o número sorteado é maior.
    
    tentativas -= 1 # Toda vez que errar, perderá uma tentativa.

if tentativas == 0: # Ser tiver a tentativas restantes.
    print(f"Você perdeu! O número era {numero_sorteado}.") # Aparecerá que você perdeu e apresentará o número sorteado.