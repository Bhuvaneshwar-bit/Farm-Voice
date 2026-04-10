import { useRef, useState } from 'react'
import { Camera, X, ImageIcon } from 'lucide-react'

export default function ImageUpload({ onImageCaptured, imagePreview, disabled }) {
  const fileInputRef = useRef(null)
  const cameraInputRef = useRef(null)

  const handleFile = file => {
    if (!file || !file.type.startsWith('image/')) return
    const reader = new FileReader()
    reader.readAsDataURL(file)
    reader.onloadend = () => {
      const base64 = reader.result.split(',')[1]
      onImageCaptured(base64, reader.result)
    }
  }

  return (
    <div className="flex flex-col gap-2">
      {imagePreview ? (
        <div className="relative">
          <img
            src={imagePreview}
            alt="Crop photo"
            className="w-full h-40 object-cover rounded-2xl border-2 border-farm-200"
          />
          <button
            onClick={() => onImageCaptured(null, null)}
            className="absolute top-2 right-2 bg-black/60 text-white rounded-full p-1 hover:bg-black/80"
          >
            <X className="w-4 h-4" />
          </button>
          <div className="absolute bottom-2 left-2 bg-farm-600 text-white text-xs px-2 py-1 rounded-lg">
            Photo added
          </div>
        </div>
      ) : (
        <div className="flex gap-2">
          {/* Camera capture (mobile) */}
          <button
            onClick={() => cameraInputRef.current?.click()}
            disabled={disabled}
            className="flex-1 flex items-center justify-center gap-2 py-3.5 rounded-2xl
                       border-2 border-dashed border-farm-300 text-farm-600
                       hover:bg-farm-50 active:bg-farm-100 transition-all
                       disabled:opacity-50 disabled:cursor-not-allowed"
          >
            <Camera className="w-5 h-5" />
            <span className="text-sm font-medium">Take Photo</span>
          </button>

          {/* File upload */}
          <button
            onClick={() => fileInputRef.current?.click()}
            disabled={disabled}
            className="flex-1 flex items-center justify-center gap-2 py-3.5 rounded-2xl
                       border-2 border-dashed border-farm-300 text-farm-600
                       hover:bg-farm-50 active:bg-farm-100 transition-all
                       disabled:opacity-50 disabled:cursor-not-allowed"
          >
            <ImageIcon className="w-5 h-5" />
            <span className="text-sm font-medium">Upload</span>
          </button>
        </div>
      )}

      <input
        ref={cameraInputRef}
        type="file"
        accept="image/*"
        capture="environment"
        onChange={e => handleFile(e.target.files?.[0])}
        className="hidden"
      />
      <input
        ref={fileInputRef}
        type="file"
        accept="image/*"
        onChange={e => handleFile(e.target.files?.[0])}
        className="hidden"
      />
    </div>
  )
}
