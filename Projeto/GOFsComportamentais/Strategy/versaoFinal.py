from abc import ABC, abstractmethod
from typing import List, Optional
from datetime import datetime

# ===== STRATEGY INTERFACE =====

class ProcessamentoStrategy(ABC):
    """Interface Strategy para processamento de mídia"""
    
    @abstractmethod
    def processar(self) -> None:
        """Executa o processamento da mídia"""
        pass
    
    @abstractmethod
    def obter_formato(self) -> str:
        """Retorna o formato após processamento"""
        pass
    
    @abstractmethod
    def validar(self) -> bool:
        """Valida se a estratégia pode ser executada"""
        pass

# ===== CONCRETE STRATEGIES =====

class ProcessamentoVideo(ProcessamentoStrategy):
    """Estratégia concreta para processamento de vídeos"""
    
    def __init__(self, codec: str, qualidade: int):
        self.codec = codec
        self.qualidade = qualidade
    
    def processar(self) -> None:
        """Processa vídeo com codec e qualidade específicos"""
        print(f"🎬 Processando vídeo com codec {self.codec}")
        print(f"📺 Aplicando qualidade: {self.qualidade}p")
        print("🖼️  Gerando thumbnail...")
        print("🌐 Otimizando para streaming...")
        print("✅ Processamento de vídeo concluído!")
    
    def obter_formato(self) -> str:
        return f"MP4 - {self.codec} ({self.qualidade}p)"
    
    def validar(self) -> bool:
        return self.codec is not None and self.qualidade > 0

class ProcessamentoImagem(ProcessamentoStrategy):
    """Estratégia concreta para processamento de imagens"""
    
    def __init__(self, compressao: str, resolucao: str):
        self.compressao = compressao
        self.resolucao = resolucao
    
    def processar(self) -> None:
        """Processa imagem com compressão e resolução específicas"""
        print(f"🖼️  Processando imagem com compressão {self.compressao}")
        print(f"📏 Ajustando resolução para: {self.resolucao}")
        print("🗜️  Otimizando tamanho do arquivo...")
        print("📱 Gerando versões responsivas...")
        print("✅ Processamento de imagem concluído!")
    
    def obter_formato(self) -> str:
        return f"JPEG - {self.compressao} ({self.resolucao})"
    
    def validar(self) -> bool:
        return self.compressao is not None and self.resolucao is not None

class ProcessamentoWebOptimizado(ProcessamentoStrategy):
    """Estratégia para otimização web"""
    
    def __init__(self, formato_web: str = "WebP"):
        self.formato_web = formato_web
    
    def processar(self) -> None:
        """Otimiza mídia para web"""
        print(f"🌐 Otimizando para web em formato {self.formato_web}...")
        print("⚡ Reduzindo tamanho do arquivo...")
        print("🔄 Aplicando lazy loading...")
        print("📊 Gerando diferentes resoluções...")
        print("✅ Otimização web concluída!")
    
    def obter_formato(self) -> str:
        return f"{self.formato_web} Otimizado para Web"
    
    def validar(self) -> bool:
        return self.formato_web is not None

class ProcessamentoMobileOptimizado(ProcessamentoStrategy):
    """Estratégia para otimização mobile"""
    
    def processar(self) -> None:
        """Otimiza mídia para dispositivos móveis"""
        print("📱 Otimizando para dispositivos móveis...")
        print("🔋 Reduzindo consumo de bateria...")
        print("📶 Otimizando para conexões lentas...")
        print("✅ Otimização mobile concluída!")
    
    def obter_formato(self) -> str:
        return "Mobile Optimized"
    
    def validar(self) -> bool:
        return True

# ===== CONTEXT CLASS =====

class MidiaDigital(ABC):
    """Classe Context abstrata para mídia digital"""
    
    def __init__(self, id_midia: int, formato: str, legenda: str):
        self.id = id_midia
        self.formato = formato
        self.legenda = legenda
        self.data_criacao = datetime.now()
        self._strategy: Optional[ProcessamentoStrategy] = None
    
    def set_strategy(self, strategy: ProcessamentoStrategy) -> None:
        """Define a estratégia de processamento"""
        self._strategy = strategy
    
    def executar_processamento(self) -> None:
        """Executa o processamento usando a estratégia atual"""
        if self._strategy and self._strategy.validar():
            print(f"\n🚀 Iniciando processamento da mídia ID: {self.id}")
            print(f"📝 Legenda: {self.legenda}")
            print("-" * 50)
            
            self._strategy.processar()
            self.formato = self._strategy.obter_formato()
            
            print("-" * 50)
            print(f"✅ Processamento concluído!")
            print(f"📄 Novo formato: {self.formato}")
        else:
            print(f"❌ Estratégia inválida ou não definida para mídia ID: {self.id}")
    
    # Getters e Setters
    @property
    def strategy(self) -> Optional[ProcessamentoStrategy]:
        return self._strategy
    
    def __str__(self) -> str:
        return f"MidiaDigital(id={self.id}, formato={self.formato}, legenda='{self.legenda}')"

