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
        print(f"Usuário {self.nome} está compartilhando uma memória...")
        estrategia.compartilhar(memoria)



# Exemplo
if __name__ == "__main__":
    memoria = {
        "id": 42,
        "titulo": "Viagem para o interior"
    }

    usuario = Usuario("Maria")

    # Compartilhando de diferentes formas uma mesma memória
    usuario.compartilhar_memoria(memoria, CompartilharPorLink())
    usuario.compartilhar_memoria(memoria, CompartilharPorWhatsApp())
    usuario.compartilhar_memoria(memoria, CompartilharPorTelegram())
    usuario.compartilhar_memoria(memoria, CompartilharPorEmail())
