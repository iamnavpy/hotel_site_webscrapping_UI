const residenceSelect = document.getElementById("residence");
const bookingPeriodSelect = document.getElementById("booking_period");
const ensuiteCheckbox = document.getElementById("ensuite_checkbox");
const scrapeButton = document.getElementById("scrape-button");
const resultsDiv = document.getElementById("results");

scrapeButton.addEventListener("click", async () => {
    const residence = residenceSelect.value;
    const bookingPeriod = bookingPeriodSelect.value;
    const ensuite = ensuiteCheckbox.checked;

    // Send user input to server using AJAX or fetch API
    // For security, avoid sending data directly in the URL
    const response = await fetch("/scrape", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ residence, bookingPeriod, ensuite })
    });

    if (response.ok) {
        const data = await response.json();

    } else {
        alert("Error scraping data
