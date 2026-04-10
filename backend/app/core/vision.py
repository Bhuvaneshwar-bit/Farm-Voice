import base64
from typing import Optional
from groq import Groq
from app.core.config import settings, GROQ_VISION_MODEL

VISION_PROMPT = """You are an expert plant pathologist. Analyze this crop/plant image and describe:

1. Leaf condition: color changes, spots, lesions, wilting, curling, yellowing
2. Affected plant parts: leaves, stem, roots, fruit, flowers
3. Symptom patterns: uniform vs scattered, edge vs center, top vs bottom leaves
4. Severity estimate: what percentage of plant is affected?
5. Any visible pests, eggs, or insect damage
6. Any fungal growth, mold, or bacterial ooze visible

Be specific and clinical. This will be used for disease diagnosis.
Format: one concise paragraph, then a bullet list of key visual observations."""


async def analyze_crop_image(image_base64: str) -> Optional[str]:
    """
    Use Llama 3.2 Vision (via Groq) to extract visual disease features from crop photo.
    Returns a textual description of visual symptoms.
    Model: llama-3.2-11b-vision-preview (open-source, free on Groq).
    """
    if not image_base64 or not settings.GROQ_API_KEY:
        return None

    try:
        client = Groq(api_key=settings.GROQ_API_KEY)

        # Groq vision expects a data URI
        image_url = f"data:image/jpeg;base64,{image_base64}"

        response = client.chat.completions.create(
            model=GROQ_VISION_MODEL,
            max_tokens=600,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "image_url",
                            "image_url": {"url": image_url},
                        },
                        {
                            "type": "text",
                            "text": VISION_PROMPT,
                        },
                    ],
                }
            ],
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Vision analysis error: {e}")
        return None
