"""Endpoint GET /api/em_breve — conteúdo da página Em Breve."""

import json
from http.server import BaseHTTPRequestHandler

DATA = {
    "titulo": "Ainda não há produções fotografadas — e tudo bem.",
    "texto": "Este espaço está reservado para os primeiros trabalhos de Aryelle como diretora de arte: registros de cenografia, figurino e produções teatrais que estão por vir. À medida que novos projetos ganharem forma, eles serão documentados aqui, prancha por prancha.",
    "tags": ["Próxima produção — em breve", "Registro fotográfico — em breve"],
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
