from flask import Flask, request, jsonify
import pickle
import pandas as pd

# Load the pre-trained machine learning model
model = pickle.load(open('model.pkl', 'rb'))

# Create a Flask web application
app = Flask(__name__)


# Define the home route
@app.route('/')
def home():
    """
    Home route for the Flask application.
    """
    return "Hi, I guess this API works!!!"


# Define the predictor route for handling prediction requests
@app.route('/predictor', methods=['POST'])
def predictor():
    """
    Route for handling prediction requests.
    """
    try:
        # Retrieve input data from the request
        data = request.get_json()

        # Validate input data
        required_fields = [
            'BRAND', 'CPU BRAND', 'CPU CORE', 'CPU GENERATION', 'CPU FAMILY',
            'RAM SIZE', 'RAM(DDR) TYPE', 'DISK TYPE', 'SSD SIZE', 'HDD SIZE',
            'GPU BRAND', 'GPU TYPE', 'SCREEN SIZE', 'SCREEN RESOLUTION', 'STATE'
        ]

        for field in required_fields:
            if field not in data:
                raise ValueError(f"Missing required field: {field}")

        # Prepare input data for prediction
        specifications = {field: data[field] for field in required_fields}

        # Convert the laptop specifications into a pandas dataframe
        input_query = pd.DataFrame(data=[specifications])

        # Perform prediction using the pre-trained model
        result = model.predict(input_query)[0]

        # Return the prediction result as a JSON response
        return jsonify({'predicted_price': result.round().tolist()}), 200

    except ValueError as ve:
        return jsonify({'error': str(ve)}), 400


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True, host="192.168.1.4", port=9090)
