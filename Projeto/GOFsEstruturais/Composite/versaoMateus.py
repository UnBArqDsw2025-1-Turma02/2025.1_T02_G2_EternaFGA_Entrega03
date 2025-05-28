from abc import ABC, abstractmethod
from typing import Optional, List

#Componente base 
class MidiaDigital(ABC):
    def __init__(self, url: str, formato: str, legenda: Optional[str] = None):
        self.url = url
        self.formato = formato
        self.legenda = legenda if legenda else "Mídia sem legenda"
        
    @abstractmethod
    def exibir(self):
        pass

# Folhas
class Video(MidiaDigital):
    def __init__(self, url: str, formato: str, duracao: str, legenda: Optional[str] = None):
        super().__init__(url, formato, legenda)
        self.duracao = duracao

    def exibir(self):
        print(f"Vídeo: {self.url} | Formato: {self.formato} | Duração: {self.duracao} | Legenda: {self.legenda}")

class Imagem(MidiaDigital):
    def __init__(self, url: str, formato: str, resolucao: str, legenda: Optional[str] = None):
        super().__init__(url, formato, legenda)
        self.resolucao = resolucao

    def exibir(self):
        print(f"Imagem: {self.url} | Formato: {self.formato} | Resolução: {self.resolucao} | Legenda: {self.legenda}")

# Composite
class CompositeMidia(MidiaDigital):
    def __init__(self, nome: str):
        super().__init__(url="", formato="colecao", legenda=nome)
        self.componentes: List[MidiaDigital] = []

    def adicionar(self, midia: MidiaDigital):
        self.componentes.append(midia)

    def remover(self, midia: MidiaDigital):
        self.componentes.remove(midia)

    def exibir(self):
        print(f"Coleção: {self.legenda}")
        for componente in self.componentes:
            componente.exibir()

if __name__ == "__main__":
    video1 = Video("aula1.mp4", "mp4", "10:00", "Aula 1")
    imagem1 = Imagem("slide1.png", "png", "Slide 1", "1024x768")

    colecao_principal = CompositeMidia("Aula de Arquitetura")
    colecao_principal.adicionar(video1)
    colecao_principal.adicionar(imagem1)
    colecao_principal.exibir()