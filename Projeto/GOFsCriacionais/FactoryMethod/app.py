from flask import Flask, request, jsonify, render_template_string
from abc import ABC, abstractmethod
from typing import Optional, Any, Dict

app = Flask(__name__)

# Produto
class MidiaDigital(ABC):
    def __init__(self, url: str, formato: str, legenda: Optional[str] = None):
        self.url = url
        self.formato = formato
        self.legenda = legenda if legenda else "Mídia sem legenda"

# Produto Concreto 1
class Video(MidiaDigital):
    """
    Representa um arquivo de vídeo, um tipo de MidiaDigital.
    """
    def __init__(self, url: str, formato: str, legenda: Optional[str] = None, duracao: str = "00:00"):
        super().__init__(url, formato, legenda)
        self.duracao = duracao # Atributo específico do vídeo

# Produto Concreto 2
class Imagem(MidiaDigital):
    """
    Representa um arquivo de imagem, um tipo de MidiaDigital.
    """
    def __init__(self, url: str, formato: str, legenda: Optional[str] = None, resolucao: str = "N/A"):
        super().__init__(url, formato, legenda)
        self.resolucao = resolucao # Atributo específico da imagem

# Creator (fábrica abstrata)
class CreateMidiaDigital(ABC):
    def __init__(self):
        self.midia = None

    @abstractmethod
    def criarMidia(self, url: str, formato: str, legenda: Optional[str] = None, **kwargs: Any) -> MidiaDigital:
        pass

    def enviar(self):
        print(f"Enviando mídia com ID {self.midia.id} e legenda: {self.midia.legenda}")

# Fábrica concreta para vídeo
class CreateVideo(CreateMidiaDigital):

    def criarMidia(self, url: str, formato: str, legenda: Optional[str] = None, **kwargs: Any) -> MidiaDigital:
        duracao = kwargs.get("duracao", "00:00")
        return Video(url, formato, legenda, duracao=duracao)

# Fábrica concreta para imagem
class CreateImagem(CreateMidiaDigital):

    def criar_midia(self, url: str, formato: str, legenda: Optional[str] = None, **kwargs: Any) -> MidiaDigital:
        resolucao = kwargs.get("resolucao", "N/A")
        return Imagem(url, formato, legenda, resolucao=resolucao)
    

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
        font-size: 18px;
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

        <label for="legenda">Legenda:</label>
        <input type="text" id="legenda" name="legenda" required />

        <label for="url_arquivo">URL do Arquivo:</label>
        <input type="text" id="url_arquivo" name="url_arquivo" required />

        <div id="resolucaoContainer" style="display:none;">
            <label for="resolucao">Resolução:</label>
            <input type="text" id="resolucao" name="resolucao" placeholder="Ex: 1920x1080" />
        </div>

        <button type="submit">Enviar</button>
    </form>
    <div id="resultado"></div>
</div>

<script>
    const tipoSelect = document.getElementById('tipo');
    const resolucaoContainer = document.getElementById('resolucaoContainer');

    tipoSelect.addEventListener('change', function() {
        if (this.value === 'imagem') {
            resolucaoContainer.style.display = 'block';
            document.getElementById('resolucao').required = true;
        } else {
            resolucaoContainer.style.display = 'none';
            document.getElementById('resolucao').required = false;
            document.getElementById('resolucao').value = '';
        }
    });

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

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.message || "Erro no envio");
            }

            const result = await response.json();
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
def criar_midia():
    data = request.get_json()

    tipo = data.get('tipo')
    try:
        id = int(data.get('id'))
    except (ValueError, TypeError):
        return jsonify({'message': 'ID inválido'}), 400

    legenda = data.get('legenda')
    url_arquivo = data.get('url_arquivo')
    resolucao = data.get('resolucao')  # Pode ser None se não for imagem

    if not all([tipo, id, legenda, url_arquivo]):
        return jsonify({'message': 'Dados incompletos'}), 400

    if tipo == 'video':
        criador = CreateVideo()
        midia = criador.factory_method(id=id, legenda=legenda, url_arquivo=url_arquivo)
    elif tipo == 'imagem':
        if not resolucao:
            return jsonify({'message': 'Resolução obrigatória para imagens'}), 400
        criador = CreateImagem()
        midia = criador.factory_method(id=id, legenda=legenda, url_arquivo=url_arquivo, resolucao=resolucao)
    else:
        return jsonify({'message': 'Tipo de mídia inválido'}), 400

    msg = criador.enviar()

    return jsonify({'message': msg})

if __name__ == '__main__':
    app.run(debug=True)

