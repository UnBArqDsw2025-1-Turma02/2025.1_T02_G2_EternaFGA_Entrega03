from flask import Flask, request, jsonify, render_template_string
from abc import ABC, abstractmethod
from typing import Optional, Any, Dict

app = Flask(__name__)

# Produto
class MidiaDigital(ABC):
    def __init__(self, id: int, url: str, formato: str, legenda: Optional[str] = None):
        self.id = id
        self.url = url
        self.formato = formato
        self.legenda = legenda if legenda else "Mídia sem legenda"

# Produto Concreto 1
class Video(MidiaDigital):
    """
    Representa um arquivo de vídeo, um tipo de MidiaDigital.
    """
    def __init__(self, id: int, url: str, formato: str, legenda: Optional[str] = None, duracao: str = "00:00"):
        super().__init__(id, url, formato, legenda)
        self.duracao = duracao

# Produto Concreto 2
class Imagem(MidiaDigital):
    """
    Representa um arquivo de imagem, um tipo de MidiaDigital.
    """
    def __init__(self, id: int, url: str, formato: str, legenda: Optional[str] = None, resolucao: str = "N/A", textoAlternativo: Optional[str] = None):
        super().__init__(id, url, formato, legenda)
        self.resolucao = resolucao
        self.textoAlternativo = textoAlternativo if textoAlternativo and textoAlternativo.strip() else "Imagem sem texto alternativo"

# Creator (fábrica abstrata)
class CreateMidiaDigital(ABC):
    def __init__(self):
        self.midia: Optional[MidiaDigital] = None

    @abstractmethod
    def criarMidia(self, id: int, url: str, formato: str, legenda: Optional[str] = None, **kwargs: Any) -> MidiaDigital:
        pass

    def enviar(self) -> str:
        if self.midia and hasattr(self.midia, 'id'):
            msg = f"Enviando mídia com ID {self.midia.id}, formato {self.midia.formato}, legenda: {self.midia.legenda}."
            if isinstance(self.midia, Video):
                msg += f" Duração: {self.midia.duracao}."
            elif isinstance(self.midia, Imagem):
                msg += f" Resolução: {self.midia.resolucao}."
                # Only add alt text to message if it's custom (not the default placeholder)
                if self.midia.textoAlternativo and self.midia.textoAlternativo != "Imagem sem texto alternativo":
                     msg += f" Texto Alternativo: {self.midia.textoAlternativo}."
            print(msg) # Server log
            return msg
        else:
            err_msg = "Erro: Mídia não criada ou sem ID para enviar."
            print(err_msg)
            return err_msg

# Fábrica concreta para vídeo
class CreateVideo(CreateMidiaDigital):
    def criarMidia(self, id: int, url: str, formato: str, legenda: Optional[str] = None, **kwargs: Any) -> MidiaDigital:
        duracao = kwargs.get("duracao", "00:00")
        self.midia = Video(id, url, formato, legenda, duracao=duracao)
        return self.midia

# Fábrica concreta para imagem
class CreateImagem(CreateMidiaDigital):
    def criarMidia(self, id: int, url: str, formato: str, legenda: Optional[str] = None, **kwargs: Any) -> MidiaDigital:
        resolucao = kwargs.get("resolucao", "N/A")
        textoAlternativo = kwargs.get("textoAlternativo") # Get from kwargs
        self.midia = Imagem(id, url, formato, legenda, resolucao=resolucao, textoAlternativo=textoAlternativo)
        return self.midia
    

# Frontend HTML com CSS e JS integrados (inline no render_template_string)
frontend_html = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Enviar Memória</title>
<style>
    body {
        font-family: Arial, sans-serif;
        background-color: #f4f4f4;
        margin: 0;
        padding: 20px;
    }
    .container {
        max-width: 600px;
        margin: auto;
        background: white;
        padding: 20px;
        border-radius: 5px;
        box-shadow: 0 0 12px rgba(0, 0, 0, 0.15);
    }
    h1 {
        text-align: center;
        color: #333;
    }
    label {
        display: block;
        margin-top: 15px;
        font-weight: bold;
        color: #555;
    }
    input, select {
        width: 100%;
        padding: 10px;
        margin-top: 6px;
        border: 1px solid #ccc;
        border-radius: 5px;
        font-size: 16px;
        box-sizing: border-box;
        transition: border-color 0.3s ease;
    }
    input:focus, select:focus {
        border-color: #28a745;
        outline: none;
    }
    button {
        width: 100%;
        margin-top: 25px;
        background-color: #28a745;
        border: none;
        color: white;
        font-size: 18px;
        padding: 12px;
        border-radius: 6px;
        cursor: pointer;
        box-shadow: 0 4px 8px rgba(40, 167, 69, 0.3);
        transition: background-color 0.25s ease;
    }
    button:hover {
        background-color: #218838;
    }
    #resultado {
        margin-top: 30px;
        font-weight: bold;
        font-size: 16px;
        color: #222;
        padding: 15px;
        background-color: #e8f5e9;
        border: 2px solid #28a745;
        border-radius: 6px;
        word-wrap: break-word;
        white-space: pre-wrap;
    }
