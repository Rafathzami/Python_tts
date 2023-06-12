from flask import Flask, jsonify, request
from gtts import gTTS
import base64
from flask_cors import CORS
#import ssl #this will import ssl module

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["https://domain.com" ,"https://localhost:1001"]}})

@app.route('/generate_speech', methods=['POST'])
def generate_speech():
    lang = request.json['lang']
    text = request.json['text']
    tts = gTTS(text, lang=lang)
    file_name = f'{lang}.mp3'
    tts.save(file_name)

    with open(file_name, 'rb') as f:
        speech_bytes = f.read()

    speech_base64 = base64.b64encode(speech_bytes).decode('utf-8')
    response = jsonify({'status': 200, 'speech_base64': speech_base64})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    #context = ssl.SSLContext(ssl.PROTOCOL_TLS)  # Create SSL context
    #context.load_cert_chain('/home/tts/cert.pem', '/home/user/key.pem')  # Load SSL certificate and private key
    app.run(debug=True, host='0.0.0.0', port=8001)  # Run the app with SSL context