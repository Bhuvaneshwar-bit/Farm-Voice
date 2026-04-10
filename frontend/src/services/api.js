import axios from 'axios'

const BASE_URL = import.meta.env.VITE_API_URL || '/api/v1'

const api = axios.create({
  baseURL: BASE_URL,
  timeout: 120000, // 2 minutes for audio processing
})

export async function diagnose({ audioBase64, textInput, imageBase64, latitude, longitude, language, cropType }) {
  const payload = {
    language: language || 'auto',
  }
  if (audioBase64) payload.audio_base64 = audioBase64
  if (textInput)   payload.text_input   = textInput
  if (imageBase64) payload.image_base64 = imageBase64
  if (latitude != null) payload.latitude = latitude
  if (longitude != null) payload.longitude = longitude
  if (cropType)    payload.crop_type    = cropType

  const { data } = await api.post('/diagnose', payload)
  return data
}

export async function submitFeedback({ sessionId, feedbackType, actualDisease, farmerNote, helpfulRating }) {
  const { data } = await api.post('/feedback', {
    session_id: sessionId,
    feedback_type: feedbackType,
    actual_disease: actualDisease,
    farmer_note: farmerNote,
    helpful_rating: helpfulRating,
  })
  return data
}

export async function getHistory(limit = 10) {
  const { data } = await api.get(`/history?limit=${limit}`)
  return data
}

export async function getHealth() {
  const { data } = await api.get('/health')
  return data
}

export default api
