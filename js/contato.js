document.addEventListener("DOMContentLoaded", async () => {
  marcarNavAtiva("contato");
  await carregarCabecalho();

  try {
    const contato = await apiGet("/api/contato");

    const linkInsta = document.querySelector("[data-instagram]");
    linkInsta.href = contato.instagram;
    linkInsta.textContent = contato.instagram_handle;

    document.querySelector("[data-area]").textContent = contato.area;
    document.querySelector("[data-cidade]").textContent = contato.cidade;
    document.querySelector("[data-universidade]").textContent = contato.universidade;
  } catch (erro) {
    console.error("Não foi possível carregar a página Contato:", erro);
  }
});
