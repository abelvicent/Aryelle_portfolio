"""Endpoint GET /api/sobre — conteúdo da página Sobre."""

import json
from http.server import BaseHTTPRequestHandler

DATA = {
    "paragrafos": [
        "Aryelle é estudante de Arte & Mídia na Universidade Federal de Campina Grande (UFCG), onde vem descobrindo sua voz como diretora de arte. Curiosa por natureza, se interessa pelo que acontece nos bastidores de uma produção: a construção de cenário, a escolha de figurino, a composição de cada quadro.",
        "Ainda no começo da trajetória, já esteve envolvida com produções teatrais estudantis dentro da própria faculdade — experiências que despertaram seu olhar para a direção de arte como profissão.",
    ],
    "onde_estuda": "Universidade Federal de Campina Grande — UFCG",
    "areas": ["Direção de Arte", "Cenografia", "Figurino", "Teatro Universitário"],
}


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = json.dumps(DATA, ensure_ascii=False).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("X-Frame-Options", "DENY")
        self.send_header("Referrer-Policy", "no-referrer-when-downgrade")
        self.send_header("Cache-Control", "public, max-age=60")
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        return
