/**
 * Configuração central de acesso à API.
 * Caminho relativo: front e back ficam no mesmo domínio quando publicados
 * na Vercel, então não é preciso configurar nenhum endereço aqui.
 */
const API_BASE_URL = "";

/**
 * Busca um endpoint da API com tratamento de erro simples e seguro
 * (nunca injeta o erro cru na página, evitando vazamento de detalhes internos).
 */
async function apiGet(path) {
  const response = await fetch(`${API_BASE_URL}${path}`, {
    method: "GET",
    headers: { Accept: "application/json" },
  });

  if (!response.ok) {
    throw new Error(`Falha ao carregar ${path} (status ${response.status})`);
  }

  return response.json();
}

/** Marca o link de navegação da página atual como ativo. */
function marcarNavAtiva(paginaId) {
  document.querySelectorAll("nav a[data-page]").forEach((link) => {
    if (link.dataset.page === paginaId) {
      link.classList.add("active");
    }
  });
}

/** Preenche o nome no cabeçalho (comum a todas as páginas) a partir da API. */
async function carregarCabecalho() {
  try {
    const site = await apiGet("/api/site");
    const marca = document.querySelector(".mark");
    if (marca) marca.textContent = site.nome;
    const footerNome = document.querySelector("[data-footer-nome]");
    if (footerNome) footerNome.textContent = site.nome;
    return site;
  } catch (erro) {
    console.error(erro);
    return null;
  }
}
