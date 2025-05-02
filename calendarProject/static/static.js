document.addEventListener("DOMContentLoaded", function () {
    // Placeholder for interactivity, like toggling forms or sending async requests
    console.log("Widgets JS loaded.");

    // Example: toggle show/hide for widget sections
    document.querySelectorAll(".widget-toggle").forEach(button => {
        button.addEventListener("click", () => {
            const content = button.nextElementSibling;
            if (content.style.display === "none") {
                content.style.display = "block";
                button.textContent = "Hide";
            } else {
                content.style.display = "none";
                button.textContent = "Show";
            }
        });
    });
});