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