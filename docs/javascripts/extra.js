// Ouvrir uniquement les PDF et Excel dans un nouvel onglet
document.addEventListener("DOMContentLoaded", function () {
  var links = document.querySelectorAll("a[href]");
  links.forEach(function (link) {
    var href = link.getAttribute("href");
    if (href && (href.endsWith(".pdf") || href.endsWith(".xlsx"))) {
      link.setAttribute("target", "_blank");
      link.setAttribute("rel", "noopener noreferrer");
    }
  });
});
