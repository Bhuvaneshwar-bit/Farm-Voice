import { Leaf } from 'lucide-react'

export default function Header({ language, onLanguageChange, languages }) {
  return (
    <header className="sticky top-0 z-20 bg-farm-700 text-white shadow-lg">
      <div className="max-w-lg mx-auto px-4 py-3 flex items-center justify-between">
        <div className="flex items-center gap-2">
          <div className="bg-white/20 rounded-xl p-1.5">
            <Leaf className="w-5 h-5" />
          </div>
          <div>
            <h1 className="font-bold text-lg leading-none">FarmVoice</h1>
            <p className="text-farm-200 text-xs">AI Crop Doctor</p>
          </div>
        </div>

        <select
          value={language}
          onChange={e => onLanguageChange(e.target.value)}
          className="bg-farm-800 border border-farm-500 text-white text-sm rounded-xl px-3 py-1.5 focus:outline-none focus:ring-2 focus:ring-farm-300"
        >
          <option value="auto">Auto Detect</option>
          {Object.entries(languages).map(([code, info]) => (
            <option key={code} value={code}>
              {info.native}
            </option>
          ))}
        </select>
      </div>
    </header>
  )
}
