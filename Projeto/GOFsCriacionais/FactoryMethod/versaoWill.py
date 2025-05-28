from abc import ABC, abstractmethod
from typing import Optional, Any


# Produto abstrato
class MidiaDigital(ABC):
    def __init__(self, url: str, formato: str, legenda: Optional[str] = None):
        self.url = url
        self.formato = formato
        self.legenda = legenda if legenda else "Sem legenda"

    @abstractmethod
    def exibir_info(self) -> str:
        pass

    def exibir_detalhes(self) -> None:
        print(self.exibir_info())


# Produto concreto: Imagem
class Imagem(MidiaDigital):
    def __init__(self, url: str, formato: str, legenda: Optional[str] = None, resolucao: str = "N/A"):
        super().__init__(url, formato, legenda)
        self.resolucao = resolucao

    def exibir_info(self) -> str:
        return (f"[Imagem]\nURL: {self.url}\nFormato: {self.formato}\nLegenda: {self.legenda}\n"
                f"Resolução: {self.resolucao}")


# Produto concreto: Vídeo
class Video(MidiaDigital):
    def __init__(self, url: str, formato: str, legenda: Optional[str] = None, duracao: str = "00:00"):
        super().__init__(url, formato, legenda)
        self.duracao = duracao

    def exibir_info(self) -> str:
        return (f"[Vídeo]\nURL: {self.url}\nFormato: {self.formato}\nLegenda: {self.legenda}\n"
                f"Duração: {self.duracao}")


# Fábrica abstrata
class MidiaFactory(ABC):
    @abstractmethod
    def criar_midia(self, url: str, formato: str, legenda: Optional[str] = None, **kwargs: Any) -> MidiaDigital:
        pass


# Fábrica concreta: Imagem
class ImagemFactory(MidiaFactory):
    def criar_midia(self, url: str, formato: str, legenda: Optional[str] = None, **kwargs: Any) -> Imagem:
        resolucao = kwargs.get("resolucao", "N/A")
        return Imagem(url, formato, legenda, resolucao=resolucao)


# Fábrica concreta: Vídeo
class VideoFactory(MidiaFactory):
    def criar_midia(self, url: str, formato: str, legenda: Optional[str] = None, **kwargs: Any) -> Video:
        duracao = kwargs.get("duracao", "00:00")
        return Video(url, formato, legenda, duracao=duracao)


# Gerenciador de Fábricas
class GerenciadorDeFabricasMidia:
    def __init__(self):
        self.fabricas = {
            "imagem": ImagemFactory(),
            "video": VideoFactory()
        }

    def get_factory(self, tipo: str) -> MidiaFactory:
        tipo = tipo.lower()
        if tipo in self.fabricas:
            return self.fabricas[tipo]
        raise ValueError(f"Fábrica para tipo '{tipo}' não encontrada.")


# --- Exemplo de Uso do Gerenciador ---
if __name__ == "__main__":
    gerenciador = GerenciadorDeFabricasMidia()

    # Cliente quer criar um vídeo
    try:
        fabrica_de_videos = gerenciador.get_factory("video")
        meu_video = fabrica_de_videos.criar_midia(
            url="http://example.com/filme.mp4",
            formato="MP4",
            legenda="Filme de Ação",
            duracao="01:45:30"
        )
        meu_video.exibir_detalhes()
    except ValueError as e:
        print(e)

    print("-" * 20)

    # Cliente quer criar uma imagem
    try:
        fabrica_de_imagens = gerenciador.get_factory("imagem")
        minha_imagem = fabrica_de_imagens.criar_midia(
            url="http://example.com/paisagem.jpg",
            formato="JPEG",
            legenda="Bela Paisagem",
            resolucao="4032x3024"
        )
        minha_imagem.exibir_detalhes()
    except ValueError as e:
        print(e)

    print("-" * 20)

    # Tentativa de obter uma fábrica para um tipo desconhecido
    try:
        fabrica_desconhecida = gerenciador.get_factory("audiobook")
    except ValueError as e:
        print(e)
