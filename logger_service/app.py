from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

logging.basicConfig(filename='scan_results.log', level=logging.INFO, format='%(asctime)s - %(message)s')

@app.route('/log', methods=['POST'])
def log_results():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    try:
        logging.info(data)
        return jsonify({"message": "Scan results logged successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
