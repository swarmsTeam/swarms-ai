from flask import Flask, jsonify, request
import pandas as pd
from utilities import rating_pipeline

app = Flask(__name__)

@app.post('/sentiment')
def sentiment():
    # Check if the input is JSON or CSV
    if request.content_type == 'application/json':
        data = pd.DataFrame(request.json)
    elif 'csv' in request.content_type:
        data = pd.read_csv(request.files['file'])
    else:
        return jsonify({'error': 'Unsupported content type, use JSON or CSV.'}), 400

    # Ensure 'comments' and 'event_id' columns exist
    if 'comments' not in data.columns or 'event_id' not in data.columns:
        return jsonify({'error': 'Missing required columns: comments, event_id'}), 400

    # Get the overall rating for each event_id
    try:
        ratings = rating_pipeline(data, 'comments', 'event_id')
        result = ratings.to_dict()
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
