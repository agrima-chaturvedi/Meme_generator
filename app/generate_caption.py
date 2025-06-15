import os
os.environ['HF_HOME'] = 'E:/huggingface_cache'

from transformers import pipeline

# Load GPT-2 text generation pipeline
generator = pipeline("text-generation", model="gpt2")

def generate_caption(prompt):
    formatted_prompt = f"Write a funny meme caption for: {prompt}\nMeme caption:"
    
    # Generate caption with GPT-2
    result = generator(
        formatted_prompt,
        max_length=60,        # Slightly increased for funnier/completer sentences
        do_sample=True,
        top_k=50,
        top_p=0.95,
        temperature=0.9       # Slight creativity boost
    )[0]["generated_text"]

    # Clean and extract generated caption
    caption = result.replace(formatted_prompt, "").strip().split("\n")[0]

    # Basic sanitization
    if not caption or len(caption) < 5:
        return "Oops, GPT2 was too tired to be funny. Try again!"
    
    return caption

