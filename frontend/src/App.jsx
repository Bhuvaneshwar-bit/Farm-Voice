import { useState, useCallback } from 'react'
import { Toaster, toast } from 'react-hot-toast'
import { motion, AnimatePresence } from 'framer-motion'
import { MapPin, RefreshCw, MessageSquare, Mic, Leaf } from 'lucide-react'

import Header from './components/Header'
import VoiceRecorder from './components/VoiceRecorder'
import ImageUpload from './components/ImageUpload'
import DiagnosisResult from './components/DiagnosisResult'
import FeedbackPanel from './components/FeedbackPanel'
import { diagnose } from './services/api'

const LANGUAGES = {
  ta: { name: 'Tamil',    tts_code: 'ta', native: 'தமிழ்'   },
  hi: { name: 'Hindi',   tts_code: 'hi', native: 'हिंदी'    },
  kn: { name: 'Kannada', tts_code: 'kn', native: 'ಕನ್ನಡ'   },
  te: { name: 'Telugu',  tts_code: 'te', native: 'తెలుగు'  },
  bn: { name: 'Bengali', tts_code: 'bn', native: 'বাংলা'   },
  mr: { name: 'Marathi', tts_code: 'mr', native: 'मराठी'   },
  en: { name: 'English', tts_code: 'en', native: 'English'  },
}

const CROP_OPTIONS = [
  'auto-detect', 'rice', 'wheat', 'tomato', 'potato', 'cotton',
  'maize', 'groundnut', 'sugarcane', 'brinjal', 'chilli',
  'onion', 'banana', 'mango', 'soybean', 'chickpea',
]

function LoadingSteps({ step }) {
  const steps = [
    { label: 'Transcribing audio...', icon: '🎙' },
    { label: 'Analyzing crop photo...', icon: '🔬' },
    { label: 'Checking weather data...', icon: '🌤' },
    { label: 'Searching knowledge base...', icon: '📚' },
    { label: 'Generating diagnosis...', icon: '🧠' },
    { label: 'Preparing audio response...', icon: '🔊' },
  ]

  return (
    <div className="card space-y-3">
      <div className="flex items-center justify-center gap-2 mb-2">
        <div className="w-6 h-6 border-3 border-farm-600 border-t-transparent rounded-full animate-spin" />
        <span className="font-semibold text-farm-700">Analyzing your crop...</span>
      </div>
      {steps.map((s, i) => (
        <div
          key={i}
          className={`flex items-center gap-3 text-sm transition-all duration-300 ${
            i < step ? 'text-farm-600 opacity-100' : i === step ? 'text-gray-800 font-medium' : 'text-gray-300'
          }`}
        >
          <span className={`text-base ${i < step ? 'opacity-100' : i === step ? 'animate-bounce' : 'opacity-20'}`}>
            {i < step ? '✅' : s.icon}
          </span>
          {s.label}
        </div>
      ))}
    </div>
  )
}

