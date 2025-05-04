// static/calendarApp/js/weather.js
document.addEventListener("DOMContentLoaded", () => {
    console.log("JavaScript is connected!");

    const csrfToken = document.querySelector('meta[name="csrf-token"]')?.getAttribute('content');
    const weatherWidget = document.querySelector("#weather-widget");
    const city = weatherWidget?.dataset.city;

    // Use geolocation if city data is missing
    if (!city) {
        console.log("City data not found, fetching location...");

        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition((position) => {
                const lat = position.coords.latitude;
                const lon = position.coords.longitude;

                // Make an API request to get the city name based on coordinates
                fetch(`https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${csrfToken}&units=metric`)
                    .then(response => response.json())
                    .then(data => {
                        const city = data.name;
                        weatherWidget.dataset.city = city; // Update the dataset

                        // Send the updated city to your backend
                        fetch("/widgets/weather/update/", {
                            method: "POST",
                            headers: {
                                "Content-Type": "application/json",
                                "X-CSRFToken": csrfToken,
                            },
                            body: JSON.stringify({ city: city }),
                        })
                        .then(response => response.json())
                        .then(data => {
                            console.log("City updated:", data);
                        })
                        .catch(error => {
                            console.error("Error sending city data:", error);
                        });
                    });
            });
        } else {
            console.warn("Geolocation is not supported by this browser.");
        }
    }
});