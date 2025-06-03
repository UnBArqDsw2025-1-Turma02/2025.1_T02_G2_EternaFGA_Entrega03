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
    memoria_exemplo = Memoria(
        imagem_url="https://exemplo.com/imagem.jpg",
        titulo="Aniversário da Vovó",
        descricao="Uma linda festa com toda a família reunida.",
        data_memoria="2024-12-20"
    )

    usuario = Usuario()
    usuario.compartilharMemoria(memoria_exemplo)