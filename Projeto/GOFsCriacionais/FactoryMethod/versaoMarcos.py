from abc import ABC, abstractmethod
from typing import Optional, Any, Dict

# --- Produto Abstrato ---
class MidiaDigital(ABC):
    """
    Classe base abstrata para todos os tipos de mídia digital.
    Define a interface comum.
    """
    def __init__(self, url: str, formato: str, legenda: Optional[str] = None):
        self.url = url
        self.formato = formato
        self.legenda = legenda if legenda else "Mídia sem legenda"

    @abstractmethod
    def exibir_detalhes(self) -> None:
        """
        Método abstrato para exibir os detalhes específicos da mídia.
        As subclasses concretas devem implementar este método.
        """
        print(f"URL: {self.url}")
        print(f"Formato: {self.formato}")
        print(f"Legenda: {self.legenda}")

# --- Produtos Concretos ---
class Video(MidiaDigital):
    """
    Representa um arquivo de vídeo, um tipo de MidiaDigital.
    """
    def __init__(self, url: str, formato: str, legenda: Optional[str] = None, duracao: str = "00:00"):
        super().__init__(url, formato, legenda)
        self.duracao = duracao # Atributo específico do vídeo

    def exibir_detalhes(self) -> None:
        print("--- Detalhes do Vídeo ---")
        super().exibir_detalhes()
        print(f"Duração: {self.duracao}")
        print("-------------------------")

class Imagem(MidiaDigital):
    """
    Representa um arquivo de imagem, um tipo de MidiaDigital.
    """
    def __init__(self, url: str, formato: str, legenda: Optional[str] = None, resolucao: str = "N/A"):
        super().__init__(url, formato, legenda)
        self.resolucao = resolucao # Atributo específico da imagem

    def exibir_detalhes(self) -> None:
        print("--- Detalhes da Imagem ---")
        super().exibir_detalhes()
        print(f"Resolução: {self.resolucao}")
        print("--------------------------")

# --- Fábrica Abstrata (Creator Abstrato) ---
class AbstractMidiaFactory(ABC):
    """
    Interface abstrata para as fábricas de MidiaDigital.
    Define o Factory Method 'criar_midia'.
    """
    @abstractmethod
    def criar_midia(self, url: str, formato: str, legenda: Optional[str] = None, **kwargs: Any) -> MidiaDigital:
        """
        Factory Method: As subclasses concretas implementarão este método
        para criar um tipo específico de MidiaDigital.
        """
        pass

# --- Fábricas Concretas (Concrete Creators) ---
class VideoFactory(AbstractMidiaFactory):
    """
    Fábrica concreta para criar objetos Video.
    """
    def criar_midia(self, url: str, formato: str, legenda: Optional[str] = None, **kwargs: Any) -> Video:
        duracao = kwargs.get("duracao", "00:00")
        return Video(url, formato, legenda, duracao=duracao)

class ImagemFactory(AbstractMidiaFactory):
    """
    Fábrica concreta para criar objetos Imagem.
    """
    def criar_midia(self, url: str, formato: str, legenda: Optional[str] = None, **kwargs: Any) -> Imagem:
        resolucao = kwargs.get("resolucao", "N/A")
        return Imagem(url, formato, legenda, resolucao=resolucao)
    
# --- Gerenciador de Fábricas ---
class GerenciadorDeFabricasMidia:
    """
    Gerencia e fornece acesso às fábricas de mídia concretas.
    """
    def __init__(self):
        self._fabricas_registradas: Dict[str, AbstractMidiaFactory] = {}
        self._registrar_fabricas_padrao()

    def _registrar_fabricas_padrao(self):
        """Registra as fábricas conhecidas no sistema."""
        self.registrar_fabrica("video", VideoFactory())
        self.registrar_fabrica("imagem", ImagemFactory())
        # Se você adicionar AudioFactory, registraria aqui também:
        # self.registrar_fabrica("audio", AudioFactory())

    def registrar_fabrica(self, tipo_midia: str, fabrica: AbstractMidiaFactory):
        """
        Permite registrar uma nova fábrica para um tipo de mídia.
        Args:
            tipo_midia (str): A chave identificadora para o tipo de mídia (ex: "video").
            fabrica (AbstractMidiaFactory): A instância da fábrica concreta.
        """
        self._fabricas_registradas[tipo_midia.lower()] = fabrica

    def get_factory(self, tipo_midia: str) -> Optional[AbstractMidiaFactory]:
        """
        Retorna a fábrica para um tipo de mídia específico.

        Args:
            tipo_midia (str): O tipo de mídia para o qual a fábrica é desejada (ex: "video", "imagem").

        Returns:
            Optional[AbstractMidiaFactory]: A instância da fábrica se encontrada, ou None caso contrário.
                                            Pode também levantar um erro se preferir (como no seu exemplo).
        """
        fabrica = self._fabricas_registradas.get(tipo_midia.lower())
        if not fabrica:
            # Opção 1: Retornar None e deixar o cliente tratar
            # print(f"Aviso: Fábrica para o tipo de mídia '{tipo_midia}' não encontrada.")
            # return None
            # Opção 2: Levantar um erro (como no seu exemplo)
            raise ValueError(f"Fábrica para o tipo de mídia '{tipo_midia}' não encontrada.")
        return fabrica

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
        # ...
    except ValueError as e:
        print(e) 