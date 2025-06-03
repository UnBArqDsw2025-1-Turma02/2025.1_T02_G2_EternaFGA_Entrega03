from abc import ABC, abstractmethod

class CompartilhamentoMemoria(ABC):
    def compartilhar(self, memoria):
        self.preparar(memoria)
        self.executar(memoria)
        self.finalizar()

    def preparar(self, memoria):
        print(f"[Preparar] Iniciando compartilhamento da memória: {memoria['titulo']}")

    @abstractmethod
    def executar(self, memoria):
        pass

    def finalizar(self):
        print("[Finalizar] Compartilhamento concluído.\n")


class CompartilharPorLink(CompartilhamentoMemoria):
    def executar(self, memoria):
        link = f"https://meusite.com/memoria/{memoria['id']}"
        print(f"[Link Copiado] Link: {link}")


class CompartilharExterno(CompartilhamentoMemoria, ABC):
    def executar(self, memoria):
        canal = self.definir_canal()
        link = f"https://meusite.com/memoria/{memoria['id']}"
        print(f"[{canal}] Enviando link: {link}")

    @abstractmethod
    def definir_canal(self):
        pass


class CompartilharPorWhatsApp(CompartilharExterno):
    def definir_canal(self):
        return "WhatsApp"


class CompartilharPorTelegram(CompartilharExterno):
    def definir_canal(self):
        return "Telegram"


class CompartilharPorEmail(CompartilharExterno):
    def definir_canal(self):
        return "Email"


class Usuario:
    def __init__(self, nome):
        self.nome = nome

    def compartilhar_memoria(self, memoria, estrategia: CompartilhamentoMemoria):
        print(f"\nUsuário {self.nome} está compartilhando uma memória...")
        estrategia.compartilhar(memoria)


# Exemplo com interação
if __name__ == "__main__":
    memoria = {
        "id": 42,
        "titulo": "Viagem com a equipe de competição"
    }

    usuario = Usuario("Maria")

    print("=== Dados da memória ===")
    print(f"Título: {memoria['titulo']}")
    print(f"ID: {memoria['id']}\n")

    print("Escolha a forma de compartilhamento:")
    print("1 - Link")
    print("2 - WhatsApp")
    print("3 - Telegram")
    print("4 - Email")
    opcao = input("Digite o número da opção: ")

    estrategias = {
        "1": CompartilharPorLink(),
        "2": CompartilharPorWhatsApp(),
        "3": CompartilharPorTelegram(),
        "4": CompartilharPorEmail()
    }

    estrategia = estrategias.get(opcao)

    if estrategia:
        usuario.compartilhar_memoria(memoria, estrategia)
    else:
        print("[Erro] Opção inválida.")
