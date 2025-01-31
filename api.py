from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Load the JSON data
with open('q-vercel-python.json', 'r') as f:
    data = json.load(f)

@app.route('/api', methods=['GET'])
def get_marks():
    # Get query parameters X and Y
    x = request.args.get('x')
    y = request.args.get('y')

    try:
        # Check if data is a list or dictionary
        if isinstance(data, list):
            # Search for x and y in the list
            x_marks = next((item['marks'] for item in data if item['name'] == x), None)
            y_marks = next((item['marks'] for item in data if item['name'] == y), None)
        elif isinstance(data, dict):
            # Use .get() if data is a dictionary
            x_marks = data.get(x)
            y_marks = data.get(y)
        else:
            return jsonify({"error": "Invalid JSON structure"}), 500

        # Handle cases where names are not found
        if x_marks is None or y_marks is None:
            return jsonify({"error": "One or both names not found"}), 404

        return jsonify({"marks": [x_marks, y_marks]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
