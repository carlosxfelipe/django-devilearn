function setLogoByTheme() {
  const logo = document.getElementById("logo-devilearn");
  if (!logo) return;
  const isDark =
    document.documentElement.getAttribute("data-theme") === "dark" ||
    (window.matchMedia &&
      window.matchMedia("(prefers-color-scheme: dark)").matches &&
      !document.documentElement.getAttribute("data-theme"));
  logo.src = isDark ? logo.dataset.dark : logo.dataset.light;
}
setLogoByTheme();
window
  .matchMedia("(prefers-color-scheme: dark)")
  .addEventListener("change", setLogoByTheme);
const themeToggle = document.getElementById("theme-toggle");
if (themeToggle) {
  themeToggle.addEventListener("click", function () {
    setTimeout(setLogoByTheme, 100);
  });
}
document.addEventListener("DOMContentLoaded", setLogoByTheme);
