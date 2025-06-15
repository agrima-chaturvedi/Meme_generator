import requests

def generate_imgflip_meme(template_id, top_text, bottom_text, username, password):
    url = 'https://api.imgflip.com/caption_image'

    params = {
        'template_id': template_id,
        'username': username,
        'password': password,
        'text0': top_text,
        'text1': bottom_text
    }

    response = requests.post(url, params=params)
    result = response.json()

    if result['success']:
        return result['data']['url']
    else:
        raise Exception(f"❌ Meme generation failed: {result['error_message']}")
