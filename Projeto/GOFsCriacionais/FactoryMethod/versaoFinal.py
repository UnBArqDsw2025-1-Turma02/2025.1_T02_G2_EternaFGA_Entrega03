from abc import ABC, abstractmethod
from typing import Optional, Any, Dict

# Produto
class MidiaDigital(ABC):
    def __init__(self, url: str, formato: str, legenda: Optional[str] = None):
        self.url = url
        self.formato = formato
        self.legenda = legenda if legenda else "Mídia sem legenda"

# Produto Concreto 1
class Video(MidiaDigital):
    """
    Representa um arquivo de vídeo, um tipo de MidiaDigital.
    """
    def __init__(self, url: str, formato: str, legenda: Optional[str] = None, duracao: str = "00:00"):
        super().__init__(url, formato, legenda)
        self.duracao = duracao # Atributo específico do vídeo

# Produto Concreto 2
class Imagem(MidiaDigital):
    """
    Representa um arquivo de imagem, um tipo de MidiaDigital.
    """
    def __init__(self, url: str, formato: str, legenda: Optional[str] = None, resolucao: str = "N/A"):
        super().__init__(url, formato, legenda)
        self.resolucao = resolucao # Atributo específico da imagem

# Creator (fábrica abstrata)
class CreateMidiaDigital(ABC):
    def __init__(self):
        self.midia = None

    @abstractmethod
    def criarMidia(self, url: str, formato: str, legenda: Optional[str] = None, **kwargs: Any) -> MidiaDigital:
        pass

    def enviar(self):
        print(f"Enviando mídia com ID {self.midia.id} e legenda: {self.midia.legenda}")

# Fábrica concreta para vídeo
class CreateVideo(CreateMidiaDigital):

    def criarMidia(self, url: str, formato: str, legenda: Optional[str] = None, **kwargs: Any) -> MidiaDigital:
        duracao = kwargs.get("duracao", "00:00")
        return Video(url, formato, legenda, duracao=duracao)

# Fábrica concreta para imagem
class CreateImagem(CreateMidiaDigital):

    def criar_midia(self, url: str, formato: str, legenda: Optional[str] = None, **kwargs: Any) -> MidiaDigital:
        resolucao = kwargs.get("resolucao", "N/A")
        return Imagem(url, formato, legenda, resolucao=resolucao)
    
