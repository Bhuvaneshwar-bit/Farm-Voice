import { useState, useRef } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import {
  AlertTriangle, CheckCircle, ChevronDown, ChevronUp,
  Leaf, FlaskConical, Sprout, ShieldCheck,
  PlayCircle, PauseCircle, Info, Zap, Clock
} from 'lucide-react'
import WeatherWidget from './WeatherWidget'

const URGENCY_CONFIG = {
  critical: { color: 'text-red-600', bg: 'bg-red-50', border: 'border-red-200', label: 'CRITICAL', icon: AlertTriangle },
  high:     { color: 'text-orange-600', bg: 'bg-orange-50', border: 'border-orange-200', label: 'HIGH', icon: AlertTriangle },
  medium:   { color: 'text-yellow-600', bg: 'bg-yellow-50', border: 'border-yellow-200', label: 'MEDIUM', icon: Info },
  low:      { color: 'text-green-600', bg: 'bg-green-50', border: 'border-green-200', label: 'LOW', icon: CheckCircle },
}

const SEVERITY_LABELS = ['', 'Very Mild', 'Mild', 'Moderate', 'Severe', 'Critical']

function SeverityBar({ severity }) {
  const colors = ['', 'bg-green-400', 'bg-lime-400', 'bg-yellow-400', 'bg-orange-500', 'bg-red-500']
  return (
    <div className="flex items-center gap-1.5">
      {[1, 2, 3, 4, 5].map(i => (
        <div
          key={i}
          className={`h-2.5 flex-1 rounded-full transition-all ${i <= severity ? colors[severity] : 'bg-gray-200'}`}
        />
      ))}
      <span className="text-xs font-medium text-gray-600 ml-1 whitespace-nowrap">
        {SEVERITY_LABELS[severity]}
      </span>
    </div>
  )
}

function ConfidenceMeter({ confidence }) {
  const color = confidence >= 80 ? 'bg-farm-500' : confidence >= 60 ? 'bg-yellow-500' : 'bg-orange-400'
  return (
    <div className="flex items-center gap-2">
      <div className="flex-1 bg-gray-100 rounded-full h-2">
        <motion.div
          className={`h-2 rounded-full ${color}`}
          initial={{ width: 0 }}
          animate={{ width: `${confidence}%` }}
          transition={{ duration: 0.8, ease: 'easeOut', delay: 0.3 }}
        />
      </div>
      <span className="text-sm font-bold text-gray-700">{confidence}%</span>
    </div>
  )
}

function AudioPlayer({ audioBase64, responseText }) {
  const [playing, setPlaying] = useState(false)
  const audioRef = useRef(null)

  const toggle = () => {
    if (!audioRef.current) {
      const audio = new Audio(`data:audio/mp3;base64,${audioBase64}`)
      audio.onended = () => setPlaying(false)
      audioRef.current = audio
    }
    if (playing) {
      audioRef.current.pause()
      setPlaying(false)
    } else {
      audioRef.current.play()
      setPlaying(true)
    }
  }

  return (
    <div className="bg-farm-50 border border-farm-200 rounded-2xl p-3.5 flex items-center gap-3">
      <button onClick={toggle} className="text-farm-600 hover:text-farm-700 active:scale-90 transition-all flex-shrink-0">
        {playing
          ? <PauseCircle className="w-10 h-10" />
          : <PlayCircle className="w-10 h-10" />
        }
      </button>
      <div className="flex-1 min-w-0">
        <p className="text-xs font-semibold text-farm-700 mb-1">Audio Diagnosis</p>
        <p className="text-xs text-gray-500 line-clamp-2">{responseText}</p>
      </div>
    </div>
  )
}

