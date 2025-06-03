from datetime import date
from typing import List


class Usuario:
    def __init__(self, nome: str):
        self.nome = nome


class Tag:
    def __init__(self, id: int, nome: str):
        self.id = id
        self.nome = nome


class MidiaDigital:
    def __init__(self, id: int, formato: str, legenda: str):
        self.id = id
        self.formato = formato
        self.legenda = legenda


class Imagem(MidiaDigital):
    def __init__(self, id: int, formato: str, legenda: str, url_arquivo: str, texto_alternativo: str, resolucao: str):
        super().__init__(id, formato, legenda)
        self.url_arquivo = url_arquivo
        self.texto_alternativo = texto_alternativo
        self.resolucao = resolucao


class Video(MidiaDigital):
    def __init__(self, id: int, formato: str, legenda: str, url_arquivo: str, duracao: int):
        super().__init__(id, formato, legenda)
        self.url_arquivo = url_arquivo
        self.duracao = duracao


class Memoria:
    def __init__(self, titulo: str, descricao: str, status: str, autor: Usuario, data_envio: date):
        self.titulo = titulo
        self.descricao = descricao
        self.status = status
        self.autor = autor
        self.data_envio = data_envio
        self.midias: List[MidiaDigital] = []
        self.tags: List[Tag] = []

    def adicionar_tag(self, tag: Tag):
        self.tags.append(tag)

    def adicionar_midia(self, midia: MidiaDigital):
        self.midias.append(midia)


class MemoriaBuilder:
    def __init__(self):
        self._titulo = None
        self._descricao = None
        self._status = None
        self._autor = None
        self._data_envio = None
        self._midias = []
        self._tags = []

    def com_titulo(self, titulo: str):
        self._titulo = titulo
        return self

    def com_descricao(self, descricao: str):
        self._descricao = descricao
        return self

    def com_status(self, status: str):
        self._status = status
        return self

    def com_autor(self, autor: Usuario):
        self._autor = autor
        return self

    def com_data_envio(self, data_envio: date):
        self._data_envio = data_envio
        return self

    def com_midia(self, midia: MidiaDigital):
        self._midias.append(midia)
        return self

    def com_tag(self, tag: Tag):
        self._tags.append(tag)
        return self

    def build(self):
        memoria = Memoria(
            titulo=self._titulo,
            descricao=self._descricao,
            status=self._status,
            autor=self._autor,
            data_envio=self._data_envio
        )
        for midia in self._midias:
            memoria.adicionar_midia(midia)
        for tag in self._tags:
            memoria.adicionar_tag(tag)
        return memoria

def criar_memoria():
    print("=== Criação de Memória ===")

    nome_autor = input("Digite o nome do autor: ")
    autor = Usuario(nome_autor)

    titulo = input("Título da memória: ")
    descricao = input("Descrição da memória: ")
    data_envio = date.today()
    status = "Pendente"  # Status fixo

    builder = MemoriaBuilder() \
        .com_titulo(titulo) \
        .com_descricao(descricao) \
        .com_status(status) \
        .com_autor(autor) \
        .com_data_envio(data_envio)

    # Adicionar mídias
    # Adicionar mídias
    while True:
        opcao = input("Qual mídia você que adicionar? (1 - Imagem, 2 - Vídeo, Enter para continuar): ")
        if opcao == "1":
            imagem = Imagem(id=0, formato="jpg", legenda="", url_arquivo="", texto_alternativo="", resolucao="")
            builder.com_midia(imagem)
            print("Imagem adicionada!")
            break
        elif opcao == "2":
            video = Video(id=0, formato="mp4", legenda="", url_arquivo="", duracao=0)
            builder.com_midia(video)
            print("Vídeo adicionado!")
            break
        elif opcao == "":
            break
        else:
            print("Opção inválida.")


    id_tag_counter = 1  

    while True:
        adicionar = input("Deseja adicionar uma tag? (s/n): ")
        if adicionar.lower() == "s":
            nome_tag = input("Nome da tag: ")
            tag = Tag(id_tag_counter, nome_tag)
            builder.com_tag(tag)
            print("Tag adicionada!")
            id_tag_counter += 1
            break
        elif adicionar.lower() == "n":
            break
        else:
            print("Digite 's' ou 'n'.")

    memoria = builder.build()

    # Resumo
    print("\n=== Memória criada com sucesso ===")
    print(f"Título: {memoria.titulo}")
    print(f"Descrição: {memoria.descricao}")
    print(f"Status: {memoria.status}")
    print(f"Autor: {memoria.autor.nome}")
    print(f"Data de envio: {memoria.data_envio}")
    print(f"Mídias ({len(memoria.midias)}):")
    for midia in memoria.midias:
        tipo = "Imagem" if isinstance(midia, Imagem) else "Vídeo"
        print(f" - {tipo} (ID: {midia.id}, Formato: {midia.formato}, Legenda: {midia.legenda})")

    print(f"Tags ({len(memoria.tags)}): {[tag.nome for tag in memoria.tags]}")

if __name__ == "__main__":
    criar_memoria()