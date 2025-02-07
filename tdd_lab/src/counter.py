"""
Counter API Implementation
"""
from flask import Flask, jsonify
from . import status

app = Flask(__name__)

COUNTERS = {}



def counter_exists(name):
    """Check if counter exists"""
    return name in COUNTERS 
@app.route('/counters/<name>', methods=['POST'])
def create_counter(name):
  """Create a counter"""
  if counter_exists(name):
      return jsonify({"error": f"Counter {name} already exists"}), status.HTTP_409_CONFLICT
  COUNTERS[name] = 0
  return jsonify({name: COUNTERS[name]}), status.HTTP_201_CREATED

@app.route('/counters/<name>', methods=['GET'])
def get_counter(name):
    """Get the value of a counter"""
    if not counter_exists(name):
        return jsonify({"error": f"Counter {name} not found"}), status.HTTP_404_NOT_FOUND
    if counter_exists(name):
        return jsonify({name: COUNTERS[name]}), status.HTTP_201_CREATED    
    return jsonify({name: COUNTERS[name]}), status.HTTP_200_OK
    



@app.route('/counters/<name>', methods=['POST'])
def create_new_counter(name):
    """Create a counter"""
    if counter_exists(name):
        return jsonify({"error": f"Counter {name} already exists"}), status.HTTP_409_CONFLICT
    COUNTERS[name] = 0
    return jsonify({name: COUNTERS[name]}), status.HTTP_201_CREATED

@app.route('/counters/<name>', methods=['DELETE'])
def delete_counter(name):
    """Delete an existing counter"""
    if not counter_exists(name):
        return jsonify({"error": f"Counter {name} not found"}), status.HTTP_404_NOT_FOUND
    del COUNTERS[name]
    return '', status.HTTP_204_NO_CONTENT

def reset_counters():
    """Helper function to reset all counters"""
    global COUNTERS
    for key in COUNTERS:
        COUNTERS[key] = 0
        
@app.route('/counters/reset', methods=['POST'])
def reset_all_counters():
    """Resets all counters using helper function"""
    reset_counters()
    return jsonify({"message": "All counters reset"}), status.HTTP_200_OK

# Evan Hollingshead - 5
@app.route('/counters/<name>', methods=['PUT'])
def increment_counter(name):
    """Increment a counter"""
    if not counter_exists(name):
        return jsonify({"error": f"Counter {name} not found"}), status.HTTP_404_NOT_FOUND
    COUNTERS[name] += 1
    return jsonify({name: COUNTERS[name]}), status.HTTP_200_OK