function TreatmentSection({ icon: Icon, title, items, accent }) {
  const [open, setOpen] = useState(title === 'Immediate Actions')
  if (!items || items.length === 0) return null

  const accentClasses = {
    red: 'bg-red-50 border-red-100 text-red-700',
    green: 'bg-green-50 border-green-100 text-green-700',
    blue: 'bg-blue-50 border-blue-100 text-blue-700',
    purple: 'bg-purple-50 border-purple-100 text-purple-700',
  }

  return (
    <div className={`rounded-2xl border ${accentClasses[accent].split(' ').slice(1).join(' ')} overflow-hidden`}>
      <button
        onClick={() => setOpen(!open)}
        className={`w-full flex items-center justify-between p-3.5 ${accentClasses[accent].split(' ')[0]}`}
      >
        <div className="flex items-center gap-2">
          <Icon className={`w-4 h-4 ${accentClasses[accent].split(' ')[2]}`} />
          <span className={`text-sm font-semibold ${accentClasses[accent].split(' ')[2]}`}>{title}</span>
          <span className={`text-xs px-1.5 py-0.5 rounded-full bg-white/60 ${accentClasses[accent].split(' ')[2]}`}>
            {Array.isArray(items) ? items.length : items.length}
          </span>
        </div>
        {open ? <ChevronUp className="w-4 h-4" /> : <ChevronDown className="w-4 h-4" />}
      </button>

      <AnimatePresence initial={false}>
        {open && (
          <motion.div
            initial={{ height: 0 }}
            animate={{ height: 'auto' }}
            exit={{ height: 0 }}
            transition={{ duration: 0.2 }}
            className="overflow-hidden"
          >
            <div className="p-3.5 pt-0 space-y-2">
              {typeof items[0] === 'string'
                ? items.map((item, i) => (
                    <div key={i} className="flex gap-2 text-sm text-gray-700">
                      <span className="flex-shrink-0 w-5 h-5 rounded-full bg-white border border-gray-200 flex items-center justify-center text-xs font-bold text-gray-500">
                        {i + 1}
                      </span>
                      <span>{item}</span>
                    </div>
                  ))
                : items.map((item, i) => (
                    <div key={i} className="bg-white rounded-xl p-3 border border-blue-100">
                      <p className="font-semibold text-sm text-blue-800">{item.product}</p>
                      {item.active_ingredient && (
                        <p className="text-xs text-gray-500 mt-0.5">Active: {item.active_ingredient}</p>
                      )}
                      <div className="flex flex-wrap gap-x-4 gap-y-1 mt-1.5">
                        {item.dosage && <span className="text-xs text-gray-600">📏 {item.dosage}</span>}
                        {item.frequency && <span className="text-xs text-gray-600">🔄 {item.frequency}</span>}
                      </div>
                      {item.safety_precautions && (
                        <p className="text-xs text-orange-600 mt-1.5 flex gap-1">
                          <span>⚠️</span><span>{item.safety_precautions}</span>
                        </p>
                      )}
                    </div>
                  ))
              }
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  )
}

export default function DiagnosisResult({ result }) {
  const { diagnosis, explanation, alternatives, treatment, urgency, recovery_timeline,
          weather_context, audio_response_base64, response_text, transcript } = result

  const urgencyConf = URGENCY_CONFIG[urgency] || URGENCY_CONFIG.medium
  const UrgencyIcon = urgencyConf.icon
  const [showAlternatives, setShowAlternatives] = useState(false)
  const [showExplanation, setShowExplanation] = useState(false)

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.4 }}
      className="space-y-4"
    >
      {/* Transcript */}
      {transcript && (
        <div className="bg-gray-50 border border-gray-100 rounded-2xl p-3.5">
          <p className="text-xs text-gray-400 font-medium mb-1">Your report (transcribed)</p>
          <p className="text-sm text-gray-700 italic">"{transcript}"</p>
        </div>
      )}

      {/* Main diagnosis card */}
      <div className="card">
        {/* Urgency badge */}
        <div className={`inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-bold mb-3 ${urgencyConf.bg} ${urgencyConf.color}`}>
          <UrgencyIcon className="w-3 h-3" />
          {urgencyConf.label} URGENCY
        </div>

        {/* Disease name */}
        <h2 className="text-xl font-bold text-gray-900 leading-tight">{diagnosis.primary_disease}</h2>
        {diagnosis.local_name && diagnosis.local_name !== diagnosis.primary_disease && (
          <p className="text-farm-700 font-medium text-base mt-0.5">{diagnosis.local_name}</p>
        )}
        {diagnosis.scientific_name && (
          <p className="text-xs text-gray-400 italic mt-0.5">{diagnosis.scientific_name}</p>
        )}

        <div className="flex items-center gap-2 mt-1 mb-3">
          <span className="text-xs bg-farm-100 text-farm-700 px-2 py-0.5 rounded-full font-medium">
            {diagnosis.affected_crop}
          </span>
          <span className="text-xs bg-gray-100 text-gray-600 px-2 py-0.5 rounded-full">
            {diagnosis.stage} stage
          </span>
        </div>

        {/* Confidence */}
        <div className="mb-3">
          <p className="text-xs text-gray-500 mb-1 font-medium">Diagnosis Confidence</p>
          <ConfidenceMeter confidence={diagnosis.confidence} />
        </div>

        {/* Severity */}
        <div className="mb-3">
          <p className="text-xs text-gray-500 mb-1 font-medium">Disease Severity</p>
          <SeverityBar severity={diagnosis.severity} />
        </div>

        {/* Recovery timeline */}
        {recovery_timeline && (
          <div className="flex items-center gap-1.5 text-xs text-gray-500">
            <Clock className="w-3.5 h-3.5" />
            <span>Recovery: {recovery_timeline}</span>
          </div>
        )}
      </div>

      {/* Audio response */}
      {audio_response_base64 && response_text && (
        <AudioPlayer audioBase64={audio_response_base64} responseText={response_text} />
      )}

      {/* Weather */}
      {weather_context && <WeatherWidget weather={weather_context} />}

      {/* Explanation / Why this diagnosis */}
      <div className="card">
        <button
          className="w-full flex items-center justify-between"
          onClick={() => setShowExplanation(!showExplanation)}
        >
          <div className="flex items-center gap-2">
            <Info className="w-4 h-4 text-farm-600" />
            <span className="font-semibold text-gray-800 text-sm">Why this diagnosis?</span>
          </div>
          {showExplanation ? <ChevronUp className="w-4 h-4 text-gray-400" /> : <ChevronDown className="w-4 h-4 text-gray-400" />}
        </button>

        <AnimatePresence initial={false}>
          {showExplanation && (
            <motion.div
              initial={{ height: 0, opacity: 0 }}
              animate={{ height: 'auto', opacity: 1 }}
              exit={{ height: 0, opacity: 0 }}
              transition={{ duration: 0.2 }}
              className="overflow-hidden"
            >
              <div className="pt-3 space-y-3">
                <p className="text-sm text-gray-700">{explanation.reasoning}</p>

                {explanation.key_symptoms?.length > 0 && (
                  <div>
                    <p className="text-xs font-semibold text-gray-500 mb-1.5">Symptoms Matched</p>
                    <div className="flex flex-wrap gap-1.5">
                      {explanation.key_symptoms.map((s, i) => (
                        <span key={i} className="text-xs bg-farm-50 text-farm-700 border border-farm-200 px-2 py-1 rounded-xl">
                          ✓ {s}
                        </span>
                      ))}
                    </div>
                  </div>
                )}

                {explanation.visual_evidence?.length > 0 && explanation.visual_evidence[0] !== 'N/A' && (
                  <div>
                    <p className="text-xs font-semibold text-gray-500 mb-1.5">Visual Evidence</p>
                    {explanation.visual_evidence.map((v, i) => (
                      <p key={i} className="text-xs text-gray-600 flex gap-1.5">
                        <span>📷</span><span>{v}</span>
                      </p>
                    ))}
                  </div>
                )}

                {explanation.environmental_factors?.length > 0 && (
                  <div>
                    <p className="text-xs font-semibold text-gray-500 mb-1.5">Environmental Factors</p>
                    {explanation.environmental_factors.map((f, i) => (
                      <p key={i} className="text-xs text-gray-600 flex gap-1.5">
                        <span>🌤</span><span>{f}</span>
                      </p>
                    ))}
                  </div>
                )}
              </div>
            </motion.div>
          )}
        </AnimatePresence>
      </div>

      {/* Treatment sections */}
      <div className="space-y-2">
        <h3 className="font-semibold text-gray-800 flex items-center gap-2">
          <Zap className="w-4 h-4 text-farm-600" /> Treatment Plan
        </h3>

        <TreatmentSection
          icon={AlertTriangle} title="Immediate Actions" items={treatment.immediate} accent="red"
        />
        <TreatmentSection
          icon={Sprout} title="Organic / Natural Treatment" items={treatment.organic} accent="green"
        />
        <TreatmentSection
          icon={FlaskConical} title="Chemical Treatment" items={treatment.chemical} accent="blue"
        />
        <TreatmentSection
          icon={ShieldCheck} title="Prevention" items={treatment.prevention} accent="purple"
        />
      </div>

      {/* Alternative diagnoses */}
      {alternatives?.length > 0 && (
        <div className="card">
          <button
            className="w-full flex items-center justify-between"
            onClick={() => setShowAlternatives(!showAlternatives)}
          >
            <span className="text-sm font-semibold text-gray-700">
              Other possibilities ({alternatives.length})
            </span>
            {showAlternatives ? <ChevronUp className="w-4 h-4 text-gray-400" /> : <ChevronDown className="w-4 h-4 text-gray-400" />}
          </button>

          <AnimatePresence initial={false}>
            {showAlternatives && (
              <motion.div
                initial={{ height: 0, opacity: 0 }}
                animate={{ height: 'auto', opacity: 1 }}
                exit={{ height: 0, opacity: 0 }}
                transition={{ duration: 0.2 }}
                className="overflow-hidden"
              >
                <div className="pt-3 space-y-2">
                  {alternatives.map((alt, i) => (
                    <div key={i} className="bg-gray-50 rounded-xl p-3">
                      <div className="flex items-center justify-between">
                        <span className="text-sm font-medium text-gray-800">{alt.disease}</span>
                        <span className="text-xs text-gray-500">{alt.confidence}% likely</span>
                      </div>
                      {alt.differentiator && (
                        <p className="text-xs text-gray-500 mt-1">{alt.differentiator}</p>
                      )}
                    </div>
                  ))}
                </div>
              </motion.div>
            )}
          </AnimatePresence>
        </div>
      )}
    </motion.div>
  )
}
