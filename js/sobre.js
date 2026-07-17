document.addEventListener("DOMContentLoaded", async () => {
  marcarNavAtiva("sobre");
  await carregarCabecalho();

  try {
    const sobre = await apiGet("/api/sobre");

    const container = document.querySelector("[data-paragrafos]");
    container.innerHTML = "";
    sobre.paragrafos.forEach((texto) => {
      const p = document.createElement("p");
      p.textContent = texto;
      container.appendChild(p);
    });

    document.querySelector("[data-onde-estuda]").textContent = sobre.onde_estuda;

    const tools = document.querySelector("[data-areas]");
    tools.innerHTML = "";
    sobre.areas.forEach((area) => {
      const span = document.createElement("span");
      span.textContent = area;
      tools.appendChild(span);
    });
  } catch (erro) {
    console.error("Não foi possível carregar a página Sobre:", erro);
  }
});
