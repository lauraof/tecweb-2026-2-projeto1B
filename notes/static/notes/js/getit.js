function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

document.addEventListener("DOMContentLoaded", function () {
  // Faz textarea aumentar a altura automaticamente
  // Fonte: https://www.geeksforgeeks.org/how-to-create-auto-resize-textarea-using-javascript-jquery/#:~:text=It%20can%20be%20achieved%20by,height%20of%20an%20element%20automatically.
  let textareas = document.getElementsByClassName("autoresize");
  for (let i = 0; i < textareas.length; i++) {
    let textarea = textareas[i];
    function autoResize() {
      this.style.height = "auto";
      this.style.height = this.scrollHeight + "px";
    }

    textarea.addEventListener("input", autoResize, false);
  }

  // Sorteia classes de cores aleatoriamente para os cards
  let cards = document.getElementsByClassName("card");
  for (let i = 0; i < cards.length; i++) {
    let card = cards[i];
    card.className += ` card-color-${getRandomInt(
      1,
      5
    )} card-rotation-${getRandomInt(1, 11)}`;
  }
  // Lógica dos botões Salvar/Cancelar na página de editar e index 
const formNota = document.querySelector(".form-card");
  const btnCancelar = document.querySelector(".btn-cinza");

  // Funciona no index e no edit
  if (formNota) {
    formNota.addEventListener("submit", function (event) {
      const campoTitulo = formNota.querySelector('[name="titulo"]');
      const campoDetalhes = formNota.querySelector('[name="detalhes"]');

      const titulo = campoTitulo.value.trim();
      const detalhes = campoDetalhes.value.trim();

      if (titulo === "" || detalhes === "") {
        event.preventDefault();

        alert("Preencha o título e o conteúdo antes de salvar.");

        if (titulo === "") {
          campoTitulo.focus();
        } else {
          campoDetalhes.focus();
        }
      }
    });
  }  // Lógica do botão Não na página de deletar
const btnNao = document.querySelector(".btn-nao");

if (btnNao) {
    btnNao.addEventListener("click", function () {
        window.location.href = "/";
    });
}
});
