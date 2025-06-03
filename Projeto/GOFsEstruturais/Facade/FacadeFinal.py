class Memoria:
    def __init__(self, imagem_url, titulo, descricao, data_memoria):
        self.imagem_url = imagem_url
        self.titulo = titulo
        self.descricao = descricao
        self.data_memoria = data_memoria

class ValidadorDeMemoria:
    def validar(self, memoria: Memoria):
        if not memoria.imagem_url:
            raise ValueError("Imagem obrigatória")
        if not memoria.titulo:
            raise ValueError("Título obrigatório")
        if not memoria.descricao:
            raise ValueError("Descrição obrigatória")
        if not memoria.data_memoria:
            raise ValueError("Data da memória obrigatória")


class ArmazenacaoDeMemoria:
    def salvar(self, memoria: Memoria):
        print("Nova memória salva no banco de dados")


class NotificacaoAdmin:
    def notificar(self, memoria: Memoria):
        print("Admin notificado sobre nova memória enviada")


class EnvioDeMemoriaFacade:
    def __init__(self):
        self.validador = ValidadorDeMemoria()
        self.armazenamento = ArmazenacaoDeMemoria()
        self.notificacao = NotificacaoAdmin()

    def enviar_memoria(self, memoria: Memoria):
        self.validador.validar(memoria)
        self.armazenamento.salvar(memoria)
        self.notificacao.notificar(memoria)
        print("Envio concluído com sucesso")



class Usuario:
    def compartilharMemoria(self, memoria: Memoria):
        facade = EnvioDeMemoriaFacade()
        facade.enviar_memoria(memoria)

if __name__ == "__main__":
    memoria1 = Memoria(
        imagem_url="https://exemplo.com/foto1.jpg",
        titulo="Viagem à praia",
        descricao="Foi um dia ensolarado e perfeito para relaxar.",
        data_memoria="2025-01-10"
    )

    memoria2 = Memoria(
        imagem_url="https://exemplo.com/foto2.jpg",
        titulo="Formatura do Ensino Médio",
        descricao="Momento emocionante com amigos e familiares.",
        data_memoria="2024-12-05"
    )

    usuario = Usuario()

    # Enviando primeira memória
    print("=== Memória 1 enviada ===")
    print(f"Título: {memoria1.titulo}")
    print(f"Descrição: {memoria1.descricao}")
    print(f"Data: {memoria1.data_memoria}")
    print(f"Imagem: {memoria1.imagem_url}")
    usuario.compartilharMemoria(memoria1)
    print()

    # Enviando segunda memória
    print("=== Memória 2 enviada ===")
    print(f"Título: {memoria2.titulo}")
    print(f"Descrição: {memoria2.descricao}")
    print(f"Data: {memoria2.data_memoria}")
    print(f"Imagem: {memoria2.imagem_url}")
    usuario.compartilharMemoria(memoria2)

