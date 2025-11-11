// Theme switcher functionality
const themes = ["auto", "light", "dark"];
const themeIcons = {
  auto: "fa-circle-half-stroke",
  light: "fa-sun",
  dark: "fa-moon",
};

const switchTheme = (theme) => {
  if (theme === "auto") {
    document.documentElement.removeAttribute("data-theme");
  } else {
    document.documentElement.setAttribute("data-theme", theme);
  }

  // Save preference
  localStorage.setItem("theme", theme);

  // Update button icon
  const themeBtn = document.getElementById("theme-toggle");
  if (themeBtn) {
    const icon = themeBtn.querySelector("i");
    if (icon) {
      icon.className = `fa-solid ${themeIcons[theme]}`;
    }
    themeBtn.title = `Tema: ${theme}`;
  }
};

// Toggle theme function
const toggleTheme = () => {
  const currentTheme = localStorage.getItem("theme") || "auto";
  const currentIndex = themes.indexOf(currentTheme);
  const nextIndex = (currentIndex + 1) % themes.length;
  const nextTheme = themes[nextIndex];
  switchTheme(nextTheme);
};

// Load saved theme or default to auto
const savedTheme = localStorage.getItem("theme") || "auto";
switchTheme(savedTheme);

// Add click listener to toggle button when DOM is ready
document.addEventListener("DOMContentLoaded", () => {
  const themeToggle = document.getElementById("theme-toggle");
  if (themeToggle) {
    themeToggle.addEventListener("click", toggleTheme);
  }
});
