import random

listaNumeroUsuario = []
numerosSorteados = []

while True:
    try:
        qtd = int(input("Quantos números você quer jogar? (6 a 20): "))
        if 6 <= qtd <= 20:
            break
        else:
            print("Por favor, insira um número entre 6 e 20.")
    except ValueError:
        print("Digite um número válido.")

print(f"Digite os {qtd} números entre 1 e 60:")

while len(listaNumeroUsuario) < qtd:
    try:
        numero = int(input(f"Digite o {len(listaNumeroUsuario) + 1}º número: "))
        if numero < 1 or numero > 60:
            print("Número fora do intervalo. Tente novamente.")
        elif numero in listaNumeroUsuario:
            print("Número já inserido. Tente novamente.")
        else:
            listaNumeroUsuario.append(numero)
    except ValueError:
        print("Digite um número válido.")

numerosSorteados = random.sample(range(1, 61), 6)

acertos = set(listaNumeroUsuario) & set(numerosSorteados)
qtd_acertos = len(acertos)

print(f"\nNúmeros sorteados: {sorted(numerosSorteados)}")
print(f"Números jogados: {sorted(listaNumeroUsuario)}")
print("Voce acertou: ", qtd_acertos)

if qtd_acertos == 6:
    print("Parabéns! Você fez a sena!")
elif qtd_acertos == 5:
    print("Muito bom! Você fez a quina!")
elif qtd_acertos == 4:
    print("Legal! Você fez a quadra!")
else:
    print("Não foi dessa vez. Tente novamente!")
    
