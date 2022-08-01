# server does routing of request and response
from flask import Flask, request, jsonify
import util

app = Flask(__name__) # use this line to create an app

# create an endpoint for price prediction 
@app.route('/predict_stability_number', methods=['GET', 'POST']) # decleration of http endpoint
def predict_stability_number():
    D = float(request.form['D'])
    GSI = float(request.form['GSI'])
    mi = float(request.form['mi'])
    beta = float(request.form['beta'])
    kh = float(request.form['kh'])


    response = jsonify({
        'estimated_stability_number': util.get_stability_number(D, GSI, mi, beta, kh)
    })

    response.headers.add('Access-Control-Allow-Origin', '*')
    
    return response


if __name__ == "__main__":
    print ('Starting Flask server for stability number prediction...')
    util.load_saved_artifacts()
    app.run()