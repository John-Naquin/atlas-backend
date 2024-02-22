from flask import Flask, request, jsonify
from flask_cors import CORS  
import openai

app = Flask(__name__)
CORS(app)

openai.api_key = 'You can not have my key!' 

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
    app.run(debug=True)