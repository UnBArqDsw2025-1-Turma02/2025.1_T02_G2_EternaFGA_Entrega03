from flask import Flask, render_template_string
from datetime import date
from abc import ABC, abstractmethod
from typing import List

app = Flask(__name__)

# Estratégia de exibição
class ExibicaoStrategy(ABC):
    @abstractmethod
    def exibir(self, midia):
        pass

class ExibicaoImagem(ExibicaoStrategy):
    def exibir(self, midia):
        return {
            "tipo": "imagem",
            "url": midia.urlArquivo,
            "resolucao": midia.resolucao,
            "texto": midia.textoAlternativo,
            "legenda": midia.legenda
        }

class ExibicaoVideo(ExibicaoStrategy):
    def exibir(self, midia):
        return {
            "tipo": "video",
            "url": midia.urlArquivo,
            "duracao": midia.duracao,
            "legenda": midia.legenda,
            "formato": midia.formato
        }

# Mídia base
class MidiaDigital:
    def __init__(self, formato: str, legenda: str):
        self.formato = formato
        self.legenda = legenda
        self._estrategia_exibicao: ExibicaoStrategy = None

    def set_exibicao_strategy(self, estrategia: ExibicaoStrategy):
        self._estrategia_exibicao = estrategia

    def exibir(self):
        if self._estrategia_exibicao:
            return self._estrategia_exibicao.exibir(self)
        else:
            return {"erro": "Estratégia de exibição não definida."}

# Vídeo
class Video(MidiaDigital):
    def __init__(self, formato: str, legenda: str, urlArquivo: str, duracao: str):
        super().__init__(formato, legenda)
        self.urlArquivo = urlArquivo
        self.duracao = duracao

# Imagem
class Imagem(MidiaDigital):
    def __init__(self, formato: str, legenda: str, urlArquivo: str, textoAlternativo: str, resolucao: str):
        super().__init__(formato, legenda)
        self.urlArquivo = urlArquivo
        self.textoAlternativo = textoAlternativo
        self.resolucao = resolucao

# Memória
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

    def exibir_midias(self):
        return [midia.exibir() for midia in self.midias]

# Dados de exemplo
img1 = Imagem("jpg", "Foto da paisagem", "/static/paisagem.jpg", "Descrição da paisagem", "1920x1080")
vid1 = Video("mp4", "Vídeo da festa", "/static/festa.mp4", "02:30")
img2 = Imagem("png", "Foto do pôr do sol", "/static/por_do_sol.png", "Pôr do sol na praia", "1280x720")

img1.set_exibicao_strategy(ExibicaoImagem())
vid1.set_exibicao_strategy(ExibicaoVideo())
img2.set_exibicao_strategy(ExibicaoImagem())

memoria = Memoria(1, "Viagem à praia", "Momentos incríveis", "público", "Ana", date.today())
memoria.addMidiaDigital(img1)
memoria.addMidiaDigital(img2)
memoria.addMidiaDigital(vid1)
memoria.adicionarTag("praia")
memoria.adicionarTag("férias")

# Página principal
@app.route("/")
def index():
    return render_template_string("""
    <html>
    <head>
        <title>Memória: {{ memoria.titulo }}</title>
        <style>
            body { font-family: Arial; padding: 20px; background: #f4f4f4; }
            .memoria { background: white; padding: 20px; border-radius: 10px; }
            .midia { margin: 20px 0; padding: 10px; background: #eef; border-radius: 8px; }
            .imagem { border: 2px solid #99c; padding: 10px; }
            .video { border: 2px dashed #c99; padding: 10px; }
            video { width: 100%; max-width: 600px; }
            img { max-width: 100%; height: auto; border-radius: 8px; }
            .tags { font-size: 0.9em; color: #666; }
        </style>
    </head>
    <body>
        <div class="memoria">
            <h1>{{ memoria.titulo }}</h1>
            <p><strong>Legenda:</strong> {{ memoria.legenda }}</p>
            <p><strong>Autor:</strong> {{ memoria.autor }} | <strong>Data:</strong> {{ memoria.dataEnvio }}</p>
            <p class="tags"><strong>Tags:</strong> {{ ", ".join(memoria.tags) }}</p>
            
            <h2>Mídias</h2>
            {% for m in midias %}
                <div class="midia {% if m.tipo == 'imagem' %}imagem{% else %}video{% endif %}">
                    {% if m.tipo == 'imagem' %}
                        <img src="{{ m.url }}" alt="{{ m.texto }}">
                        <p><strong>Legenda:</strong> {{ m.legenda }}</p>
                        <p><strong>Resolução:</strong> {{ m.resolucao }}</p>
                    {% elif m.tipo == 'video' %}
                        <video controls>
                            <source src="{{ m.url }}" type="video/mp4">
                            Seu navegador não suporta o vídeo.
                        </video>
                        <p><strong>Legenda:</strong> {{ m.legenda }}</p>
                        <p><strong>Duração:</strong> {{ m.duracao }}</p>
                    {% endif %}
                </div>
            {% endfor %}
        </div>
    </body>
    </html>
    """, memoria=memoria, midias=memoria.exibir_midias())

# Rodar o app
if __name__ == "__main__":
    app.run(debug=True)
