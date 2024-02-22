from flask import Flask, request, jsonify
from flask_cors import CORS  
import openai
import os
from dotenv import load_dotenv

app = Flask(__name__)
CORS(app)

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY', 'DefaultApiKeyIfNotSet')

def chat_with_gpt(message):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are a helpful assistant."},
                  {"role": "user", "content": message}]
    )
    return response.choices[0].message['content']

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    message = data['message']
    response = chat_with_gpt(message)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)