# ===== CONCRETE CONTEXTS =====

class Video(MidiaDigital):
    """Contexto concreto para vídeos"""
    
    def __init__(self, id_midia: int, formato: str, legenda: str, 
                 url_arquivo: str, duracao: int):
        super().__init__(id_midia, formato, legenda)
        self.url_arquivo = url_arquivo
        self.duracao = duracao
        
        # Estratégia padrão para vídeos
        self.set_strategy(ProcessamentoVideo("H.264", 1080))
    
    def reproduzir(self) -> None:
        """Reproduz o vídeo"""
        print(f"▶️  Reproduzindo vídeo: {self.url_arquivo}")
        print(f"⏱️  Duração: {self.duracao} segundos")
        print(f"🎬 Formato atual: {self.formato}")
    
    def __str__(self) -> str:
        return f"Video(id={self.id}, duracao={self.duracao}s, formato={self.formato})"

class Imagem(MidiaDigital):
    """Contexto concreto para imagens"""
    
    def __init__(self, id_midia: int, formato: str, legenda: str,
                 url_arquivo: str, texto_alternativo: str, resolucao: str):
        super().__init__(id_midia, formato, legenda)
        self.url_arquivo = url_arquivo
        self.texto_alternativo = texto_alternativo
        self.resolucao = resolucao
        
        # Estratégia padrão para imagens
        self.set_strategy(ProcessamentoImagem("Alta", "1920x1080"))
    
    def exibir(self) -> None:
        """Exibe informações da imagem"""
        print(f"🖼️  Exibindo imagem: {self.url_arquivo}")
        print(f"📝 Alt text: {self.texto_alternativo}")
        print(f"📏 Resolução: {self.resolucao}")
        print(f"🎨 Formato atual: {self.formato}")
    
    def __str__(self) -> str:
        return f"Imagem(id={self.id}, resolucao={self.resolucao}, formato={self.formato})"

# ===== ESTRATÉGIAS PARA MEMORIA (OPERAÇÕES DE COLEÇÃO) =====

class MemoriaStrategy(ABC):
    """Strategy para operações de coleção na Memoria"""
    
    @abstractmethod
    def organizar_midias(self, midias: List[MidiaDigital]) -> List[MidiaDigital]:
        pass
    
    @abstractmethod
    def buscar_midias(self, midias: List[MidiaDigital], criterio: str) -> List[MidiaDigital]:
        pass

class OrganizacaoPorTipo(MemoriaStrategy):
    """Organiza mídias por tipo"""
    
    def organizar_midias(self, midias: List[MidiaDigital]) -> List[MidiaDigital]:
        print("📁 Organizando por tipo de mídia...")
        return sorted(midias, key=lambda x: type(x).__name__)
    
    def buscar_midias(self, midias: List[MidiaDigital], criterio: str) -> List[MidiaDigital]:
        print(f"🔍 Buscando mídias do tipo: {criterio}")
        return [midia for midia in midias if type(midia).__name__.lower() == criterio.lower()]

class OrganizacaoPorData(MemoriaStrategy):
    """Organiza mídias por data de criação"""
    
    def organizar_midias(self, midias: List[MidiaDigital]) -> List[MidiaDigital]:
        print("📅 Organizando por data de criação...")
        return sorted(midias, key=lambda x: x.data_criacao, reverse=True)
    
    def buscar_midias(self, midias: List[MidiaDigital], criterio: str) -> List[MidiaDigital]:
        print(f"🔍 Buscando mídias por critério de data: {criterio}")
        # Implementação simplificada
        return midias

class Memoria:
    """Classe para gerenciar coleção de mídias"""
    
    def __init__(self):
        self._midias: List[MidiaDigital] = []
        self._organizacao_strategy: Optional[MemoriaStrategy] = None
    
    def set_organizacao_strategy(self, strategy: MemoriaStrategy) -> None:
        """Define estratégia de organização"""
        self._organizacao_strategy = strategy
    
    def adicionar_midia(self, midia: MidiaDigital) -> None:
        """Adiciona mídia à coleção"""
        self._midias.append(midia)
        print(f"➕ Mídia adicionada: {midia}")
    
    def organizar_midias(self) -> None:
        """Organiza mídias usando a estratégia atual"""
        if self._organizacao_strategy:
            self._midias = self._organizacao_strategy.organizar_midias(self._midias)
        else:
            print("⚠️  Nenhuma estratégia de organização definida")
    
    def buscar_midias(self, criterio: str) -> List[MidiaDigital]:
        """Busca mídias usando a estratégia atual"""
        if self._organizacao_strategy:
            return self._organizacao_strategy.buscar_midias(self._midias, criterio)
        return []
    
    def processar_todas_midias(self) -> None:
        """Processa todas as mídias (cada uma com sua estratégia)"""
        print("\n🔄 Processando todas as mídias...")
        for midia in self._midias:
            midia.executar_processamento()
    
    def listar_midias(self) -> None:
        """Lista todas as mídias"""
        print("\n📋 Lista de mídias:")
        for i, midia in enumerate(self._midias, 1):
            print(f"{i}. {midia}")
    
    @property
    def midias(self) -> List[MidiaDigital]:
        return self._midias.copy()