export default function App() {
  const [language, setLanguage] = useState('auto')
  const [cropType, setCropType] = useState('auto-detect')
  const [audioBase64, setAudioBase64] = useState(null)
  const [textInput, setTextInput] = useState('')
  const [imageBase64, setImageBase64] = useState(null)
  const [imagePreview, setImagePreview] = useState(null)
  const [useLocation, setUseLocation] = useState(false)
  const [location, setLocation] = useState(null)
  const [loading, setLoading] = useState(false)
  const [loadingStep, setLoadingStep] = useState(0)
  const [result, setResult] = useState(null)
  const [useTextMode, setUseTextMode] = useState(false)

  const handleAudioCaptured = useCallback(base64 => {
    setAudioBase64(base64)
    toast.success('Voice recorded! Tap "Analyze" to diagnose.')
  }, [])

  const handleImageCaptured = useCallback((base64, preview) => {
    setImageBase64(base64)
    setImagePreview(preview)
  }, [])

  const requestLocation = async () => {
    if (!navigator.geolocation) return toast.error('Location not supported on this device')
    navigator.geolocation.getCurrentPosition(
      pos => {
        setLocation({ lat: pos.coords.latitude, lng: pos.coords.longitude })
        setUseLocation(true)
        toast.success('Location enabled!')
      },
      () => {
        toast.error('Could not get location')
        setUseLocation(false)
      }
    )
  }

  const simulateLoadingSteps = () => {
    const delays = [0, 800, 1400, 1900, 2400, 3200]
    delays.forEach((delay, i) => {
      setTimeout(() => setLoadingStep(i), delay)
    })
  }

  const handleAnalyze = async () => {
    if (!audioBase64 && !textInput.trim()) {
      return toast.error('Please record a voice message or type your crop problem.')
    }

    setLoading(true)
    setLoadingStep(0)
    setResult(null)
    simulateLoadingSteps()

    try {
      const data = await diagnose({
        audioBase64: audioBase64 || undefined,
        textInput: textInput.trim() || undefined,
        imageBase64: imageBase64 || undefined,
        latitude: location?.lat,
        longitude: location?.lng,
        language,
        cropType: cropType !== 'auto-detect' ? cropType : undefined,
      })
      setResult(data)
      window.scrollTo({ top: 0, behavior: 'smooth' })
    } catch (err) {
      const msg = err.response?.data?.detail || 'Analysis failed. Please check your connection and try again.'
      toast.error(msg)
    } finally {
      setLoading(false)
    }
  }

  const handleReset = () => {
    setAudioBase64(null)
    setTextInput('')
    setImageBase64(null)
    setImagePreview(null)
    setResult(null)
    setLoadingStep(0)
  }

  const hasInput = audioBase64 || textInput.trim()

  return (
    <div className="min-h-dvh bg-farm-50 flex flex-col">
      <Toaster
        position="top-center"
        toastOptions={{
          style: { fontSize: '14px', borderRadius: '12px', maxWidth: '340px' },
        }}
      />

      <Header language={language} onLanguageChange={setLanguage} languages={LANGUAGES} />

      <main className="flex-1 max-w-lg mx-auto w-full px-4 py-5 space-y-4">

        {/* ── Results view ────────────────────────────────────────── */}
        <AnimatePresence mode="wait">
          {result ? (
            <motion.div
              key="result"
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              className="space-y-4"
            >
              <div className="flex items-center justify-between">
                <h2 className="font-bold text-lg text-gray-800">Diagnosis Complete</h2>
                <button
                  onClick={handleReset}
                  className="flex items-center gap-1.5 text-sm text-farm-600 font-medium bg-farm-50 border border-farm-200 px-3 py-1.5 rounded-xl hover:bg-farm-100 active:scale-95 transition-all"
                >
                  <RefreshCw className="w-3.5 h-3.5" />
                  New Query
                </button>
              </div>

              <DiagnosisResult result={result} />
              <FeedbackPanel sessionId={result.session_id} />
            </motion.div>
          ) : (
            <motion.div
              key="input"
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              className="space-y-4"
            >

              {/* Loading state */}
              {loading ? (
                <LoadingSteps step={loadingStep} />
              ) : (
                <>
                  {/* Hero prompt */}
                  <div className="text-center py-2">
                    <div className="text-4xl mb-2">🌾</div>
                    <h2 className="text-xl font-bold text-gray-800">What's wrong with your crop?</h2>
                    <p className="text-gray-500 text-sm mt-1">
                      Describe in your language — Tamil, Hindi, Kannada, or English
                    </p>
                  </div>

                  {/* Input mode toggle */}
                  <div className="flex bg-white border border-farm-200 rounded-2xl p-1 gap-1">
                    <button
                      onClick={() => setUseTextMode(false)}
                      className={`flex-1 flex items-center justify-center gap-2 py-2.5 rounded-xl text-sm font-medium transition-all ${
                        !useTextMode ? 'bg-farm-600 text-white shadow-sm' : 'text-gray-500 hover:text-gray-700'
                      }`}
                    >
                      <Mic className="w-4 h-4" /> Voice
                    </button>
                    <button
                      onClick={() => setUseTextMode(true)}
                      className={`flex-1 flex items-center justify-center gap-2 py-2.5 rounded-xl text-sm font-medium transition-all ${
                        useTextMode ? 'bg-farm-600 text-white shadow-sm' : 'text-gray-500 hover:text-gray-700'
                      }`}
                    >
                      <MessageSquare className="w-4 h-4" /> Type
                    </button>
                  </div>

                  {/* Voice recorder */}
                  {!useTextMode && (
                    <div className="card flex flex-col items-center py-8 gap-2">
                      <VoiceRecorder onAudioCaptured={handleAudioCaptured} disabled={loading} />
                      {audioBase64 && (
                        <div className="mt-3 text-xs text-farm-600 bg-farm-50 border border-farm-200 px-3 py-1.5 rounded-xl font-medium">
                          ✓ Voice recorded — ready to analyze
                        </div>
                      )}
                    </div>
                  )}

                  {/* Text input */}
                  {useTextMode && (
                    <div className="card">
                      <label className="block text-xs font-semibold text-gray-500 mb-2">
                        Describe your crop problem
                      </label>
                      <textarea
                        value={textInput}
                        onChange={e => setTextInput(e.target.value)}
                        placeholder="Example: My tomato leaves are turning yellow at the edges and have brown spots with rings. Some leaves are falling off."
                        className="w-full text-sm border border-gray-200 rounded-xl px-3 py-2.5 resize-none focus:outline-none focus:ring-2 focus:ring-farm-400 bg-gray-50 min-h-[100px]"
                        maxLength={500}
                      />
                      <p className="text-xs text-gray-400 mt-1 text-right">{textInput.length}/500</p>
                    </div>
                  )}

                  {/* Crop selector */}
                  <div className="card">
                    <label className="block text-xs font-semibold text-gray-500 mb-2">
                      Crop Type <span className="font-normal text-gray-400">(optional — helps accuracy)</span>
                    </label>
                    <div className="flex flex-wrap gap-2">
                      {CROP_OPTIONS.slice(0, 8).map(crop => (
                        <button
                          key={crop}
                          onClick={() => setCropType(crop)}
                          className={`px-3 py-1.5 rounded-xl text-xs font-medium border transition-all active:scale-95 ${
                            cropType === crop
                              ? 'bg-farm-600 text-white border-farm-600'
                              : 'bg-white text-gray-600 border-gray-200 hover:border-farm-300 hover:text-farm-600'
                          }`}
                        >
                          {crop === 'auto-detect' ? '🔍 Auto' : crop}
                        </button>
                      ))}
                    </div>
                    <div className="flex flex-wrap gap-2 mt-2">
                      {CROP_OPTIONS.slice(8).map(crop => (
                        <button
                          key={crop}
                          onClick={() => setCropType(crop)}
                          className={`px-3 py-1.5 rounded-xl text-xs font-medium border transition-all active:scale-95 ${
                            cropType === crop
                              ? 'bg-farm-600 text-white border-farm-600'
                              : 'bg-white text-gray-600 border-gray-200 hover:border-farm-300 hover:text-farm-600'
                          }`}
                        >
                          {crop}
                        </button>
                      ))}
                    </div>
                  </div>

                  {/* Photo upload */}
                  <div className="card">
                    <label className="block text-xs font-semibold text-gray-500 mb-2">
                      Crop Photo <span className="font-normal text-gray-400">(optional — improves diagnosis)</span>
                    </label>
                    <ImageUpload
                      onImageCaptured={handleImageCaptured}
                      imagePreview={imagePreview}
                      disabled={loading}
                    />
                  </div>

                  {/* Location */}
                  <button
                    onClick={useLocation ? () => { setUseLocation(false); setLocation(null) } : requestLocation}
                    className={`w-full flex items-center justify-between p-3.5 rounded-2xl border-2 transition-all ${
                      useLocation
                        ? 'bg-farm-50 border-farm-300 text-farm-700'
                        : 'bg-white border-gray-200 text-gray-600 hover:border-farm-200'
                    }`}
                  >
                    <div className="flex items-center gap-2.5">
                      <MapPin className={`w-4 h-4 ${useLocation ? 'text-farm-600' : 'text-gray-400'}`} />
                      <div className="text-left">
                        <p className="text-sm font-medium">
                          {useLocation ? 'Location enabled' : 'Enable location'}
                        </p>
                        <p className="text-xs text-gray-400">
                          {useLocation && location
                            ? `${location.lat.toFixed(3)}°N, ${location.lng.toFixed(3)}°E`
                            : 'For weather-aware diagnosis'
                          }
                        </p>
                      </div>
                    </div>
                    <div className={`w-5 h-5 rounded-full border-2 flex items-center justify-center transition-all ${
                      useLocation ? 'bg-farm-600 border-farm-600' : 'border-gray-300'
                    }`}>
                      {useLocation && <div className="w-2 h-2 bg-white rounded-full" />}
                    </div>
                  </button>

                  {/* Analyze button */}
                  <button
                    onClick={handleAnalyze}
                    disabled={!hasInput || loading}
                    className="btn-primary w-full text-base py-5"
                  >
                    {loading ? (
                      <span className="flex items-center justify-center gap-2">
                        <div className="w-5 h-5 border-2 border-white/50 border-t-white rounded-full animate-spin" />
                        Analyzing...
                      </span>
                    ) : (
                      <span className="flex items-center justify-center gap-2">
                        <Leaf className="w-5 h-5" />
                        Diagnose My Crop
                      </span>
                    )}
                  </button>

                  {!hasInput && (
                    <p className="text-center text-xs text-gray-400">
                      Record a voice message or type to begin
                    </p>
                  )}
                </>
              )}
            </motion.div>
          )}
        </AnimatePresence>
      </main>

      <footer className="text-center text-xs text-gray-400 py-4 px-4">
        FarmVoice — AI assistance, not a substitute for local agronomist advice
      </footer>
    </div>
  )
}
