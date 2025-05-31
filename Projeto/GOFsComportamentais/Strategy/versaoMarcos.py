from abc import ABC, abstractmethod

# 1. Interface da Estratégia
class EstrategiaDeReproducao(ABC):
    @abstractmethod
    def reproduzir(self, midia):
        pass

# 2. Estratégia Nula (Default)
class StrategyNula(EstrategiaDeReproducao):
    def reproduzir(self, midia):
        print("Nenhuma estratégia definida para reprodução.")

# 3. Estratégias Concretas
class StrategyVideo(EstrategiaDeReproducao):
    def reproduzir(self, midia):
        if not isinstance(midia, Video):
            print("StrategyVideo: Tipo de mídia incompatível.")
            return
        print(f"--- Estratégia Vídeo ---")
        print(f"Iniciando reprodução de VÍDEO:")
        print(f"  Arquivo: {midia.url_arquivo}")
        print(f"  Formato: {midia.formato}")
        print(f"  Duração: {midia.duracao} segundos")
        print(f"  Legenda: {midia.legenda or 'N/A'}")
        print(f"------------------------")

class StrategyImagem(EstrategiaDeReproducao):
    def reproduzir(self, midia):
        if not isinstance(midia, Imagem):
            print("StrategyImagem: Tipo de mídia incompatível.")
            return
        print(f"--- Estratégia Imagem ---")
        print(f"Exibindo IMAGEM:")
        print(f"  Arquivo: {midia.url_arquivo}")
        print(f"  Formato: {midia.formato}")
        print(f"  Resolução: {midia.resolucao}")
        print(f"  Texto Alternativo: {midia.texto_alternativo}")
        print(f"  Legenda: {midia.legenda or 'N/A'}")
        print(f"-------------------------")

class StrategyVideoLeve(EstrategiaDeReproducao):
    def reproduzir(self, midia):
        if not isinstance(midia, Video):
            print("StrategyVideoLeve: Tipo de mídia incompatível.")
            return
        print(f"--- Estratégia Vídeo Leve ---")
        print(f"Reproduzindo VÍDEO (versão leve) de: {midia.url_arquivo}")
        print(f"Qualidade reduzida para economizar banda.")
        print(f"-----------------------------")

# 4. Contexto e Subclasses
class MidiaDigital(ABC):
    def __init__(self, url_arquivo: str, formato: str, legenda: str = None, estrategia: EstrategiaDeReproducao = None):
        self.url_arquivo = url_arquivo
        self.formato = formato
        self.legenda = legenda
        self._estrategia = estrategia if estrategia else StrategyNula()

    def set_estrategia_reproducao(self, estrategia: EstrategiaDeReproducao):
        self._estrategia = estrategia

    def executar_reproducao(self):
        self._estrategia.reproduzir(self)

class Video(MidiaDigital):
    def __init__(self, url_arquivo: str, formato: str, duracao: int, legenda: str = None, estrategia: EstrategiaDeReproducao = None):
        super().__init__(url_arquivo, formato, legenda, estrategia if estrategia else StrategyVideo())
        self.duracao = duracao

class Imagem(MidiaDigital):
    def __init__(self, url_arquivo: str, formato: str, texto_alternativo: str, resolucao: str, legenda: str = None, estrategia: EstrategiaDeReproducao = None):
        super().__init__(url_arquivo, formato, legenda, estrategia if estrategia else StrategyImagem())
        self.texto_alternativo = texto_alternativo
        self.resolucao = resolucao

# 5. Exemplo de Uso
if __name__ == "__main__":
    meu_video = Video(
        url_arquivo="filme_legal.mp4",
        formato="MP4",
        duracao=7200,
        legenda="Um épico de aventura."
    )

    minha_imagem = Imagem(
        url_arquivo="paisagem_bonita.jpg",
        formato="JPEG",
        texto_alternativo="Montanhas ao pôr do sol.",
        resolucao="1920x1080",
        legenda="Foto tirada nas férias."
    )

    print("Executando com estratégias padrão:")
    meu_video.executar_reproducao()
    minha_imagem.executar_reproducao()

    print("\n--- Demonstração de troca de estratégia ---")
    estrategia_video_leve = StrategyVideoLeve()
    meu_video.set_estrategia_reproducao(estrategia_video_leve)
    print("\nExecutando vídeo com nova estratégia (Leve):")
    meu_video.executar_reproducao()

    print("\nTentando usar estratégia de imagem em um vídeo:")
    estrategia_so_para_imagem = StrategyImagem()
    meu_video.set_estrategia_reproducao(estrategia_so_para_imagem)
    meu_video.executar_reproducao()
