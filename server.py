from flask import Flask, request, jsonify, render_template
import util

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('app.html')


@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location,
                                                    total_sqft,
                                                    bhk, bath)
    })
    response.headers.add('Access-Control-Allow-origin', '*')
    return response


if __name__ == "__main__":
    util.load_saved_artifacts()
    print("Starting Python Flask Server")
    app.run(debug=True)
