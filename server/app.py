from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Ensure your OPENAI_API_KEY is loaded from environment variables
openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    try:
        transcript = openai.Audio.transcriptions.create(
            model="whisper-1",
            file=file,
            wait_for_completion=True  # This ensures the API request waits for the transcription to complete
        )
        return jsonify({'transcription': transcript['text']}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World"

if __name__ == '__main__':
    app.run(debug=True)