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
    # Retrieve input data from the request
    new = request.get_json()

    brand = new['BRAND']
    cpu_brand = new['CPU BRAND']
    cpu_core = new['CPU CORE']
    cpu_generation = new['CPU GENERATION']
    cpu_family = new['CPU FAMILY']
    ram_size = new['RAM SIZE']
    ddr_type = new['RAM(DDR) TYPE']
    disk_type = new['DISK TYPE']
    ssd_size = new['SSD SIZE']
    hdd_size = new['HDD SIZE']
    gpu_brand = new['GPU BRAND']
    gpu_type = new['GPU TYPE']
    screen_size = new['SCREEN SIZE']
    screen_resolution = new['SCREEN RESOLUTION']
    state = new['STATE']

    # Prepare input data for prediction
    specifications = {
        'BRAND': brand,
        'CPU BRAND': cpu_brand,
        'CPU CORE': cpu_core,
        'CPU GENERATION': cpu_generation,
        'CPU FAMILY': cpu_family,
        'RAM SIZE': ram_size,
        'RAM(DDR) TYPE': ddr_type,
        'DISK TYPE': disk_type,
        'SSD SIZE': ssd_size,
        'HDD SIZE': hdd_size,
        'GPU BRAND': gpu_brand,
        'GPU TYPE': gpu_type,
        'SCREEN SIZE': screen_size,
        'SCREEN RESOLUTION': screen_resolution,
        'STATE': state
    }

    # Convert the laptop specifications into a pandas dataframe
    input_query = pd.DataFrame(data=specifications)

    print(input_query)

    # Perform prediction using the pre-trained model
    result = model.predict(input_query)[0]

    # Return the prediction result as a JSON response
    return jsonify(result.round().tolist())


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True, host="192.168.1.6", port=9090)
