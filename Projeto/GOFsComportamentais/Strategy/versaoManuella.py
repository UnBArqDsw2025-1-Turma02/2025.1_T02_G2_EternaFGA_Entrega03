from abc import ABC, abstractmethod
from datetime import date
from typing import List

# Interface da Estratégia
class ExibicaoStrategy(ABC):
    @abstractmethod
    def exibir(self, midia):
        pass

# Estratégia para exibir imagens
class ExibicaoImagem(ExibicaoStrategy):
    def exibir(self, midia):
        print("\n🖼️ [Imagem]")
        print(f"┌────────────────────────────┐")
        print(f"| URL: {midia.urlArquivo}")
        print(f"| Resolução: {midia.resolucao}")
        print(f"| Texto Alt: {midia.textoAlternativo}")
        print(f"| Legenda: {midia.legenda}")
        print(f"└────────────────────────────┘")

# Estratégia para exibir vídeos
class ExibicaoVideo(ExibicaoStrategy):
    def exibir(self, midia):
        print("\n🎬 [Vídeo]")
        print("▶️ Reprodução de vídeo")
        print(f"🎞️ URL: {midia.urlArquivo}")
        print(f"⏱️ Duração: {midia.duracao}")
        print(f"📝 Legenda: {midia.legenda}")
        print(f"📁 Formato: {midia.formato}")

# Classe base para mídia digital
class MidiaDigital:
    def __init__(self, formato: str, legenda: str):
        self.formato = formato
        self.legenda = legenda
        self._estrategia_exibicao: ExibicaoStrategy = None

    def set_exibicao_strategy(self, estrategia: ExibicaoStrategy):
        self._estrategia_exibicao = estrategia

    def exibir(self):
        if self._estrategia_exibicao:
            self._estrategia_exibicao.exibir(self)
        else:
            print("⚠️ Estratégia de exibição não definida.")

# Classe concreta: Vídeo
class Video(MidiaDigital):
    def __init__(self, formato: str, legenda: str, urlArquivo: str, duracao: str):
        super().__init__(formato, legenda)
        self.urlArquivo = urlArquivo
        self.duracao = duracao

# Classe concreta: Imagem
class Imagem(MidiaDigital):
    def __init__(self, formato: str, legenda: str, urlArquivo: str, textoAlternativo: str, resolucao: str):
        super().__init__(formato, legenda)
        self.urlArquivo = urlArquivo
        self.textoAlternativo = textoAlternativo
        self.resolucao = resolucao

# Classe que compõe as mídias: Memória
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
        print(f"\n📚 Memória: {self.titulo} (ID: {self.id})")
        print(f"📝 Legenda: {self.legenda}")
        print(f"🔖 Status: {self.status}")
        print(f"✍️ Autor: {self.autor}")
        print(f"📅 Data: {self.dataEnvio}")
        print("🏷️ Tags:", ", ".join(self.tags))
        print("📂 Mídias associadas:")
        for midia in self.midias:
            midia.exibir()

# Execução de exemplo
if __name__ == "__main__":
    # Criando mídias
    img = Imagem("jpg", "Foto da paisagem", "paisagem.jpg", "Descrição da paisagem", "1920x1080")
    vid = Video("mp4", "Vídeo da festa", "festa.mp4", "02:30")

    # Atribuindo estratégias
    img.set_exibicao_strategy(ExibicaoImagem())
    vid.set_exibicao_strategy(ExibicaoVideo())

    # Criando memória
    memoria = Memoria(1, "Viagem à praia", "Momentos incríveis", "público", "Ana", date.today())
    memoria.addMidiaDigital(img)
    memoria.addMidiaDigital(vid)
    memoria.adicionarTag("praia")
    memoria.adicionarTag("férias")

    # Exibindo
    memoria.exibir()
