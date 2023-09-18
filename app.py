from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_query = request.form.get('user_query')

    # Add sorting by rating to the user's query by default
    user_query_with_sort = f"{user_query} go through the entire PDF carefully, check the ratings, and then sort the top ones by rating DESC"

    api_url = 'https://api.chatpdf.com/v1/chats/message'
    api_key = 'sec_ejO1KiIHZXOSmOKyYjKpyWocMEZuRKhp'
    source_id = 'src_bBvRmhofMS4JlCncekfoS'

    headers = {
        'x-api-key': api_key,
        'Content-Type': 'application/json',
    }

    data = {
        'sourceId': source_id,
        'messages': [
            {
                'role': 'user',
                'content': user_query_with_sort,  # Include default sorting
            }
        ]
    }

    try:
        response = requests.post(api_url, headers=headers, json=data)
        result = response.json()
        chat_response = result.get('content')

        # Split the response into individual lines
        lines = chat_response.strip().split('\n')

    except Exception as e:
        lines = [f"Error: {str(e)}"]

    return render_template('responses.html', lines=lines)

if __name__ == '__main__':
    app.run(debug=True)
