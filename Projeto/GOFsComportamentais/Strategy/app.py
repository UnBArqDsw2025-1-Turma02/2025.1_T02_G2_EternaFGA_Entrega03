from flask import Flask, render_template, request, redirect, url_for, flash
from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Callable
from datetime import datetime

# ===== STRATEGY INTERFACE (Processamento) =====
class ProcessamentoStrategy(ABC):
    @abstractmethod
    def processar(self) -> List[str]: # Modificado para retornar logs
        pass
    @abstractmethod
    def obter_formato(self) -> str:
        pass
    @abstractmethod
    def validar(self) -> bool:
        pass
    def __str__(self) -> str: # Adicionado para melhor display na UI
        return self.__class__.__name__

# ===== CONCRETE STRATEGIES (Processamento) =====
class ProcessamentoVideo(ProcessamentoStrategy):
    def __init__(self, codec: str, qualidade: int):
        self.codec = codec
        self.qualidade = qualidade
    def processar(self) -> List[str]:
        return [
            f"🎬 Processando vídeo com codec {self.codec}",
            f"📺 Aplicando qualidade: {self.qualidade}p",
            "🖼️  Gerando thumbnail...",
            "🌐 Otimizando para streaming...",
            "✅ Processamento de vídeo concluído!"
        ]
    def obter_formato(self) -> str:
        return f"MP4 - {self.codec} ({self.qualidade}p)"
    def validar(self) -> bool:
        return self.codec is not None and self.qualidade > 0
    def __str__(self) -> str:
        return f"Vídeo Padrão ({self.codec}, {self.qualidade}p)"

class ProcessamentoImagem(ProcessamentoStrategy):
    def __init__(self, compressao: str, resolucao: str):
        self.compressao = compressao
        self.resolucao = resolucao
    def processar(self) -> List[str]:
        return [
            f"🖼️  Processando imagem com compressão {self.compressao}",
            f"📏 Ajustando resolução para: {self.resolucao}",
            "🗜️  Otimizando tamanho do arquivo...",
            "📱 Gerando versões responsivas...",
            "✅ Processamento de imagem concluído!"
        ]
    def obter_formato(self) -> str:
        return f"JPEG - {self.compressao} ({self.resolucao})"
    def validar(self) -> bool:
        return self.compressao is not None and self.resolucao is not None
    def __str__(self) -> str:
        return f"Imagem Padrão ({self.compressao}, {self.resolucao})"

class ProcessamentoWebOptimizado(ProcessamentoStrategy):
    def __init__(self, formato_web: str = "WebP"):
        self.formato_web = formato_web
    def processar(self) -> List[str]:
        return [
            f"🌐 Otimizando para web em formato {self.formato_web}...",
            "⚡ Reduzindo tamanho do arquivo...",
            "🔄 Aplicando lazy loading...",
            "📊 Gerando diferentes resoluções...",
            "✅ Otimização web concluída!"
        ]
    def obter_formato(self) -> str:
        return f"{self.formato_web} Otimizado para Web"
    def validar(self) -> bool:
        return self.formato_web is not None
    def __str__(self) -> str:
        return f"Otimização Web ({self.formato_web})"

class ProcessamentoMobileOptimizado(ProcessamentoStrategy):
    def processar(self) -> List[str]:
        return [
            "📱 Otimizando para dispositivos móveis...",
            "🔋 Reduzindo consumo de bateria...",
            "📶 Otimizando para conexões lentas...",
            "✅ Otimização mobile concluída!"
        ]
    def obter_formato(self) -> str:
        return "Mobile Optimized"
    def validar(self) -> bool:
        return True
    def __str__(self) -> str:
        return "Otimização Mobile"

# ===== CONTEXT CLASS (MidiaDigital) =====
class MidiaDigital(ABC):
    def __init__(self, id_midia: int, formato_original: str, legenda: str):
        self.id = id_midia
        self.formato_original = formato_original # Guardar o original
        self.formato_atual = formato_original # Começa com o original
        self.legenda = legenda
        self.data_criacao = datetime.now()
        self._strategy: Optional[ProcessamentoStrategy] = None
        self.logs_processamento: List[str] = []

    def set_strategy(self, strategy: ProcessamentoStrategy) -> None:
        self._strategy = strategy

    def executar_processamento(self) -> None:
        self.logs_processamento = [] # Limpa logs anteriores desta mídia
        if self._strategy and self._strategy.validar():
            self.logs_processamento.append(f"🚀 Iniciando processamento da mídia ID: {self.id} ('{self.legenda}')")
            self.logs_processamento.append(f"🎞️ Formato antes: {self.formato_atual}")
            self.logs_processamento.append(f"🛠️ Usando estratégia: {self._strategy}")
            self.logs_processamento.append("-" * 30)
            
            msgs_strategy = self._strategy.processar()
            self.logs_processamento.extend(msgs_strategy)
            self.formato_atual = self._strategy.obter_formato()
            
            self.logs_processamento.append("-" * 30)
            self.logs_processamento.append("✅ Processamento concluído!")
            self.logs_processamento.append(f"📄 Novo formato: {self.formato_atual}")
        else:
            msg = f"❌ Estratégia inválida ou não definida para mídia ID: {self.id}"
            self.logs_processamento.append(msg)

    @property
    def strategy(self) -> Optional[ProcessamentoStrategy]:
        return self._strategy
    
    def __str__(self) -> str:
        return f"ID:{self.id} ({self.legenda}) - Formato: {self.formato_atual}"
    
    @abstractmethod
    def tipo(self) -> str: # Para diferenciar na UI
        pass

