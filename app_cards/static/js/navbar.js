
/* navbar */
document.addEventListener("DOMContentLoaded", function () {
    var toggler = document.querySelector(".navbar-toggler");
    var navbarNav = document.querySelector(".navbar-collapse");
  
    document.addEventListener("click", function (event) {
      if (event.target !== toggler && !navbarNav.contains(event.target)) {
        if (!navbarNav.classList.contains("show")) {
          return;
        }
        var bootstrapNavbar = new bootstrap.Collapse(navbarNav, { toggle: false });
        bootstrapNavbar.hide();
      }
    });
  });
  