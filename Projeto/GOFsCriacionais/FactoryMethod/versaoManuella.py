from abc import ABC, abstractmethod

# Produto
class MidiaDigital(ABC):
    def __init__(self, id: int, legenda: str):
        self.id = id
        self.legenda = legenda

# Produto Concreto 1
class Video(MidiaDigital):
    def __init__(self, id: int, legenda: str, url_arquivo: str):
        super().__init__(id, legenda)
        self.url_arquivo = url_arquivo

# Produto Concreto 2
class Imagem(MidiaDigital):
    def __init__(self, id: int, legenda: str, url_arquivo: str, resolucao: str):
        super().__init__(id, legenda)
        self.url_arquivo = url_arquivo
        self.resolucao = resolucao

# Creator (fábrica abstrata)
class CreateMidiaDigital(ABC):
    def __init__(self):
        self.midia = None

    @abstractmethod
    def factory_method(self, id: int) -> MidiaDigital:
        pass

    def enviar(self):
        print(f"Enviando mídia com ID {self.midia.id} e legenda: {self.midia.legenda}")

# Fábrica concreta para vídeo
class CreateVideo(CreateMidiaDigital):
    def factory_method(self, id: int) -> MidiaDigital:
        self.midia = Video(id=id, legenda="Vídeo institucional", url_arquivo="video.mp4")
        return self.midia

# Fábrica concreta para imagem
class CreateImagem(CreateMidiaDigital):
    def factory_method(self, id: int) -> MidiaDigital:
        self.midia = Imagem(id=id, legenda="Imagem promocional", url_arquivo="imagem.jpg", resolucao="1920x1080")
        return self.midia
    

if __name__ == "__main__":
    criador_video = CreateVideo()
    midia_video = criador_video.factory_method(1)
    criador_video.enviar()

    criador_imagem = CreateImagem()
    midia_imagem = criador_imagem.factory_method(2)
    criador_imagem.enviar()