# ===== CONCRETE CONTEXTS (Midia) =====
class Video(MidiaDigital):
    def __init__(self, id_midia: int, formato: str, legenda: str, url_arquivo: str, duracao: int):
        super().__init__(id_midia, formato, legenda)
        self.url_arquivo = url_arquivo
        self.duracao = duracao
        self.set_strategy(ProcessamentoVideo("H.264", 1080)) # Estratégia padrão
    
    def tipo(self) -> str: return "Vídeo"

class Imagem(MidiaDigital):
    def __init__(self, id_midia: int, formato: str, legenda: str, url_arquivo: str, resolucao: str):
        super().__init__(id_midia, formato, legenda)
        self.url_arquivo = url_arquivo
        self.resolucao_original = resolucao # Guardar original
        self.set_strategy(ProcessamentoImagem("Alta", "1920x1080")) # Estratégia padrão

    def tipo(self) -> str: return "Imagem"


# ===== MEMORIA CLASS (Simplificada para o backend) =====
class Memoria:
    def __init__(self):
        self._midias: List[MidiaDigital] = []
    
    def adicionar_midia(self, midia: MidiaDigital) -> None:
        self._midias.append(midia)
    
    def get_midia_by_id(self, midia_id: int) -> Optional[MidiaDigital]:
        for midia in self._midias:
            if midia.id == midia_id:
                return midia
        return None

    @property
    def midias(self) -> List[MidiaDigital]:
        return self._midias.copy()

    def clear_all_media_logs(self):
        for midia in self._midias:
            midia.logs_processamento = []


# ===== FLASK APP SETUP =====
app = Flask(__name__)
app.secret_key = 'uma_chave_secreta_simples'

# --- Estado Global para o Demo ---
memoria_global = Memoria()
next_media_id_global = 1
# Logs gerais da aplicação (não por mídia)
app_execution_logs: List[str] = []


# --- Estratégias disponíveis para a UI ---
# Usamos lambdas para que os parâmetros sejam passados no momento da criação
# Se a estratégia não tem parâmetros, a lambda simplesmente chama o construtor
available_processing_strategies: Dict[str, Callable[[], ProcessamentoStrategy]] = {
    "video_padrao": lambda: ProcessamentoVideo("H.264", 1080),
    "video_4k": lambda: ProcessamentoVideo("H.265", 2160),
    "imagem_padrao": lambda: ProcessamentoImagem("Padrão", "1024x768"),
    "imagem_altares": lambda: ProcessamentoImagem("Alta", "3840x2160"),
    "web_otimizado": lambda: ProcessamentoWebOptimizado("WebP"),
    "mobile_otimizado": lambda: ProcessamentoMobileOptimizado(),
}

def get_next_id() -> int:
    global next_media_id_global
    current_id = next_media_id_global
    next_media_id_global += 1
    return current_id

def add_app_log(message: str):
    """Adiciona log à lista de logs da aplicação."""
    timestamp = datetime.now().strftime("%H:%M:%S")
    app_execution_logs.insert(0, f"[{timestamp}] {message}")
    if len(app_execution_logs) > 20: # Limita o tamanho dos logs
        app_execution_logs.pop()

def setup_initial_data():
    """Configura algumas mídias iniciais para o demo."""
    global memoria_global, next_media_id_global, app_execution_logs
    memoria_global = Memoria() # Reseta a memória
    app_execution_logs = []    # Limpa logs da app
    next_media_id_global = 1   # Reseta contador de ID

    add_app_log(" Dados iniciais carregados.")
    video1 = Video(id_midia=get_next_id(), formato="AVI", legenda="Filme Curto", url_arquivo="curta.avi", duracao=180)
    memoria_global.adicionar_midia(video1)
    add_app_log(f" Adicionado: {video1.tipo()} '{video1.legenda}'")

    img1 = Imagem(id_midia=get_next_id(), formato="BMP", legenda="Logo Antigo", url_arquivo="logo.bmp", resolucao="800x600")
    memoria_global.adicionar_midia(img1)
    add_app_log(f" Adicionado: {img1.tipo()} '{img1.legenda}'")


