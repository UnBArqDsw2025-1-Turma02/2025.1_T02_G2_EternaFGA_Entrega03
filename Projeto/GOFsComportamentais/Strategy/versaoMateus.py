from abc import ABC, abstractmethod
from typing import Optional

class Strategy(ABC):
    @abstractmethod
    def processar(self, midia: 'MidiaDigital') -> None:
        pass


class StrategyVideo(Strategy):
    def processar(self, midia: 'MidiaDigital') -> None:
        print(f"Exibindo prévia {midia.urlArquivo}")


class StrategyImagem(Strategy):
    def processar(self, midia: 'MidiaDigital') -> None:
        print(f"Gerando miniatura para imagem {midia.urlArquivo} com resolução {midia.resolucao}...")


class MidiaDigital:
    def __init__(self, id: int, formato: str, legenda: str, strategy: Optional[Strategy] = None):
        self.id = id
        self.formato = formato
        self.legenda = legenda
        self.strategy = strategy

    def set_strategy(self, strategy: Strategy):
        self.strategy = strategy

    def executar_processamento(self):
        if self.strategy:
            self.strategy.processar(self)


class Video(MidiaDigital):
    def __init__(self, id: int, formato: str, legenda: str, urlArquivo: str, duracao: str):
        super().__init__(id, formato, legenda)
        self.urlArquivo = urlArquivo
        self.duracao = duracao


class Imagem(MidiaDigital):
    def __init__(self, id: int, formato: str, legenda: str, urlArquivo: str, textoAlternativo: str, resolucao: str):
        super().__init__(id, formato, legenda)
        self.urlArquivo = urlArquivo
        self.textoAlternativo = textoAlternativo
        self.resolucao = resolucao

        
video = Video(1, "mp4", "Vídeo da viagem", "video.mp4", "120")
imagem = Imagem(2, "jpg", "Imagem do quadro", "imagem.jpg", "Aula de Arquitetura", "400x300")

video.set_strategy(StrategyVideo())
imagem.set_strategy(StrategyImagem())
video.executar_processamento()
imagem.executar_processamento()

