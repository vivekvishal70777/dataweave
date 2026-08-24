(function () {
  const slides = Array.from(document.querySelectorAll(".slide"));
  const counter = document.getElementById("counter");
  const bar = document.getElementById("progress");
  const notesEl = document.getElementById("notes");
  let i = Math.max(0, parseInt(location.hash.replace("#", ""), 10) - 1 || 0);

  function show(n) {
    i = Math.max(0, Math.min(slides.length - 1, n));
    slides.forEach((s, idx) => s.classList.toggle("active", idx === i));
    if (counter) counter.textContent = (i + 1) + " / " + slides.length;
    if (bar) bar.style.width = ((i + 1) / slides.length * 100) + "%";
    if (notesEl) {
      const note = slides[i].getAttribute("data-notes") || "";
      notesEl.querySelector("p").textContent = note;
      notesEl.style.display = notesEl.classList.contains("visible") && note ? "block" : "none";
    }
    history.replaceState(null, "", "#" + (i + 1));
  }

  document.addEventListener("keydown", (e) => {
    if (["INPUT", "TEXTAREA"].includes(e.target.tagName)) return;
    if (["ArrowRight", "PageDown", " ", "Enter"].includes(e.key)) {
      e.preventDefault();
      show(i + 1);
    } else if (["ArrowLeft", "PageUp", "Backspace"].includes(e.key)) {
      e.preventDefault();
      show(i - 1);
    } else if (e.key === "Home") show(0);
    else if (e.key === "End") show(slides.length - 1);
    else if (e.key === "f" || e.key === "F") {
      if (!document.fullscreenElement) document.documentElement.requestFullscreen();
      else document.exitFullscreen();
    } else if (e.key === "n" || e.key === "N") {
      if (!notesEl) return;
      notesEl.classList.toggle("visible");
      show(i);
    }
  });

  document.body.addEventListener("click", (e) => {
    if (e.target.closest("a, pre, .notes")) return;
    show(e.clientX > window.innerWidth * 0.22 ? i + 1 : i - 1);
  });

  show(i);
})();
