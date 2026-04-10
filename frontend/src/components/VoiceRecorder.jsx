import { useState, useRef, useEffect } from 'react'
import { Mic, MicOff, Square } from 'lucide-react'
import { motion, AnimatePresence } from 'framer-motion'

export default function VoiceRecorder({ onAudioCaptured, disabled }) {
  const [isRecording, setIsRecording] = useState(false)
  const [seconds, setSeconds] = useState(0)
  const [permissionDenied, setPermissionDenied] = useState(false)
  const mediaRecorderRef = useRef(null)
  const chunksRef = useRef([])
  const timerRef = useRef(null)

  useEffect(() => {
    return () => {
      clearInterval(timerRef.current)
      mediaRecorderRef.current?.stream?.getTracks().forEach(t => t.stop())
    }
  }, [])

  const startRecording = async () => {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true })
      setPermissionDenied(false)
      chunksRef.current = []

      // Try webm/opus first (better quality), fallback to default
      const mimeType = MediaRecorder.isTypeSupported('audio/webm;codecs=opus')
        ? 'audio/webm;codecs=opus'
        : MediaRecorder.isTypeSupported('audio/webm')
        ? 'audio/webm'
        : ''

      mediaRecorderRef.current = new MediaRecorder(stream, mimeType ? { mimeType } : {})

      mediaRecorderRef.current.ondataavailable = e => {
        if (e.data.size > 0) chunksRef.current.push(e.data)
      }

      mediaRecorderRef.current.onstop = () => {
        const blob = new Blob(chunksRef.current, { type: mimeType || 'audio/webm' })
        const reader = new FileReader()
        reader.readAsDataURL(blob)
        reader.onloadend = () => {
          const base64 = reader.result.split(',')[1]
          onAudioCaptured(base64)
        }
        stream.getTracks().forEach(t => t.stop())
      }

      mediaRecorderRef.current.start(100)
      setIsRecording(true)
      setSeconds(0)
      timerRef.current = setInterval(() => setSeconds(s => s + 1), 1000)
    } catch (err) {
      if (err.name === 'NotAllowedError') setPermissionDenied(true)
    }
  }

  const stopRecording = () => {
    clearInterval(timerRef.current)
    mediaRecorderRef.current?.stop()
    setIsRecording(false)
  }

  const formatTime = s => `${Math.floor(s / 60).toString().padStart(2, '0')}:${(s % 60).toString().padStart(2, '0')}`

  return (
    <div className="flex flex-col items-center gap-4">
      <AnimatePresence mode="wait">
        {isRecording ? (
          <motion.div
            key="recording"
            initial={{ scale: 0.8, opacity: 0 }}
            animate={{ scale: 1, opacity: 1 }}
            exit={{ scale: 0.8, opacity: 0 }}
            className="flex flex-col items-center gap-4"
          >
            {/* Waveform animation */}
            <div className="flex items-end gap-1 h-10 text-red-500">
              {[...Array(9)].map((_, i) => (
                <span
                  key={i}
                  className="wave-bar bg-red-500"
                  style={{ animationDelay: `${i * 0.1}s` }}
                />
              ))}
            </div>

            <div className="text-red-500 font-mono font-bold text-xl">
              {formatTime(seconds)}
            </div>

            <button
              onClick={stopRecording}
              className="w-20 h-20 rounded-full bg-red-500 hover:bg-red-600 active:bg-red-700
                         flex items-center justify-center shadow-lg shadow-red-500/40
                         transition-all active:scale-95"
            >
              <Square className="w-8 h-8 text-white fill-white" />
            </button>
            <p className="text-sm text-gray-500">Tap to stop recording</p>
          </motion.div>
        ) : (
          <motion.div
            key="idle"
            initial={{ scale: 0.8, opacity: 0 }}
            animate={{ scale: 1, opacity: 1 }}
            exit={{ scale: 0.8, opacity: 0 }}
            className="flex flex-col items-center gap-3"
          >
            <button
              onClick={startRecording}
              disabled={disabled}
              className="w-24 h-24 rounded-full bg-farm-600 hover:bg-farm-700 active:bg-farm-800
                         flex items-center justify-center shadow-xl shadow-farm-600/40
                         transition-all active:scale-95 disabled:opacity-50 disabled:cursor-not-allowed
                         animate-pulse-ring"
            >
              <Mic className="w-10 h-10 text-white" />
            </button>
            <p className="text-sm font-medium text-gray-600">
              {permissionDenied ? '⚠️ Microphone permission denied' : 'Tap to record voice'}
            </p>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  )
}
