<body>

<h1>Weather Forecast App</h1>
<p>A command-line weather forecast application built with Python that allows users to check daily, hourly, and weekly weather forecasts for a specified location.</p>

<h2>Features</h2>
<ul>
    <li>Get <strong>daily</strong>, <strong>hourly</strong>, and <strong>weekly</strong> weather forecasts for any location.</li>
    <li>Data includes temperature, wind speed, and precipitation type.</li>
    <li>Simple, interactive CLI interface.</li>
</ul>

<h2>Usage</h2>
<p>Run the application and follow the prompts to get weather information for a chosen location:</p>
<pre><code>python main.py</code></pre>

<h3>1. Location Entry</h3>
<p>Upon startup, you will be prompted to enter a location:</p>
<pre><code>Enter The Location (Example: London): istanbul</code></pre>

<h3>2. Select Forecast Type</h3>
<p>Select the type of forecast you want to view:</p>
<pre><code>Daily weather : 1 
Weekly weather : 2
Exit: 3
Your choice: 2</code></pre>

<h2>Sample Outputs</h2>

<h3>Daily Weather Forecast</h3>
<p>When you select daily weather, enter the date to view the forecast for a specific day.</p>
<pre><code>Enter date to see weather forecast (Example: 2024-11-08): 2024-10-27

DAILY WEATHER
+------------+---------+-------------+--------------+
| date       |   temp  | windspeed   | preciptype   |
+============+=========+=============+==============+
| 2024-10-27 | 15.1111 | 16.1        |              |
+------------+---------+-------------+--------------+</code></pre>

<h3>Hourly Weather Forecast</h3>
<p>To view the weather forecast for a specific hour, enter the desired hour.</p>
<pre><code>Enter the time to see the weather hourly, otherwise leave blank (Example: 05): 06

HOURLY WEATHER
+------------+---------+-------------+--------------+
| time       |   temp  | windspeed   | preciptype   |
+============+=========+=============+==============+
| 06:00:00   | 12.7222 | 11.7        |              |
+------------+---------+-------------+--------------+</code></pre>

<h3>Weekly Weather Forecast</h3>
<p>When you select weekly weather, a forecast for the entire week is displayed.</p>
<pre><code>WEEKLY WEATHER
+------------+---------+-------------+--------------+
| date       |   temp  | windspeed   | preciptype   |
+============+=========+=============+==============+
| 2024-10-27 | 15.1111 | 16.1        |              |
| 2024-10-28 | 13.8889 | 6.9         |              |
| 2024-10-29 | 15.5556 | 11          |              |
| 2024-10-30 | 15.6111 | 13          | ['rain']     |
| 2024-10-31 | 15.0556 | 13.6        | ['rain']     |
| 2024-11-01 | 15.2222 | 14.1        |              |
| 2024-11-02 | 15.2222 | 8.5         |              |
+------------+---------+-------------+--------------+</code></pre>

<h2>Requirements</h2>
<ul>
    <li>Python 3.x</li>
    <li>An API key from <a href="https://www.visualcrossing.com/weather-api" target="_blank">Visual Crossing Weather API</a></li>
    <li><strong>Redis:</strong> Redis must be installed and running on your system for caching weather data. You can download Redis from the <a href="https://redis.io/download" target="_blank">official Redis website</a>.</li>
</ul>
<p>You can obtain a free API key by signing up on the <a href="https://www.visualcrossing.com/weather-api" target="_blank">Visual Crossing website</a>
  . For Redis installation instructions, visit the <a href="https://redis.io/documentation" target="_blank">Redis documentation</a>.</p>


<h2>Installation</h2>
<ol>
    <li>Clone this repository:
        <pre><code>git clone https://github.com/Haknozer/WeatherApp.git</code></pre>
    </li>
</ol>

<h2>Contributing</h2>
<p>Contributions are welcome! Please fork the repository, create a new branch, and submit a pull request.</p>

</body>