# ===== FLASK ROUTES =====
@app.route('/', methods=['GET'])
def index():
    # Limpa os logs de processamento de cada mídia ao recarregar a página principal
    # para evitar mostrar logs de ações anteriores de forma persistente na listagem de mídias.
    # Os logs da aplicação (gerais) são mantidos.
    memoria_global.clear_all_media_logs()
    
    return render_template('index.html',
                           midias=memoria_global.midias,
                           processing_strategies=available_processing_strategies,
                           app_logs=app_execution_logs)

@app.route('/add_media', methods=['POST'])
def add_media_route():
    tipo_midia = request.form.get('tipo_midia')
    legenda = request.form.get('legenda', 'Nova Mídia')
    formato_original = request.form.get('formato_original', 'N/A')
    
    midia_id = get_next_id()
    nova_midia: Optional[MidiaDigital] = None

    if tipo_midia == 'video':
        nova_midia = Video(midia_id, formato_original, legenda, "video.url", 60)
    elif tipo_midia == 'imagem':
        nova_midia = Imagem(midia_id, formato_original, legenda, "imagem.url", "100x100")
    
    if nova_midia:
        memoria_global.adicionar_midia(nova_midia)
        add_app_log(f"➕ Mídia '{nova_midia.legenda}' ({nova_midia.tipo()}) adicionada com ID {nova_midia.id}.")
        flash(f"Mídia '{nova_midia.legenda}' adicionada!", 'success')
    else:
        add_app_log(f"⚠️ Tentativa de adicionar tipo de mídia inválido: {tipo_midia}")
        flash('Tipo de mídia inválido.', 'error')
        
    return redirect(url_for('index'))

@app.route('/process_media/<int:media_id>', methods=['POST'])
def process_media_route(media_id):
    midia = memoria_global.get_midia_by_id(media_id)
    if midia:
        strategy_key = request.form.get('strategy_key') # Pega a estratégia do form
        if strategy_key and strategy_key in available_processing_strategies:
            nova_strategia = available_processing_strategies[strategy_key]()
            midia.set_strategy(nova_strategia)
            add_app_log(f"🛠️ Estratégia '{nova_strategia}' definida para mídia ID {media_id}.")
            flash(f"Estratégia '{nova_strategia}' definida para '{midia.legenda}'. Processando...", 'info')
        elif not midia.strategy:
             add_app_log(f"⚠️ Mídia ID {media_id} não tem estratégia definida. Usando padrão se houver ou falhando.")
             flash(f"Mídia '{midia.legenda}' não tinha estratégia explícita. Verifique se uma padrão foi aplicada.", 'warning')


        midia.executar_processamento() # Executa com a estratégia nova ou a já existente
        # Os logs do processamento da mídia estarão em midia.logs_processamento
        # e serão mostrados no template da próxima vez que a mídia for renderizada.
        # Adicionamos um log geral para a aplicação também.
        if midia.logs_processamento and "✅" in midia.logs_processamento[-1]: # Verifica se o último log indica sucesso
             add_app_log(f"⚙️ Mídia ID {media_id} ('{midia.legenda}') processada. Novo formato: {midia.formato_atual}")
             flash(f"Mídia '{midia.legenda}' processada! Novo formato: {midia.formato_atual}", 'success')
        else:
            add_app_log(f"⚠️ Falha ou não processamento da mídia ID {media_id} ('{midia.legenda}').")
            flash(f"Processamento de '{midia.legenda}' resultou em: {midia.logs_processamento[-1] if midia.logs_processamento else 'Nenhum log'}", 'warning')

    else:
        add_app_log(f"❌ Mídia ID {media_id} não encontrada para processamento.")
        flash(f'Mídia ID {media_id} não encontrada.', 'error')
    
    # Renderiza a página novamente, mostrando os logs de processamento da mídia específica
    return render_template('index.html',
                           midias=memoria_global.midias,
                           processing_strategies=available_processing_strategies,
                           app_logs=app_execution_logs,
                           processed_media_id=media_id) # Para focar na mídia processada, se necessário

@app.route('/reset_demo', methods=['POST'])
def reset_demo_route():
    setup_initial_data()
    add_app_log("🔄 Demonstração Reiniciada.")
    flash('Demonstração reiniciada com dados de exemplo.', 'info')
    return redirect(url_for('index'))


if __name__ == '__main__':
    setup_initial_data() # Carrega dados iniciais ao iniciar
    app.run(debug=True, port=5002) # Porta diferente para não conflitar com o anterior