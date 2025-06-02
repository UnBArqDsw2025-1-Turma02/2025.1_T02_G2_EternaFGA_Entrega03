from datetime import datetime, timedelta
from typing import Optional, List


class Sessao:
    def __init__(self, token: str, usuario: str, duracao_minutos: int = 30):
        self.token = token
        self.usuario = usuario
        self.created_at = datetime.now()
        self.expires_at = self.created_at + timedelta(minutes=duracao_minutos)
        self.ativa = True

    def reiniciar_sessao(self):
        self.created_at = datetime.now()
        self.expires_at = self.created_at + timedelta(minutes=30)
        self.ativa = True

    def iniciar_sessao(self):
        self.reiniciar_sessao()  # mesma lógica

    def is_valida(self) -> bool:
        return self.ativa and datetime.now() < self.expires_at

    def encerrar_sessao(self):
        self.ativa = False


class Autenticador:
    __instancia = None

    def __init__(self):
        if Autenticador.__instancia is not None:
            raise Exception("Esta classe é um singleton! Use get_instancia().")
        self.sessoes_ativas: List[Sessao] = []

    @staticmethod
    def get_instancia():
        if Autenticador.__instancia is None:
            Autenticador.__instancia = Autenticador()
        return Autenticador.__instancia

    def autenticar_usuario(self, login: str, senha: str) -> Optional[str]:
        if login == "admin" and senha == "123":
            token = f"TOKEN-{login}-{datetime.now().timestamp()}"
            nova_sessao = Sessao(token, login)
            self.sessoes_ativas.append(nova_sessao)
            return token
        return None

    def terminar_sessao(self, login: str):
        for sessao in self.sessoes_ativas:
            if sessao.usuario == login:
                sessao.encerrar_sessao()

    def get_usuario_logado(self, login: str) -> Optional[str]:
        for sessao in self.sessoes_ativas:
            if sessao.usuario == login and sessao.is_valida():
                return login
        return None

    def validar_token(self, token: str) -> bool:
        for sessao in self.sessoes_ativas:
            if sessao.token == token and sessao.is_valida():
                return True
        return False