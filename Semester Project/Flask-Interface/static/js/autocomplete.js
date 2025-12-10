let currentFocus = -1;

// Close suggestions
function closeAllLists(except) {
    const items = document.getElementsByClassName("autocomplete-items");
    for (let i = 0; i < items.length; i++) {
        if (except !== items[i] && except !== cityInput) {
            items[i].parentNode.removeChild(items[i]);
        }
    }
}

// Fetch cities from OpenWeatherMap
async function fetchCities(query, apiKey) {
    if (!query) return [];
    const limit = 5;
    const url = `https://api.openweathermap.org/geo/1.0/direct?q=${encodeURIComponent(query)}&limit=${limit}&appid=${apiKey}`;
    try {
        const response = await fetch(url);
        if (!response.ok) throw new Error("Network response not ok");
        const data = await response.json();
        return data; // Array of city objects
    } catch (err) {
        console.error("Error fetching cities:", err);
        return [];
    }
}

// Main autocomplete function
function autocomplete(inp, apiKey) {
    inp.addEventListener("input", async function () {
        const val = this.value;
        closeAllLists();
        if (!val) return;

        currentFocus = -1;

        const a = document.createElement("DIV");
        a.setAttribute("id", this.id + "-autocomplete-list");
        a.setAttribute("class", "autocomplete-items");
        this.parentNode.appendChild(a);

        const cities = await fetchCities(val, apiKey);

        cities.forEach(city => {
            const display = city.state ? `${city.name}, ${city.state}, ${city.country}` : `${city.name}, ${city.country}`;
            const b = document.createElement("DIV");
            b.innerHTML = `<strong>${city.name.substr(0, val.length)}</strong>${city.name.substr(val.length)}`;
            if (city.state) b.innerHTML += `, ${city.state}, ${city.country}`;
            else b.innerHTML += `, ${city.country}`;
            b.innerHTML += `<input type='hidden' value='${display}'>`;
            b.addEventListener("click", function () {
                inp.value = this.getElementsByTagName("input")[0].value;
                closeAllLists();
            });
            a.appendChild(b);
        });
    });

    inp.addEventListener("keydown", function (e) {
        let x = document.getElementById(this.id + "-autocomplete-list");
        if (x) x = x.getElementsByTagName("div");
        if (e.keyCode === 40) { currentFocus++; addActive(x); }
        else if (e.keyCode === 38) { currentFocus--; addActive(x); }
        else if (e.keyCode === 13) { e.preventDefault(); if (currentFocus > -1) if (x) x[currentFocus].click(); }
    });

    function addActive(x) {
        if (!x) return false;
        removeActive(x);
        if (currentFocus >= x.length) currentFocus = 0;
        if (currentFocus < 0) currentFocus = x.length - 1;
        x[currentFocus].classList.add("autocomplete-active");
    }

    function removeActive(x) {
        for (let i = 0; i < x.length; i++) x[i].classList.remove("autocomplete-active");
    }

    document.addEventListener("click", function (e) { closeAllLists(e.target); });
}
