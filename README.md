# 🤖 AI-Powered Meme Generator

An AI-powered meme generator built with Python, Flask, and Hugging Face Transformers. Enter a meme idea, and the app will generate a funny caption using GPT-2 and place it on a meme template from ImgFlip.

## 📸 Features

- Generate funny/sarcastic captions using GPT-2
- Select and apply meme templates automatically
- Display generated memes instantly
- Option to download the meme
- Clean and responsive web interface

## 🛠️ Tech Stack

- Python
- Flask
- Transformers (Hugging Face)
- GPT-2 Model
- PIL (Python Imaging Library)
- HTML/CSS (Jinja2 template engine)

## 🚀 How It Works

1. Enter a meme idea in the input box (e.g., *"monday mornings be like"*).
2. The app uses GPT-2 to generate a funny caption.
3. It selects a relevant meme template.
4. The caption is placed on the image.
5. The meme is displayed and downloadable.

## 📁 Folder Structure

Meme/<div>
├── app.py<div>
├── templates/<div>
│ └── index.html<div>
├── static/<div>
│ └── meme.jpg<div>
├── app/<div>
│ └── generate_caption.py<div>
└── requirements.txt<div>

## 🔧 Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/agrima-chaturvedi/Meme_generator.git
   cd Meme_generator
2. Install Dependencies
    pip install -r requirements.txt
3. Run the app
    python app.py

   
## 📷 Example

![image](https://github.com/user-attachments/assets/0ed8f635-3f54-4879-9fa1-9259218094a5)
![image](https://github.com/user-attachments/assets/51d8e34e-920c-4e50-8c46-94666fb7e7f2)

🧠 Model Used

    gpt2 model from Hugging Face

    Text generation is done via the transformers pipeline

    Meme template selection is rule-based (can be extended using template mapping)

📝 Future Improvements

    Add multiple meme templates to choose from

    Improve humor detection and filter boring captions

    Add support for custom image uploads

📄 License

This project is open-source under the MIT License.

Made by Agrima Chaturvedi
