from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('chatmaid.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_query = request.form.get('user_query')

    api_url = 'https://api.chatpdf.com/v1/chats/message'
    api_key = 'sec_ejO1KiIHZXOSmOKyYjKpyWocMEZuRKhp'
    source_id = 'cha_lFc1nwYUGu88nYVxNEFr6'

    headers = {
        'x-api-key': api_key,
        'Content-Type': 'application/json',
    }

    data = {
        'sourceId': source_id,
        'messages': [
            {
                'role': 'user',
                'content': user_query,
            }
        ]
    }

    try:
        response = requests.post(api_url, headers=headers, json=data)
        result = response.json()
        chat_response = result.get('content')
    except Exception as e:
        chat_response = f"Error: {str(e)}"

    return render_template('responses.html', response=chat_response)

if __name__ == '__main__':
    app.run(debug=True)

