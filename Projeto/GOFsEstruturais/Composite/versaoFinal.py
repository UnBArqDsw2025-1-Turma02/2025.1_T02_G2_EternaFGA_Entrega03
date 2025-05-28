from abc import ABC, abstractmethod
from datetime import date
from typing import List

# Classe base (Componente)
class MidiaDigital(ABC):
    def __init__(self, formato: str, legenda: str):
        self.formato = formato
        self.legenda = legenda

    @abstractmethod
    def exibir(self):
        pass

# Leaf: Vídeo
class Video(MidiaDigital):
    def __init__(self, formato: str, legenda: str, urlArquivo: str, duracao: str):
        super().__init__(formato, legenda)
        self.urlArquivo = urlArquivo
        self.duracao = duracao

    def exibir(self):
        print(f"[Vídeo] URL: {self.urlArquivo}, Duração: {self.duracao}, Legenda: {self.legenda}, Formato: {self.formato}")

# Leaf: Imagem
class Imagem(MidiaDigital):
    def __init__(self, formato: str, legenda: str, urlArquivo: str, textoAlternativo: str, resolucao: str):
        super().__init__(formato, legenda)
        self.urlArquivo = urlArquivo
        self.textoAlternativo = textoAlternativo
        self.resolucao = resolucao

    def exibir(self):
        print(f"[Imagem] URL: {self.urlArquivo}, Resolução: {self.resolucao}, Texto Alt: {self.textoAlternativo}, Legenda: {self.legenda}")

# Composite: Memória
class Memoria:
    def __init__(self, id: int, titulo: str, legenda: str, status: str, autor: str, dataEnvio: date):
        self.id = id
        self.titulo = titulo
        self.legenda = legenda
        self.status = status
        self.autor = autor
        self.dataEnvio = dataEnvio
        self.midias: List[MidiaDigital] = []
        self.tags = []

    def addMidiaDigital(self, midia: MidiaDigital):
        self.midias.append(midia)

    def removerMidiaDigital(self, midia: MidiaDigital):
        self.midias.remove(midia)

    def adicionarTag(self, tag: str):
        self.tags.append(tag)

    def exibir(self):
        print(f"\nMemória: {self.titulo} (ID: {self.id})")
        print(f"Legenda: {self.legenda}, Status: {self.status}, Autor: {self.autor}, Data: {self.dataEnvio}")
        print("Tags:", ", ".join(self.tags))
        print("Mídias associadas:")
        for midia in self.midias:
            midia.exibir()

# Execução exemplo
if __name__ == "__main__":
    video1 = Video("mp4", "Entrevista", "https://exemplo.com/video.mp4", "2min")
    imagem1 = Imagem("jpg", "Foto da reunião", "https://exemplo.com/imagem.jpg", "Reunião com a equipe", "1920x1080")

    memoria = Memoria(1, "Reunião de equipe", "Memória da reunião de planejamento", "finalizada", "Joana", date.today())
    memoria.addMidiaDigital(video1)
    memoria.addMidiaDigital(imagem1)
    memoria.adicionarTag("reunião")
    memoria.adicionarTag("planejamento")
    memoria.exibir()
