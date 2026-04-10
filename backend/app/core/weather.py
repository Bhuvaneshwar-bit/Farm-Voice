import httpx
from typing import Optional, Dict, Any
from app.core.config import settings


DISEASE_RISK_THRESHOLDS = {
    "high_humidity": 85,
    "rain_mm": 5,
    "temp_blight_range": (20, 30),
    "temp_rust_range": (15, 22),
}


def assess_disease_risk(temp: float, humidity: float, rainfall: float) -> str:
    risks = []
    if humidity > DISEASE_RISK_THRESHOLDS["high_humidity"]:
        risks.append("high humidity favors fungal diseases")
    if rainfall > DISEASE_RISK_THRESHOLDS["rain_mm"]:
        risks.append("recent rainfall increases blast and blight risk")
    if DISEASE_RISK_THRESHOLDS["temp_blight_range"][0] <= temp <= DISEASE_RISK_THRESHOLDS["temp_blight_range"][1]:
        risks.append("temperature range ideal for late blight")
    if DISEASE_RISK_THRESHOLDS["temp_rust_range"][0] <= temp <= DISEASE_RISK_THRESHOLDS["temp_rust_range"][1]:
        risks.append("cool temperatures favor rust diseases")
    if not risks:
        return "Weather conditions are relatively unfavorable for most diseases."
    return "Warning: " + "; ".join(risks) + "."


async def get_weather(latitude: float, longitude: float) -> Optional[Dict[str, Any]]:
    if not settings.OPENWEATHER_API_KEY:
        return None
    try:
        url = "https://api.openweathermap.org/data/2.5/weather"
        params = {
            "lat": latitude,
            "lon": longitude,
            "appid": settings.OPENWEATHER_API_KEY,
            "units": "metric",
        }
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(url, params=params)
            response.raise_for_status()
            data = response.json()

        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        rainfall = data.get("rain", {}).get("1h", 0)
        wind = data["wind"]["speed"]
        description = data["weather"][0]["description"]
        location_name = data.get("name", "Unknown location")

        return {
            "temperature": temp,
            "humidity": humidity,
            "rainfall_mm": rainfall,
            "wind_speed": wind,
            "description": description,
            "location_name": location_name,
            "disease_risk_note": assess_disease_risk(temp, humidity, rainfall),
        }
    except Exception:
        return None


def format_weather_for_prompt(weather: Optional[Dict]) -> str:
    if not weather:
        return "Weather data unavailable."
    return (
        f"Temperature: {weather['temperature']}°C, "
        f"Humidity: {weather['humidity']}%, "
        f"Rainfall: {weather['rainfall_mm']}mm, "
        f"Wind: {weather['wind_speed']} m/s, "
        f"Conditions: {weather['description']}. "
        f"{weather.get('disease_risk_note', '')}"
    )
