from flask import Flask, render_template, request, send_file
from gtts import gTTS

app = Flask(__name__)

# Available language codes supported by gTTS
LANGUAGES = {
    'en': 'English',
    'es': 'Spanish',
    'fr': 'French',
    'de': 'German',
    'it': 'Italian',
    'pt': 'Portuguese',
    'hi': 'Hindi',
    'ja': 'Japanese',
    'zh': 'Chinese (Mandarin)'
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/convert", methods=["POST"])
def convert():
    text = request.form.get("text")
    language = request.form.get("language", "en")  # Default to English

    if not text:
        return "No text provided", 400

    if language not in LANGUAGES:
        return "Selected language not supported", 400

    # Generate speech using gTTS with the selected language
    tts = gTTS(text, lang=language)
    tts.save("output.mp3")

    return send_file("output.mp3", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
