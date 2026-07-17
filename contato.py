"""Endpoint GET /api/contato — conteúdo da página Contato."""

import json
from http.server import BaseHTTPRequestHandler

DATA = {
    "instagram": "https://www.instagram.com/aaryelle__/",
    "instagram_handle": "@aaryelle__",
    "area": "Arte & Mídia",
    "cidade": "Campina Grande, PB",
    "universidade": "Universidade Federal de Campina Grande — UFCG",
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
