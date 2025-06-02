from abc import ABC, abstractmethod


# --- Interface base da página ---
class Pagina(ABC):
    @abstractmethod
    def exibir_pagina(self) -> str:
        pass


# --- Implementação concreta da página padrão ---
class PaginaConcreta(Pagina):
    def exibir_pagina(self) -> str:
        return "Exibindo página padrão."

    def mudar_tema(self) -> str:
        return "Tema padrão aplicado."


# --- Decorator base ---
class PaginaDecorator(Pagina):
    def __init__(self, pagina: Pagina):
        self.wrapper = pagina

    def exibir_pagina(self) -> str:
        return self.wrapper.exibir_pagina()


# --- Decorator de Contraste ---
class Contraste(PaginaDecorator):
    def alterar_contraste(self) -> str:
        return "Contraste aumentado."

    def alterar_cor(self) -> str:
        return "Cor ajustada para acessibilidade."

    def exibir_pagina(self) -> str:
        return f"{self.wrapper.exibir_pagina()} + {self.alterar_contraste()} + {self.alterar_cor()}"


# --- Decorator de Tamanho da Fonte ---
class TamanhoFonte(PaginaDecorator):
    def aumentar_fonte(self) -> str:
        return "Fonte aumentada."

    def diminuir_fonte(self) -> str:
        return "Fonte diminuída."

    def mudar_cor(self) -> str:
        return "Cor da fonte alterada."

    def exibir_pagina(self) -> str:
        return f"{self.wrapper.exibir_pagina()} + {self.aumentar_fonte()} + {self.mudar_cor()}"


# --- Decorator de Tamanho dos Botões ---
class TamanhoBotao(PaginaDecorator):
    def aumentar_botao(self) -> str:
        return "Botões aumentados."

    def diminuir_botao(self) -> str:
        return "Botões diminuídos."

    def alterar_cor_botao(self) -> str:
        return "Cor dos botões alterada."

    def exibir_pagina(self) -> str:
        return f"{self.wrapper.exibir_pagina()} + {self.aumentar_botao()} + {self.alterar_cor_botao()}"


# --- Execução Interativa ---
def menu():
    print("\n--- MENU DE ACESSIBILIDADE ---")
    print("1. Página padrão")
    print("2. Aplicar contraste")
    print("3. Aplicar aumento de fonte")
    print("4. Aplicar aumento de botões")
    print("5. Aplicar tudo junto")
    print("6. Sair")


def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            pagina = PaginaConcreta()
            print(f"\n🔍 {pagina.exibir_pagina()}")

        elif opcao == "2":
            pagina = Contraste(PaginaConcreta())
            print(f"\n🌈 {pagina.exibir_pagina()}")

        elif opcao == "3":
            pagina = TamanhoFonte(PaginaConcreta())
            print(f"\n🔠 {pagina.exibir_pagina()}")

        elif opcao == "4":
            pagina = TamanhoBotao(PaginaConcreta())
            print(f"\n🔳 {pagina.exibir_pagina()}")

        elif opcao == "5":
            pagina = TamanhoBotao(TamanhoFonte(Contraste(PaginaConcreta())))
            print(f"\n💡 {pagina.exibir_pagina()}")

        elif opcao == "6":
            print("\n👋 Encerrando...")
            break

        else:
            print("❗ Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
