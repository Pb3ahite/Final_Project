const apiKey = '2cefd0c60b70491e9d51a4e981b7015e';
const getWeatherButton = document.getElementById('getWeatherButton');
const locationInput = document.getElementById('locationInput');
const dateTimeInput = document.getElementById('dateTimeInput');
const weatherDataContainer = document.getElementById('weatherDataContainer');

getWeatherButton.addEventListener('click', () => {
    const location = locationInput.value;
         const currentWeatherURL = `https://api.openweathermap.org/data/2.5/weather?q=${location}&appid=${apiKey}`;

    fetch(currentWeatherURL)
        .then(response => response.json())
        .then(data => {
            console.log(data);
            const temperatureK = data.main.temp;
            const temperatureF = (temperatureK - 273.15) * 9/5 + 32;
            const forecast = data.weather[0].description;
            const humidity = data.main.humidity;
            const weatherDataHTML = `
                <p>Temperature: ${temperatureF.toFixed(2)} °F</p>
                <p>Forecast: ${forecast}</p>
                <p>Humidity: ${humidity}%</p>
            `;
            weatherDataContainer.innerHTML = weatherDataHTML;
        })
        .catch(error => {
            console.error('Error fetching current weather data:', error);
        });
});
