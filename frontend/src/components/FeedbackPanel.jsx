import { useState } from 'react'
import { ThumbsUp, ThumbsDown, Minus, CheckCircle } from 'lucide-react'
import { submitFeedback } from '../services/api'
import toast from 'react-hot-toast'

export default function FeedbackPanel({ sessionId }) {
  const [selected, setSelected] = useState(null)
  const [rating, setRating] = useState(0)
  const [note, setNote] = useState('')
  const [submitted, setSubmitted] = useState(false)
  const [loading, setLoading] = useState(false)

  const feedbackOptions = [
    { type: 'correct', icon: ThumbsUp, label: 'Correct!', color: 'text-green-600', bg: 'bg-green-50 border-green-200' },
    { type: 'partial', icon: Minus, label: 'Partially', color: 'text-yellow-600', bg: 'bg-yellow-50 border-yellow-200' },
    { type: 'incorrect', icon: ThumbsDown, label: 'Wrong', color: 'text-red-600', bg: 'bg-red-50 border-red-200' },
  ]

  const handleSubmit = async () => {
    if (!selected) return
    setLoading(true)
    try {
      await submitFeedback({
        sessionId,
        feedbackType: selected,
        farmerNote: note || undefined,
        helpfulRating: rating || undefined,
      })
      setSubmitted(true)
      toast.success('Thank you for your feedback!')
    } catch {
      toast.error('Could not save feedback. Please try again.')
    } finally {
      setLoading(false)
    }
  }

  if (submitted) {
    return (
      <div className="card flex items-center justify-center gap-3 py-6 text-farm-600">
        <CheckCircle className="w-6 h-6" />
        <p className="font-semibold">Feedback saved! Thank you.</p>
      </div>
    )
  }

  return (
    <div className="card space-y-4">
      <h3 className="font-semibold text-gray-800 text-sm">Was this diagnosis helpful?</h3>

      <div className="flex gap-2">
        {feedbackOptions.map(opt => {
          const Icon = opt.icon
          return (
            <button
              key={opt.type}
              onClick={() => setSelected(opt.type)}
              className={`flex-1 flex flex-col items-center gap-1.5 py-3 rounded-2xl border-2 transition-all active:scale-95 ${
                selected === opt.type ? opt.bg + ' border-current scale-105 shadow-sm' : 'border-gray-100 bg-white hover:bg-gray-50'
              } ${opt.color}`}
            >
              <Icon className="w-5 h-5" />
              <span className="text-xs font-medium">{opt.label}</span>
            </button>
          )
        })}
      </div>

      {selected && (
        <>
          {/* Star rating */}
          <div>
            <p className="text-xs text-gray-500 mb-2">How helpful was this? (optional)</p>
            <div className="flex gap-1.5">
              {[1, 2, 3, 4, 5].map(star => (
                <button
                  key={star}
                  onClick={() => setRating(star)}
                  className={`text-2xl transition-transform active:scale-90 ${star <= rating ? 'opacity-100' : 'opacity-30'}`}
                >
                  ⭐
                </button>
              ))}
            </div>
          </div>

          {/* Note */}
          <div>
            <p className="text-xs text-gray-500 mb-1.5">Any comments? (optional)</p>
            <textarea
              value={note}
              onChange={e => setNote(e.target.value)}
              placeholder="What was the actual disease? Any other info..."
              className="w-full text-sm border border-gray-200 rounded-xl px-3 py-2.5 resize-none focus:outline-none focus:ring-2 focus:ring-farm-400 bg-gray-50"
              rows={2}
              maxLength={300}
            />
          </div>

          <button
            onClick={handleSubmit}
            disabled={loading}
            className="btn-primary w-full text-sm py-3"
          >
            {loading ? 'Saving...' : 'Submit Feedback'}
          </button>
        </>
      )}
    </div>
  )
}
