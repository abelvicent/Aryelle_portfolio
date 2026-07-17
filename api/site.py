"""Endpoint GET /api/site — dados gerais do site (nome, tagline, etc.)."""

import json
from http.server import BaseHTTPRequestHandler

DATA = {
    "nome": "Aryelle Araújo",
    "tagline": "arte & mídia — ufcg",
    "papel": "Estudante de Arte & Mídia na UFCG — construindo uma trajetória em direção de arte",
    "instagram": "https://www.instagram.com/aaryelle__/",
    "instagram_handle": "@aaryelle__",
    "universidade": "Universidade Federal de Campina Grande — UFCG",
    "cidade": "Campina Grande, PB",
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