# ===== EXEMPLO DE USO =====

def exemplo_uso():
    """Demonstra o uso do padrão Strategy"""
    
    print("=" * 60)
    print("🎯 EXEMPLO DE USO DO PADRÃO STRATEGY")
    print("=" * 60)
    
    # Criando mídias com estratégias padrão
    video_hd = Video(1, "MP4", "Vídeo promocional da empresa", "promo.mp4", 120)
    video_4k = Video(2, "MP4", "Apresentação do produto", "produto.mp4", 300)
    imagem_logo = Imagem(3, "PNG", "Logo da empresa", "logo.png", "Logo oficial", "1920x1080")
    imagem_banner = Imagem(4, "JPEG", "Banner do site", "banner.jpg", "Banner principal", "1920x600")
    
    # Criando memória e definindo estratégia de organização
    memoria = Memoria()
    memoria.set_organizacao_strategy(OrganizacaoPorTipo())
    
    # Adicionando mídias
    memoria.adicionar_midia(video_hd)
    memoria.adicionar_midia(video_4k)
    memoria.adicionar_midia(imagem_logo)
    memoria.adicionar_midia(imagem_banner)
    
    print("\n" + "=" * 60)
    print("📋 PROCESSAMENTO COM ESTRATÉGIAS PADRÃO")
    print("=" * 60)
    
    # Processamento com estratégias padrão
    memoria.processar_todas_midias()
    
    print("\n" + "=" * 60)
    print("🔄 MUDANDO ESTRATÉGIAS DINAMICAMENTE")
    print("=" * 60)
    
    # Mudando estratégias
    video_4k.set_strategy(ProcessamentoVideo("H.265", 2160))  # 4K
    imagem_logo.set_strategy(ProcessamentoWebOptimizado("WebP"))
    imagem_banner.set_strategy(ProcessamentoMobileOptimizado())
    
    # Processamento com novas estratégias
    video_4k.executar_processamento()
    imagem_logo.executar_processamento()
    imagem_banner.executar_processamento()
    
    print("\n" + "=" * 60)
    print("📁 ORGANIZANDO MÍDIAS")
    print("=" * 60)
    
    # Organizando mídias
    memoria.organizar_midias()
    memoria.listar_midias()
    
    # Buscando mídias específicas
    videos = memoria.buscar_midias("Video")
    print(f"\n🎬 Vídeos encontrados: {len(videos)}")
    
    print("\n" + "=" * 60)
    print("▶️ REPRODUZINDO CONTEÚDO")
    print("=" * 60)
    
    # Reproduzindo/exibindo conteúdo
    video_hd.reproduzir()
    print()
    imagem_logo.exibir()
    
    print("\n" + "=" * 60)
    print("🔄 MUDANDO ESTRATÉGIA DE ORGANIZAÇÃO")
    print("=" * 60)
    
    # Mudando estratégia de organização
    memoria.set_organizacao_strategy(OrganizacaoPorData())
    memoria.organizar_midias()
    memoria.listar_midias()

def exemplo_extensibilidade():
    """Demonstra como estender o sistema com novas estratégias"""
    
    print("\n" + "=" * 60)
    print("🚀 DEMONSTRAÇÃO DE EXTENSIBILIDADE")
    print("=" * 60)
    
    # Nova estratégia personalizada
    class ProcessamentoHDR(ProcessamentoStrategy):
        def processar(self):
            print("🌈 Aplicando processamento HDR...")
            print("🎨 Aumentando gama de cores...")
            print("✨ Melhorando contraste...")
        
        def obter_formato(self):
            return "HDR Enhanced"
        
        def validar(self):
            return True
    
    # Usando nova estratégia
    video_especial = Video(99, "MP4", "Vídeo HDR", "hdr.mp4", 180)
    video_especial.set_strategy(ProcessamentoHDR())
    video_especial.executar_processamento()

if __name__ == "__main__":
    exemplo_uso()
    exemplo_extensibilidade()
    
    print("\n" + "=" * 60)
    print("✅ EXEMPLO CONCLUÍDO!")
    print("=" * 60)