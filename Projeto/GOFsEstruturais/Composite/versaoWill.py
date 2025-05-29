from abc import ABC, abstractmethod
from typing import List

# Classe base abstrata
class MidiaDigital(ABC):
    def __init__(self, id: int, formato: str, legenda: str):
        self.id = id
        self.formato = formato
        self.legenda = legenda

    @abstractmethod
    def exibir(self):
        pass

# Classe Imagem (Folha)
class Imagem(MidiaDigital):
    def __init__(self, id: int, formato: str, legenda: str, urlArquivo: str, textoAlternativo: str, resolucao: str):
        super().__init__(id, formato, legenda)
        self.urlArquivo = urlArquivo
        self.textoAlternativo = textoAlternativo
        self.resolucao = resolucao

    def exibir(self):
        print(f"[Imagem] ID: {self.id}, Formato: {self.formato}, Legenda: {self.legenda}")
        print(f"         URL: {self.urlArquivo}, Texto Alt: {self.textoAlternativo}, Resolução: {self.resolucao}")

# Classe Video (Folha)
class Video(MidiaDigital):
    def __init__(self, id: int, formato: str, legenda: str, urlArquivo: str, duracao: str):
        super().__init__(id, formato, legenda)
        self.urlArquivo = urlArquivo
        self.duracao = duracao

    def exibir(self):
        print(f"[Vídeo]  ID: {self.id}, Formato: {self.formato}, Legenda: {self.legenda}")
        print(f"         URL: {self.urlArquivo}, Duração: {self.duracao}")

# Classe Composite
class CompositeMedia(MidiaDigital):
    def __init__(self, id: int, formato: str, legenda: str):
        super().__init__(id, formato, legenda)
        self.componentes: List[MidiaDigital] = []

    def adicionar(self, midia: MidiaDigital):
        self.componentes.append(midia)

    def remover(self, midia: MidiaDigital):
        self.componentes.remove(midia)

    def exibir(self):
        print(f"[CompositeMedia] ID: {self.id}, Formato: {self.formato}, Legenda: {self.legenda}")
        print(" Componentes:")
        for componente in self.componentes:
            componente.exibir()

# Execução de exemplo
if __name__ == "__main__":
    # Criando mídias individuais
    imagem1 = Imagem(1, "jpg", "Foto do evento", "https://exemplo.com/img1.jpg", "Imagem de um palco", "1920x1080")
    video1 = Video(2, "mp4", "Vídeo da entrevista", "https://exemplo.com/video1.mp4", "3min")

    # Criando composite
    galeria = CompositeMedia(10, "composto", "Galeria do evento")
    galeria.adicionar(imagem1)
    galeria.adicionar(video1)

    # Criando outro composite dentro do primeiro (exemplo de hierarquia)
    video2 = Video(3, "avi", "Apresentação musical", "https://exemplo.com/video2.avi", "5min")
    subgaleria = CompositeMedia(11, "composto", "Vídeos extras")
    subgaleria.adicionar(video2)

    galeria.adicionar(subgaleria)

    # Exibir todos os conteúdos da galeria
    galeria.exibir()
