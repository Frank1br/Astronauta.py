
suprimentos = {
    "Comida Desidratada": 300,
    "Tanque de Oxigenio": 200,
    "Kit de Primeiros Socorros": 150,
    "Ferramentas": 250,
    "Laptop Cientifico": 100,
}


capacidade_total = 1000

nome = input("Digite seu nome, astronauta: ")

carga_utilizada = 0
itens_carregados = []


print("\nLista de suprimentos disponíveis:")
for item, peso in suprimentos.items():
    print(f"- {item} ({peso} kg)")

print("\nDigite o nome do item que deseja carregar ou 'fim' para encerrar.\n")

# Loop de seleção
while True:
    escolha = input("Escolha um item: ")

    if escolha.lower() == "fim":
        break

    if escolha in suprimentos:
        peso_item = suprimentos[escolha]

        if carga_utilizada + peso_item <= capacidade_total:
            carga_utilizada += peso_item
            itens_carregados.append(escolha)
            print(f"✔ {escolha} carregado. Carga atual: {carga_utilizada} kg")
        else:
            print(f"Não há espaço suficiente para carregar {escolha}.")
    else:
        print("Item inválido. Tente novamente.")


print("\n Preparação finalizada!")
print(f"Astronauta: {nome}")
print(f"Total de carga utilizada: {carga_utilizada} kg")
print(f"Espaço restante: {capacidade_total - carga_utilizada} kg")
print("Itens carregados:", ", ".join(itens_carregados) if itens_carregados else "Nenhum")
