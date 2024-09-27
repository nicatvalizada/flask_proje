document.addEventListener("DOMContentLoaded", function () {
  const resetButton = document.querySelector("button[type='reset']");
  const resultDiv = document.querySelector(".result");

  resetButton.addEventListener("click", function () {
    if (resultDiv) {
      resultDiv.style.display = "none";
      const resultParagraph = resultDiv.querySelector("p");
      if (resultParagraph) {
        resultParagraph.innerHTML = "";
      }
    }
  });
});