</style>
</head>
<body>
<div class="container">
    <h1>Enviar Memória</h1>
    <form id="midiaForm">
        <label for="tipo">Tipo de Mídia:</label>
        <select id="tipo" name="tipo" required>
            <option value="video" selected>Vídeo</option>
            <option value="imagem">Imagem</option>
        </select>

        <label for="id">ID:</label>
        <input type="number" id="id" name="id" required min="1" />

        <label for="url_arquivo">URL do Arquivo:</label>
        <input type="text" id="url_arquivo" name="url_arquivo" placeholder="https://exemplo.com/midia" required />
        
        <label for="formato">Formato:</label>
        <input type="text" id="formato" name="formato" placeholder="Ex: mp4, jpg, png" required />

        <label for="legenda">Legenda:</label>
        <input type="text" id="legenda" name="legenda" placeholder="Digite a legenda da mídia (opcional)" />

        <div id="duracaoContainer" style="display:block;">
            <label for="duracao">Duração:</label>
            <input type="text" id="duracao" name="duracao" placeholder="Ex: 00:03:45" />
        </div>

        <div id="imagemDetalhesContainer" style="display:none;">
            <label for="resolucao">Resolução:</label>
            <input type="text" id="resolucao" name="resolucao" placeholder="Ex: 1920x1080" />

            <label for="textoAlternativo">Texto Alternativo (Alt Text):</label>
            <input type="text" id="textoAlternativo" name="textoAlternativo" placeholder="Descreva a imagem para acessibilidade (opcional)" />
        </div>

        <button type="submit">Enviar</button>
    </form>
    <div id="resultado"></div>
</div>

<script>
    const tipoSelect = document.getElementById('tipo');
    const duracaoContainer = document.getElementById('duracaoContainer');
    const duracaoInput = document.getElementById('duracao');
    
    const imagemDetalhesContainer = document.getElementById('imagemDetalhesContainer');
    const resolucaoInput = document.getElementById('resolucao');
    const textoAlternativoInput = document.getElementById('textoAlternativo');

    function atualizarCamposMidia() {
        if (tipoSelect.value === 'imagem') {
            imagemDetalhesContainer.style.display = 'block';
            resolucaoInput.required = true;
            textoAlternativoInput.required = false; // Alt text é opcional

            duracaoContainer.style.display = 'none';
            duracaoInput.required = false;
            duracaoInput.value = '';
        } else { // 'video'
            duracaoContainer.style.display = 'block';
            duracaoInput.required = true; // Duração é obrigatória para vídeo

            imagemDetalhesContainer.style.display = 'none';
            resolucaoInput.required = false;
            resolucaoInput.value = '';
            textoAlternativoInput.required = false;
            textoAlternativoInput.value = '';
        }
    }

    tipoSelect.addEventListener('change', atualizarCamposMidia);
    document.addEventListener('DOMContentLoaded', atualizarCamposMidia); // Call on page load

    document.getElementById('midiaForm').addEventListener('submit', async function(event) {
        event.preventDefault();
        const formData = new FormData(this);
        const data = Object.fromEntries(formData.entries());

        try {
            const response = await fetch('/midia', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data)
            });

            const resultText = await response.text();
            let result;
            try {
                result = JSON.parse(resultText);
            } catch (e) {
                document.getElementById('resultado').textContent = "Erro: Resposta inesperada do servidor. " + resultText;
                console.error("Server response (not JSON):", resultText);
                return;
            }
            
            if (!response.ok) {
                throw new Error(result.message || "Erro no envio. Código: " + response.status);
            }
            
            document.getElementById('resultado').textContent = result.message;
        } catch (error) {
            document.getElementById('resultado').textContent = "Erro: " + error.message;
        }
    });
</script>
</body>
</html>
"""


## parte do backend
@app.route('/')
def index():
    return render_template_string(frontend_html)

@app.route('/midia', methods=['POST'])
def criar_midia_endpoint():
    data = request.get_json()

    tipo = data.get('tipo')
    try:
        id_val = int(data.get('id'))
    except (ValueError, TypeError):
        return jsonify({'message': 'ID inválido. Deve ser um número.'}), 400

    legenda = data.get('legenda', '') 
    url_arquivo = data.get('url_arquivo')
    formato = data.get('formato')
    
    resolucao = data.get('resolucao')
    duracao = data.get('duracao')
    texto_alternativo_val = data.get('textoAlternativo', '') # Get textoAlternativo

    if not all([tipo, id_val is not None, url_arquivo, formato]):
        return jsonify({'message': 'Dados incompletos. Tipo, ID, URL do Arquivo e Formato são obrigatórios.'}), 400
    
    if id_val <= 0:
        return jsonify({'message': 'ID deve ser um número positivo.'}), 400

    criador: Optional[CreateMidiaDigital] = None
    midia_criada: Optional[MidiaDigital] = None

    if tipo == 'video':
        if not duracao:
            return jsonify({'message': 'Duração é obrigatória para vídeos.'}), 400
        criador = CreateVideo()
        midia_criada = criador.criarMidia(id=id_val, url=url_arquivo, formato=formato, legenda=legenda, duracao=duracao)
    elif tipo == 'imagem':
        if not resolucao:
            return jsonify({'message': 'Resolução é obrigatória para imagens.'}), 400
        criador = CreateImagem()
        midia_criada = criador.criarMidia(id=id_val, url=url_arquivo, formato=formato, legenda=legenda, resolucao=resolucao, textoAlternativo=texto_alternativo_val)
    else:
        return jsonify({'message': 'Tipo de mídia inválido.'}), 400

    if midia_criada and criador:
        msg = criador.enviar()
        return jsonify({'message': msg, 'status': 'success'})
    else:
        return jsonify({'message': 'Erro ao processar a mídia.'}), 500


if __name__ == '__main__':
    app.run(debug=True) 