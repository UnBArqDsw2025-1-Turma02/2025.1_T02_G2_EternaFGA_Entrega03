from abc import ABC, abstractmethod
from typing import List

# Classe base abstrata
class MidiaDigital(ABC):
    """
    Classe base abstrata para todos os tipos de mídia digital.
    Conforme o diagrama, assume-se que toda mídia digital tem uma urlArquivo.
    """
    def __init__(self, urlArquivo: str):
        self.urlArquivo = urlArquivo

    @abstractmethod
    def mostrar(self):
        """
        Método abstrato para exibir as informações da mídia.
        As classes filhas devem implementar este método.
        """
        pass

# Classe Imagem (Folha)
class Imagem(MidiaDigital):
    """
    Representa uma mídia digital do tipo Imagem.
    Herda de MidiaDigital e adiciona atributos específicos de imagem.
    """
    def __init__(self, urlArquivo: str, textoAlternativo: str, resolucao: str):
        super().__init__(urlArquivo)
        self.textoAlternativo = textoAlternativo
        self.resolucao = resolucao

    def mostrar(self):
        """Exibe os detalhes da imagem."""
        print(f"[Imagem] URL: {self.urlArquivo}, Texto Alternativo: {self.textoAlternativo}, Resolução: {self.resolucao}")

# Classe Video (Folha)
class Video(MidiaDigital):
    """
    Representa uma mídia digital do tipo Vídeo.
    Herda de MidiaDigital e adiciona atributos específicos de vídeo.
    """
    def __init__(self, urlArquivo: str, duracao: str):
        super().__init__(urlArquivo)
        self.duracao = duracao # Específico para Video

    def mostrar(self):
        """Exibe os detalhes do vídeo."""
        print(f"[Vídeo]  URL: {self.urlArquivo}, Duração: {self.duracao}")

# Classe Composite
class CompositeMidia(MidiaDigital):
    """
    Representa uma coleção de mídias digitais (componentes).
    Pode conter tanto mídias individuais (Imagem, Video) quanto outras coleções (CompositeMidia).
    Herda de MidiaDigital, possuindo uma urlArquivo que pode representar, por exemplo,
    uma miniatura ou ícone para a coleção.
    """
    def __init__(self, titulo: str, urlArquivo_composite: str):
        super().__init__(urlArquivo_composite) # URL para o composite em si (ex: thumbnail da galeria)
        self.titulo = titulo
        self.componentes: List[MidiaDigital] = []

    def adicionar(self, midia: MidiaDigital):
        """Adiciona uma mídia (folha ou outro composite) à coleção."""
        self.componentes.append(midia)
        print(f"Adicionado à composite '{self.titulo}': {type(midia).__name__} (URL: {midia.urlArquivo})")


    def remover(self, midia: MidiaDigital):
        """Remove uma mídia da coleção."""
        try:
            self.componentes.remove(midia)
            print(f"Removido da composite '{self.titulo}': {type(midia).__name__} (URL: {midia.urlArquivo})")
        except ValueError:
            print(f"Erro: Mídia não encontrada na composite '{self.titulo}' para remoção.")


    def mostrar(self):
        """
        Implementação do método abstrato mostrar.
        Exibe informações sobre o próprio composite (metadados da coleção).
        """
        print(f"[Composite] Título: '{self.titulo}', URL Representativa: {self.urlArquivo}")

    def exibir(self):
        """
        Método específico do CompositeMidia (conforme diagrama) para exibir
        as informações de todos os seus componentes.
        """
        print(f"\n--- Conteúdo do Composite '{self.titulo}' ---")
        if not self.componentes:
            print("  (Esta coleção está vazia)")
        for componente in self.componentes:
            componente.mostrar() # Chama o método mostrar de cada componente
        print(f"--- Fim do Composite '{self.titulo}' ---\n")

# Execução de exemplo adaptada à nova estrutura
if __name__ == "__main__":
    # Criando mídias individuais
    imagem1 = Imagem(urlArquivo="https://exemplo.com/img1.jpg", textoAlternativo="Palco do evento", resolucao="1920x1080")
    video1 = Video(urlArquivo="https://exemplo.com/video1.mp4", duracao="3min")

    # Exibindo mídias individuais
    print("--- Mídias Individuais ---")
    imagem1.mostrar()
    video1.mostrar()
    print("------------------------\n")

    # Criando composite principal (Galeria)
    # Para urlArquivo_composite, podemos usar um placeholder se não houver uma URL específica para a galeria
    galeria_principal = CompositeMidia(titulo="Galeria Principal do Evento", urlArquivo_composite="https://exemplo.com/galeria_thumb.jpg")
    galeria_principal.mostrar() # Mostrar informações da própria galeria

    # Adicionando mídias à galeria principal
    galeria_principal.adicionar(imagem1)
    galeria_principal.adicionar(video1)

    # Criando outro composite (Subgaleria de Vídeos)
    video2 = Video(urlArquivo="https://exemplo.com/video2.avi", duracao="5min")
    video3 = Video(urlArquivo="https://exemplo.com/video3.mkv", duracao="10min")

    subgaleria_videos = CompositeMidia(titulo="Vídeos Extras da Apresentação", urlArquivo_composite="https://exemplo.com/subgaleria_thumb.jpg")
    subgaleria_videos.mostrar() # Mostrar informações da subgaleria

    subgaleria_videos.adicionar(video2)
    subgaleria_videos.adicionar(video3)

    # Adicionando a subgaleria à galeria principal
    galeria_principal.adicionar(subgaleria_videos)

    print("\n--- Exibindo Galeria Principal (chamando mostrar() nos filhos) ---")
    galeria_principal.exibir()

    # Para uma exibição que também "expande" os composites filhos usando seus métodos "exibir":
    print("\n--- Exibição Detalhada da Galeria Principal (com 'exibir' para sub-composites) ---")
    galeria_principal.mostrar() # Info da galeria principal
    print(f"--- Conteúdo Detalhado do Composite '{galeria_principal.titulo}' ---")
    for item in galeria_principal.componentes:
        if isinstance(item, CompositeMidia):
            item.exibir() # Se for composite, chama exibir() para ver seus filhos
        else:
            item.mostrar() # Se for folha, chama mostrar()
    print(f"--- Fim do Conteúdo Detalhado do Composite '{galeria_principal.titulo}' ---")

