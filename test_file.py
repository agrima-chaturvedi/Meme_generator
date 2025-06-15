import requests
from transformers import pipeline
import urllib.request
import os

# Step 1: Load GPT-2 for text generation
generator = pipeline("text-generation", model="gpt2")

# Step 2: Prompt for meme idea
prompt = input("Enter meme idea: ")

# Step 3: Generate caption using GPT-2
caption_result = generator(
    prompt,
    max_new_tokens=40,
    truncation=True,
    pad_token_id=50256
)
generated_caption = caption_result[0]['generated_text']
print(f"Generated Caption: {generated_caption}")

# Step 4: Define meme template (you can list all later)
template_id = "181913649"  # Drakeposting

# Imgflip credentials
username = "AgrimaChaturvedi"
password = "huggingmeme"

# Step 5: Make meme using Imgflip API
api_url = 'https://api.imgflip.com/caption_image'
params = {
    'template_id': template_id,
    'username': username,
    'password': password,
    'text0': prompt,
    'text1': generated_caption
}

response = requests.post(api_url, params=params).json()

if response['success']:
    meme_url = response['data']['url']
    print("✅ Meme created successfully!")
    print("🖼️ Meme URL:", meme_url)

    # Step 6: Save meme locally
    output_path = "final_meme.jpg"
    urllib.request.urlretrieve(meme_url, output_path)
    print(f"💾 Meme saved as {output_path}")
else:
    print("❌ Meme generation failed:", response['error_message'])
