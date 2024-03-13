from flask import Flask, request, jsonify
from flask import send_file
from sklearn.impute import SimpleImputer
import pandas as pd
import numpy as np
import subprocess
import json
import joblib

app = Flask(__name__)
model = joblib.load("lightgbm_model.pkl")
imputer = SimpleImputer(strategy='mean')  # Initialize the imputer

def get_smart_data(device_path):
    # Run smartctl command to get SMART data
    command = ["sudo", "smartctl", "--all", device_path, "-j"]
    result = subprocess.run(command, capture_output=True, text=True)

    # Print the SMART data
    print("SMART data:", result.stdout)

    # Save the JSON data to a file
    with open('/predictt/smart_data.json', 'w') as f:
        f.write(result.stdout)

    return result.stdout

json_file_path = '/predictt/smart_data.json'

def convert_to_csv_format(json_file_path):
    # Load JSON data from the file
    with open(json_file_path, 'r') as f:
        data = json.load(f)

    # Prepare your CSV data
    csv_data = {}
    for item in data["ata_smart_attributes"]["table"]:
        id = item["id"]
        if id == 1:
            csv_data["Column_" + str(1)] = item["value"]
            csv_data["Column_" + str(2)] = item["raw"]["value"]
        if id == 3:
            csv_data["Column_" + str(3)] = item["value"]
            csv_data["Column_" + str(4)] = item["raw"]["value"]
        if id == 4:
            csv_data["Column_" + str(5)] = item["value"]
            csv_data["Column_" + str(6)] = item["raw"]["value"]
        if id == 5:
            csv_data["Column_" + str(7)] = item["value"]
            csv_data["Column_" + str(8)] = item["raw"]["value"]
        if id == 7:
            csv_data["Column_" + str(9)] = item["value"]
            csv_data["Column_" + str(10)] = item["raw"]["value"]
        if id == 9:
            csv_data["Column_" + str(11)] = item["value"]
            csv_data["Column_" + str(12)] = item["raw"]["value"]
        if id == 10:
            csv_data["Column_" + str(13)] = item["value"]
            csv_data["Column_" + str(14)] = item["raw"]["value"]
        if id == 12:
            csv_data["Column_" + str(15)] = item["value"]
            csv_data["Column_" + str(16)] = item["raw"]["value"]
        if id == 192:
            csv_data["Column_" + str(17)] = item["value"]
            csv_data["Column_" + str(18)] = item["raw"]["value"]
        if id == 193:
            csv_data["Column_" + str(19)] = item["value"]
            csv_data["Column_" + str(20)] = item["raw"]["value"]
        if id == 194:
            csv_data["Column_" + str(21)] = item["value"]
            csv_data["Column_" + str(22)] = item["raw"]["value"]
        if id == 197:
            csv_data["Column_" + str(23)] = item["value"]
            csv_data["Column_" + str(24)] = item["raw"]["value"]
        if id == 198:
            csv_data["Column_" + str(25)] = item["value"]
            csv_data["Column_" + str(26)] = item["raw"]["value"]
        if id == 199:
            csv_data["Column_" + str(27)] = item["value"]
            csv_data["Column_" + str(28)] = item["raw"]["value"]

    # Convert dictionary to DataFrame
    df = pd.DataFrame([csv_data])

    # Ensure all expected columns are present, fill with NaN if not
    expected_columns = ['Column_' + str(i) for i in range(0, 28)]
    for col in expected_columns:
        if col not in df.columns:
            df[col] = np.nan

    return df

@app.route('/')
def index():
    return send_file('/app/index.html')  # Serve the index.html file

@app.route('/predict', methods=['POST'])
def predict():
    # Use a predefined device path
    device_path = '/dev/sda'

    # Get SMART data and save it to a file
    get_smart_data(device_path)

    # Convert SMART data to DataFrame
    df = convert_to_csv_format('/predictt/smart_data.json')
    
    # Use SimpleImputer to fill missing values
    if "Column_1" not in df.columns or "Column_2" not in df.columns:
        df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)
    else:
        df_imputed = df
    if "Column_3" not in df.columns or "Column_4" not in df.columns:
        df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)
    else:
        df_imputed = df
    if "Column_5" not in df.columns or "Column_6" not in df.columns:
        df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)
    else:
        df_imputed = df
    if "Column_7" not in df.columns or "Column_8" not in df.columns:
        df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)
    else:
        df_imputed = df
    if "Column_9" not in df.columns or "Column_10" not in df.columns:
        df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)
    else:
        df_imputed = df
    if "Column_11" not in df.columns or "Column_12" not in df.columns:
        df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)
    else:
        df_imputed = df
    if "Column_13" not in df.columns or "Column_14" not in df.columns:
        df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)
    else:
        df_imputed = df
    if "Column_15" not in df.columns or "Column_16" not in df.columns:
        df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)
    else:
        df_imputed = df
    if "Column_17" not in df.columns or "Column_18" not in df.columns:
        df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)
    else:
        df_imputed = df
    if "Column_19" not in df.columns or "Column_20" not in df.columns:
        df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)
    else:
        df_imputed = df
    if "Column_21" not in df.columns or "Column_22" not in df.columns:
        df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)
    else:
        df_imputed = df
    if "Column_23" not in df.columns or "Column_24" not in df.columns:
        df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)
    else:
        df_imputed = df
    if "Column_25" not in df.columns or "Column_26" not in df.columns:
        df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)
    else:
        df_imputed = df
    if "Column_27" not in df.columns or "Column_28" not in df.columns:
        df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)
    else:
        df_imputed = df

    # Sort the DataFrame columns
    df_imputed = df_imputed.sort_index(axis=1)

    # Set the display options
    pd.set_option('display.max_columns', None)  # or 1000
    pd.set_option('display.max_rows', None)  # or 1000
    pd.set_option('display.max_colwidth', None)  # or 199

    # Extract the numbers from the column names, convert to integer, and sort
    df_imputed = df_imputed.reindex(sorted(df_imputed.columns, key=lambda x: int(x.split('_')[1])), axis=1)
    
    # Make prediction
    prediction = model.predict(df_imputed)

    # Return prediction
    return jsonify(prediction.tolist())

if __name__ == '__main__':
    app.run(debug=True)