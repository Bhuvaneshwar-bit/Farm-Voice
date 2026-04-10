import { Thermometer, Droplets, Wind, CloudRain, AlertTriangle } from 'lucide-react'

export default function WeatherWidget({ weather }) {
  if (!weather) return null

  const urgentNote = weather.disease_risk_note?.startsWith('Warning')

  return (
    <div className={`rounded-2xl p-4 border ${urgentNote ? 'bg-amber-50 border-amber-200' : 'bg-blue-50 border-blue-100'}`}>
      <div className="flex items-center justify-between mb-3">
        <h3 className="text-sm font-semibold text-gray-700 flex items-center gap-1.5">
          <CloudRain className="w-4 h-4 text-blue-500" />
          Weather Context
        </h3>
        {weather.location_name && (
          <span className="text-xs text-gray-500">{weather.location_name}</span>
        )}
      </div>

      <div className="grid grid-cols-3 gap-3 mb-3">
        {weather.temperature != null && (
          <div className="flex flex-col items-center">
            <Thermometer className="w-4 h-4 text-orange-500 mb-1" />
            <span className="text-sm font-bold">{Math.round(weather.temperature)}°C</span>
            <span className="text-xs text-gray-500">Temp</span>
          </div>
        )}
        {weather.humidity != null && (
          <div className="flex flex-col items-center">
            <Droplets className="w-4 h-4 text-blue-500 mb-1" />
            <span className="text-sm font-bold">{weather.humidity}%</span>
            <span className="text-xs text-gray-500">Humidity</span>
          </div>
        )}
        {weather.wind_speed != null && (
          <div className="flex flex-col items-center">
            <Wind className="w-4 h-4 text-gray-500 mb-1" />
            <span className="text-sm font-bold">{weather.wind_speed} m/s</span>
            <span className="text-xs text-gray-500">Wind</span>
          </div>
        )}
      </div>

      {weather.disease_risk_note && (
        <div className={`flex items-start gap-2 text-xs rounded-xl p-2.5 ${urgentNote ? 'bg-amber-100 text-amber-800' : 'bg-blue-100 text-blue-800'}`}>
          {urgentNote && <AlertTriangle className="w-3.5 h-3.5 flex-shrink-0 mt-0.5" />}
          <span>{weather.disease_risk_note}</span>
        </div>
      )}
    </div>
  )
}
