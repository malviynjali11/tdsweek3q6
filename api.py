import json
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(_name_)
CORS(app)

# Load student marks from the JSON file (list of dictionaries)
with open("api/students.json", "r") as f:
    student_marks = json.load(f)

# Helper function to find marks for a given name
def get_marks_for_name(name):
    for student in student_marks:
        if student["name"] == name:
            return student["marks"]
    return None  # Return None if name is not found

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the Student Marks API!"})

@app.route("/api", methods=["GET"])
def get_marks():
    names = request.args.getlist("name")  # Get 'name' query parameters as a list
    marks = [get_marks_for_name(name) for name in names]  # Fetch marks for each name
    return jsonify({"marks": marks})

if __name__ == "_main_":
    app.run(debug=True)