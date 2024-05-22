from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def handle_request():
    data = {'message': 'Hello, World! First test'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
