from abc import ABC, abstractmethod

# Classe base da estratégia
class Strategy(ABC):
    @abstractmethod
    def processar(self, midia):
        pass

# Estratégia para vídeo
class StrategyVideo(Strategy):
    def processar(self, midia):
        print("\n🎥 Processando vídeo:")
        print(f"📁 Arquivo: {midia.urlArquivo}")
        print(f"⏱️ Duração: {midia.duracao}")
        print(f"📝 Legenda: {midia.legenda}")
        print(f"📦 Formato: {midia.formato}")

# Estratégia para imagem
class StrategyImagem(Strategy):
    def processar(self, midia):
        print("\n🖼️ Processando imagem:")
        print(f"📁 Arquivo: {midia.urlArquivo}")
        print(f"📐 Resolução: {midia.resolucao}")
        print(f"🆎 Texto alternativo: {midia.textoAlternativo}")
        print(f"📝 Legenda: {midia.legenda}")
        print(f"📦 Formato: {midia.formato}")

# Classe base MidiaDigital
class MidiaDigital:
    def __init__(self, id: int, formato: str, legenda: str):
        self.id = id
        self.formato = formato
        self.legenda = legenda
        self.strategy: Strategy = None

    def set_strategy(self, strategy: Strategy):
        self.strategy = strategy

    def processar_midia(self):
        if self.strategy:
            self.strategy.processar(self)
        else:
            print("⚠️ Nenhuma estratégia definida para processamento.")

# Subclasse para vídeo
class Video(MidiaDigital):
    def __init__(self, id: int, formato: str, legenda: str, urlArquivo: str, duracao: str):
        super().__init__(id, formato, legenda)
        self.urlArquivo = urlArquivo
        self.duracao = duracao

# Subclasse para imagem
class Imagem(MidiaDigital):
    def __init__(self, id: int, formato: str, legenda: str, urlArquivo: str, textoAlternativo: str, resolucao: str):
        super().__init__(id, formato, legenda)
        self.urlArquivo = urlArquivo
        self.textoAlternativo = textoAlternativo
        self.resolucao = resolucao

# Exemplo de uso
if __name__ == "__main__":
    # Criando instâncias de mídias
    video1 = Video(1, "mp4", "Entrevista com artista", "video_entrevista.mp4", "05:30")
    imagem1 = Imagem(2, "png", "Cartaz do evento", "cartaz_evento.png", "Cartaz com detalhes", "1080x720")

    # Aplicando estratégias
    video1.set_strategy(StrategyVideo())
    imagem1.set_strategy(StrategyImagem())

    # Processando mídias
    video1.processar_midia()
    imagem1.processar_midia()
