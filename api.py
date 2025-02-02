from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Enable CORS globally

# Load the JSON data
with open('q-vercel-python.json', 'r') as f:
    data = json.load(f)

@app.route('/api', methods=['GET'])
def get_marks():
    # Get the list of names from the query parameters
    names = request.args.getlist('name')

    try:
        # Find marks for each name in the list and calculate their sum
        total_marks = 0
        missing_names = []

        for name in names:
            marks = next((item['marks'] for item in data if item['name'] == name), None)
            if marks is not None:
                total_marks += marks
            else:
                missing_names.append(name)

        # Get the current date and time
        current_datetime = datetime.now().strftime("%A, %B %d, %Y, %I %p %Z")

        # If any names are not found, include them in the response
        if missing_names:
            return jsonify({
                "error": "Some names not found",
                "missing_names": missing_names,
                "total_marks": total_marks,
                "current_date": current_datetime
            }), 404

        return jsonify({
            "total_marks": total_marks,
            "current_date": current_datetime
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
