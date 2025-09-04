import uuid
import os

ARQUIVO = "livros.txt"

while True:
    print("\n=== Biblioteca ===")
    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Pesquisar livro")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        # Cadastrar livro
        id_livro = str(uuid.uuid4())
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")

        with open(ARQUIVO, "a", encoding="utf-8") as f:
            f.write(f"{id_livro};{titulo};{autor}\n")

        print("Livro cadastrado com sucesso!")

    elif opcao == "2":
        # Listar livros
        if not os.path.exists(ARQUIVO):
            print("⚠ Nenhum livro cadastrado ainda.")
        else:
            with open(ARQUIVO, "r", encoding="utf-8") as f:
                livros = f.readlines()

            print("\n📚 Lista de Livros:")
            for linha in livros:
                id_livro, titulo, autor = linha.strip().split(";")
                print(f"ID: {id_livro} | Título: {titulo} | Autor: {autor}")

    elif opcao == "3":
        # Pesquisar livro
        termo = input("Digite o título ou autor para pesquisar: ").lower()

        if not os.path.exists(ARQUIVO):
            print("⚠ Nenhum livro cadastrado ainda.")
        else:
            with open(ARQUIVO, "r") as biblioteca:
                livros = biblioteca.readlines()

            encontrados = [l for l in livros if termo in l.lower()]

            if encontrados:
                print("\n🔍 Resultados da pesquisa:")
                for linha in encontrados:
                    id_livro, titulo, autor = linha.strip().split(";")
                    print(f"ID: {id_livro} | Título: {titulo} | Autor: {autor}")
            else:
                print("⚠ Nenhum livro encontrado.")

    elif opcao == "0":
        print("👋 Saindo...")
        break

    else:
        print("Opção inválida!")
