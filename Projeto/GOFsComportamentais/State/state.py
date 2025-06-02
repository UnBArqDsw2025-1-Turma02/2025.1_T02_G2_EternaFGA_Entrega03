from abc import ABC, abstractmethod
from datetime import date
from typing import List


# --- Classes auxiliares ---
class Usuario:
    def __init__(self, nome: str):
        self.nome = nome


class MidiaDigital:
    def __init__(self, nome_arquivo: str):
        self.nome_arquivo = nome_arquivo


class Tag:
    def __init__(self, nome: str):
        self.nome = nome


# --- Interface do State ---
class StateMemoria(ABC):
    @abstractmethod
    def alterar_estado(self, memoria: 'Memoria') -> None:
        pass

    @abstractmethod
    def get_observacao(self) -> str:
        pass


# --- Estados Concretos ---
class AprovadoState(StateMemoria):
    def alterar_estado(self, memoria: 'Memoria') -> None:
        print("📌 Memória já está aprovada.")

    def get_observacao(self) -> str:
        return "✅ Memória aprovada."


class ReprovadoState(StateMemoria):
    def alterar_estado(self, memoria: 'Memoria') -> None:
        print("🔁 Alterando estado para 'Aprovado'.")
        memoria.estado_memoria = AprovadoState()

    def get_observacao(self) -> str:
        return "❌ Memória reprovada."


class PendenteState(StateMemoria):
    def alterar_estado(self, memoria: 'Memoria') -> None:
        print("🔁 Alterando estado para 'Reprovado'.")
        memoria.estado_memoria = ReprovadoState()

    def get_observacao(self) -> str:
        return "⏳ Memória pendente de aprovação."


# --- Classe principal ---
class Memoria:
    def __init__(self, id: int, titulo: str, descricao: str, autor: Usuario):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.midias: List[MidiaDigital] = []
        self.autor = autor
        self.data_envio = date.today()
        self.estado_memoria: StateMemoria = PendenteState()

    def adicionar_tag(self, tag: Tag) -> None:
        print(f"🏷️ Tag '{tag.nome}' adicionada à memória.")

    def alterar_estado(self):
        self.estado_memoria.alterar_estado(self)

    def get_observacao_estado(self) -> str:
        return self.estado_memoria.get_observacao()


# --- Execução Interativa ---
def menu():
    print("\n--- MENU DE MEMÓRIA ---")
    print("1. Ver estado atual")
    print("2. Alterar estado")
    print("3. Adicionar tag")
    print("4. Sair")


def main():
    autor = Usuario("Duda")
    memoria = Memoria(1, "Minha Primeira Memória", "Descrição da memória", autor)

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print(f"\n🧾 Estado atual: {memoria.get_observacao_estado()}")

        elif opcao == "2":
            print("\n🔄 Alterando estado da memória...")
            memoria.alterar_estado()

        elif opcao == "3":
            nome_tag = input("Digite o nome da tag: ")
            tag = Tag(nome_tag)
            memoria.adicionar_tag(tag)

        elif opcao == "4":
            print("👋 Saindo...")
            break

        else:
            print("❗ Opção inválida.")


if __name__ == "__main__":
    main()
