document.addEventListener("DOMContentLoaded", async () => {
  marcarNavAtiva("home");
  await carregarCabecalho();

  try {
    const site = await apiGet("/api/site");

    document.querySelector("[data-eyebrow]").textContent = site.tagline;
    document.querySelector("[data-role]").textContent = site.papel;
  } catch (erro) {
    console.error("Não foi possível carregar os dados da página inicial:", erro);
  }
});
