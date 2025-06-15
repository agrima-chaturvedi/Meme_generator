from flask import Flask, render_template, request
from app.generate_caption import generate_caption
from app.imgflip_generate import generate_imgflip_meme

app = Flask(__name__)

# Set your Imgflip credentials here
USERNAME = "AgrimaChaturvedi"
PASSWORD = "huggingmeme"

# Template map moved outside so it's not recreated every request
TEMPLATE_MAP = {
    # Emotions / School
    "exam": "112126428",               # Distracted Boyfriend
    "study": "61579",                  # One Does Not Simply
    "tired": "8072285",                # Sleeping Shaq
    "panic": "93895088",               # Expanding Brain
    "brain": "93895088",               # Expanding Brain
    "confused": "87743020",            # Two Buttons
    "celebrate": "181913649",          # Drake Hotline Bling
    "happy": "181913649",              # Drake Hotline Bling
    "sad": "61544",                    # First World Problems
    "angry": "195389",                 # Angry Tommy

    # Situational / Reaction
    "upgrade": "112210127",            # Upgrade Button
    "change": "112210127",             # Upgrade Button
    "impossible": "61579",             # One Does Not Simply
    "wait": "89370399",                # Roll Safe Think About It
    "no": "245898",                    # Why Not Both
    "yes": "14371066",                 # Captain Picard Facepalm
    "wrong": "29617627",               # Look at Me - I'm the Captain Now

    # Tech / AI / Logic
    "ai": "131087935",                 # Hard to Swallow Pills
    "machine": "131087935",            # Hard to Swallow Pills
    "coding": "1035805",               # Boardroom Meeting
    "bug": "1035805",                  # Boardroom Meeting
    "logic": "93895088",               # Expanding Brain

    # Misc / Funny
    "dog": "8072285",                 # Dog
    "cat": "124822590",                # Woman Yelling at Cat
    "money": "217743513",              # Bernie Asking Again
    "rich": "217743513",               # Bernie
    "startup": "131087935",            # Hard to Swallow Pills
    "boss": "40945639",                # Scared Cat
}

# Function to select the template based on caption
def select_template(caption):
    for keyword, template_id in TEMPLATE_MAP.items():
        if keyword.lower() in caption.lower():
            return template_id
    return "112126428"  # default: Distracted Boyfriend

@app.route("/", methods=["GET", "POST"])
def index():
    meme_url = None
    caption = ""
    if request.method == "POST":
        idea = request.form["idea"]
        caption = generate_caption(idea).split('\n')[0][:150]
        template_id = select_template(caption)
        top_text = idea
        bottom_text = caption

        meme_url = generate_imgflip_meme(template_id, top_text, bottom_text, USERNAME, PASSWORD)

    return render_template("index.html", meme_url=meme_url, caption=caption)

if __name__ == "__main__":
    app.run(debug=True)
