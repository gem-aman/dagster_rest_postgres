from flask import Flask, jsonify

app = Flask(__name__)

# Sample employee records
employees = [
    {"id": 1, "name": "Alice", "department": "Engineering"},
    {"id": 2, "name": "Bob", "department": "Marketing"},
    {"id": 3, "name": "Charlie", "department": "Sales"},
    {"id": 4, "name": "David", "department": "HR"},
    {"id": 5, "name": "Eve", "department": "Finance"},
    {"id": 6, "name": "Frank", "department": "Engineering"},
    {"id": 7, "name": "Grace", "department": "Marketing"},
    {"id": 8, "name": "Hannah", "department": "Sales"},
    {"id": 9, "name": "Ian", "department": "HR"},
    {"id": 10, "name": "Judy", "department": "Finance"},
    {"id": 11, "name": "Karen", "department": "Staff"},
]

@app.route('/employees', methods=['GET'])
def get_employees():
    return jsonify(employees)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
