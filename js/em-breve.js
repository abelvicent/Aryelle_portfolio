document.addEventListener("DOMContentLoaded", async () => {
  marcarNavAtiva("em-breve");
  await carregarCabecalho();

  try {
    const emBreve = await apiGet("/api/em_breve");

    document.querySelector("[data-titulo]").textContent = emBreve.titulo;
    document.querySelector("[data-texto]").textContent = emBreve.texto;

    const tags = document.querySelector("[data-tags]");
    tags.innerHTML = "";
    emBreve.tags.forEach((tag) => {
      const span = document.createElement("span");
      span.textContent = tag;
      tags.appendChild(span);
    });
  } catch (erro) {
    console.error("Não foi possível carregar a página Em Breve:", erro);
  }
});
