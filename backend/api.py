import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, request, jsonify
from flask_cors import CORS
from agents.orchestrator import orchestrator  # Now should work

app = Flask(__name__)
CORS(app)

@app.route('/run-agent', methods=['POST'])
def run_agent():
    data = request.json
    goal = data.get('goal', '')
    if not goal:
        return jsonify({'error': 'Goal is required'}), 400
    result = orchestrator(goal)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
