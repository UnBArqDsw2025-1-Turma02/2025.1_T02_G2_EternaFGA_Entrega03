from flask import Flask, request, render_template_string
from abc import ABC, abstractmethod
from datetime import date
from typing import List

app = Flask(__name__)
memorias_salvas = {}

class MidiaDigital(ABC):
    def __init__(self, formato: str, legenda: str):
        self.formato = formato
        self.legenda = legenda

    @abstractmethod
    def exibir(self):
        pass

class Video(MidiaDigital):
    def __init__(self, formato: str, legenda: str, urlArquivo: str, duracao: str):
        super().__init__(formato, legenda)
        self.urlArquivo = urlArquivo
        self.duracao = duracao

    def exibir(self):
        return f"[Vídeo] URL: {self.urlArquivo}, Duração: {self.duracao}, Legenda: {self.legenda}, Formato: {self.formato}"

class Imagem(MidiaDigital):
    def __init__(self, formato: str, legenda: str, urlArquivo: str, textoAlternativo: str, resolucao: str):
        super().__init__(formato, legenda)
        self.urlArquivo = urlArquivo
        self.textoAlternativo = textoAlternativo
        self.resolucao = resolucao

    def exibir(self):
        return f"[Imagem] URL: {self.urlArquivo}, Resolução: {self.resolucao}, Texto Alt: {self.textoAlternativo}, Legenda: {self.legenda}"

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

    def adicionarTag(self, tag: str):
        self.tags.append(tag)

    def exibir(self):
        media_exibidas = [midia.exibir() for midia in self.midias]
        return {
            "id": self.id,
            "titulo": self.titulo,
            "legenda": self.legenda,
            "status": self.status,
            "autor": self.autor,
            "dataEnvio": self.dataEnvio.isoformat(),
            "tags": self.tags,
            "midias": media_exibidas
        }

HTML = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Memória Digital</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f5f5f5; padding: 30px; }
        form { background: #fff; padding: 20px; border-radius: 8px; max-width: 800px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
        label { display: block; margin-top: 10px; font-weight: bold; }
        input, select { width: 100%; padding: 8px; margin-top: 4px; }
        button { margin-top: 15px; padding: 10px 20px; background: #673ab7; color: white; border: none; border-radius: 4px; cursor: pointer; }
        button:hover { background: #512da8; }
        .midia-group { padding: 10px; margin-top: 10px; border: 1px solid #ccc; border-radius: 6px; background: #fafafa; }
        .output { margin-top: 40px; background: #e0e0e0; padding: 20px; border-radius: 8px; white-space: pre-wrap; }
    </style>
</head>
<body>
    <h1>Cadastrar Memória</h1>
    <form method="POST">
        <label>ID</label>
        <input name="id" type="number" required>

        <label>Título</label>
        <input name="titulo" required>

        <label>Legenda</label>
        <input name="legenda" required>

        <label>Status</label>
        <input name="status" required>

        <label>Autor</label>
        <input name="autor" required>

        <label>Tags (separadas por vírgula)</label>
        <input name="tags">

        <h2>Mídias</h2>
        <div id="midias-container"></div>
        <button type="button" onclick="adicionarMidia()">+ Adicionar Mídia</button>

        <br><button type="submit">Criar Memória</button>
    </form>

    <h1>Buscar Memória</h1>
    <form method="GET">
        <label>Informe o ID</label>
        <input name="id" type="number" required>
        <button type="submit">Buscar</button>
    </form>

    {% if memoria %}
    <div class="output">
        <h2>Memória encontrada:</h2>
        <pre>{{ memoria | tojson(indent=2) }}</pre>
    </div>
    {% endif %}

<script>
let contador = 0;
function adicionarMidia() {
    const container = document.getElementById('midias-container');
    const midiaDiv = document.createElement('div');
    midiaDiv.className = 'midia-group';
    midiaDiv.innerHTML = `
        <label>Tipo</label>
        <select name="tipo_${contador}">
            <option value="video">Vídeo</option>
            <option value="imagem">Imagem</option>
        </select>

        <label>Formato</label>
        <input name="formato_${contador}" required>

        <label>Legenda da Mídia</label>
        <input name="midia_legenda_${contador}" required>

        <label>URL do Arquivo</label>
        <input name="urlArquivo_${contador}" required>

        <label>Duração (vídeo)</label>
        <input name="duracao_${contador}">

        <label>Texto Alternativo (imagem)</label>
        <input name="textoAlternativo_${contador}">

        <label>Resolução (imagem)</label>
        <input name="resolucao_${contador}">
    `;
    container.appendChild(midiaDiv);
    contador++;
}
</script>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    memoria = None
    if request.method == 'POST':
        data = request.form
        id = int(data['id'])
        memoria = Memoria(id, data['titulo'], data['legenda'], data['status'], data['autor'], date.today())

        # Adiciona mídias dinamicamente
        i = 0
        while f"tipo_{i}" in data:
            tipo = data[f"tipo_{i}"]
            formato = data[f"formato_{i}"]
            legenda = data[f"midia_legenda_{i}"]
            url = data[f"urlArquivo_{i}"]

            if tipo == "video":
                duracao = data.get(f"duracao_{i}", "")
                midia = Video(formato, legenda, url, duracao)
            elif tipo == "imagem":
                textoAlt = data.get(f"textoAlternativo_{i}", "")
                resolucao = data.get(f"resolucao_{i}", "")
                midia = Imagem(formato, legenda, url, textoAlt, resolucao)
            else:
                midia = None

            if midia:
                memoria.addMidiaDigital(midia)
            i += 1

        tags = data.get('tags', '')
        for tag in tags.split(','):
            memoria.adicionarTag(tag.strip())

        memorias_salvas[id] = memoria

    elif request.method == 'GET' and 'id' in request.args:
        id_param = request.args.get('id')
        if id_param and id_param.isdigit():
            memoria = memorias_salvas.get(int(id_param))

    return render_template_string(HTML, memoria=memoria.exibir() if memoria else None)

if __name__ == '__main__':
    app.run(debug=True)
