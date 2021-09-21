from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'location': util.get_location_names()
    })
    response.headers.add("Access-Control-Allow_Origin", 'r')

    return response

if __name__ == "__main__":
    app.run(debug=True)