from flask import Flask, request, jsonify
import openai

# Initialize the Flask application
app = Flask(__name__)

config_file_path = 'config'
def read_key_from_config(key_name):
    with open(config_file_path, 'r') as file:
        for line in file:
            if line.startswith(key_name):
                return line.split('=')[1].strip().replace("\"", "")
    return None

api_key = read_key_from_config('OPENAI_API_KEY')
llm_name = read_key_from_config('OPENAI_MODEL')

client = openai.OpenAI(api_key=api_key)


@app.route('/process', methods=['POST'])
def process_text():
    # Get data from POST request
    data = request.json
    text = data.get('text', '')

    # Send text to OpenAI's API
    try:
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": text}],
            model=llm_name
        )
        print(chat_completion)
        result = chat_completion.choices[0].message.content
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    # Return OpenAI's response
    print(result)
    return jsonify({'response': result})

@app.route('/ha', methods=['POST'])
def handle_ha():
    # Get data from POST request
    data = request.json
    userquery = data.get('text', '')
    with open('prompts/homeassistant', 'r') as file:
        prompt_base = file.read().strip()

    prompt = prompt_base + userquery
    print(prompt)

    # Send text to OpenAI's API
    try:
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model=llm_name  # or any other model
        )
        print(chat_completion)
        result = chat_completion.choices[0].message.content
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    # Return OpenAI's response
    print(result)
    return jsonify({'response': result})

if __name__ == '__main__':
    app.run(debug=True)
