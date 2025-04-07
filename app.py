
    from flask import Flask, request, jsonify
    import openai

    app = Flask(__name__)

    openai.api_key = 'your-openai-api-key-here'

    @app.route('/ask', methods=['POST'])
    def ask():
        user_input = request.json.get('user_input')
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=150
        )
        return jsonify(response.choices[0].text.strip())

    if __name__ == '__main__':
        app.run(debug=True)
    