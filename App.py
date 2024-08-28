from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Load responses from the JSON file
def load_responses():
    with open('responses.json', 'r') as file:
        return json.load(file)
    
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message').lower()
    responses = load_responses()
    response = responses.get(user_input, responses['default'])
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    app.run(debug=True)