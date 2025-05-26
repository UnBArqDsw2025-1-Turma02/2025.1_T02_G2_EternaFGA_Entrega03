from abc import ABC, abstractmethod
from typing import Optional, Dict


# Produto abstrato
class MidiaDigital(ABC):
    def __init__(self, url: str, formato: str, legenda: Optional[str] = None):
        self.url = url
        self.formato = formato
        self.legenda = legenda or "Sem legenda"

    @abstractmethod
    def exibir_info(self) -> str:
        pass


# Produtos concretos
class Imagem(MidiaDigital):
    def __init__(self, url: str, formato: str, legenda: Optional[str] = None, texto_alternativo: str = ""):
        super().__init__(url, formato, legenda)
        self.texto_alternativo = texto_alternativo

    def exibir_info(self) -> str:
        return f"[Imagem] URL: {self.url} | Alt: {self.texto_alternativo} | Formato: {self.formato} | Legenda: {self.legenda}"


class Video(MidiaDigital):
    def __init__(self, url: str, formato: str, legenda: Optional[str] = None, duracao: str = "00:00"):
        super().__init__(url, formato, legenda)
        self.duracao = duracao

    def exibir_info(self) -> str:
        return f"[Vídeo] URL: {self.url} | Duração: {self.duracao} | Formato: {self.formato} | Legenda: {self.legenda}"


# Fabricas concretas
class MidiaFactory(ABC):
    @abstractmethod
    def criar(self, url: str, formato: str, legenda: Optional[str], **kwargs) -> MidiaDigital:
        pass


class ImagemFactory(MidiaFactory):
    def criar(self, url: str, formato: str, legenda: Optional[str], **kwargs) -> Imagem:
        return Imagem(url, formato, legenda, texto_alternativo=kwargs.get("texto_alternativo", ""))


class VideoFactory(MidiaFactory):
    def criar(self, url: str, formato: str, legenda: Optional[str], **kwargs) -> Video:
        return Video(url, formato, legenda, duracao=kwargs.get("duracao", "00:00"))


# Gerenciador de fabricas
class GerenciadorMidia:
    def __init__(self):
        self.fabricas: Dict[str, MidiaFactory] = {}
        self.registrar_fabrica("imagem", ImagemFactory())
        self.registrar_fabrica("video", VideoFactory())

    def registrar_fabrica(self, tipo: str, fabrica: MidiaFactory):
        self.fabricas[tipo.lower()] = fabrica

    def criar_midia(self, tipo: str, url: str, formato: str, legenda: Optional[str] = None, **kwargs) -> MidiaDigital:
        fabrica = self.fabricas.get(tipo.lower())
        if not fabrica:
            raise ValueError(f"Tipo de mídia não suportado: {tipo}")
        return fabrica.criar(url, formato, legenda, **kwargs)


if __name__ == "__main__":
    gerenciador = GerenciadorMidia()

    midia1 = gerenciador.criar_midia(
        tipo="imagem",
        url="foto_evento.png",
        formato="png",
        legenda="Turma reunida 2023",
        texto_alternativo="Foto da turma no campus"
    )

    midia2 = gerenciador.criar_midia(
        tipo="video",
        url="apresentacao.mp4",
        formato="mp4",
        legenda="Apresentação de calouros",
        duracao="05:30"
    )

    print(midia1.exibir_info())
    print(midia2.exibir_info())
