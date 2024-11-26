from flask import Flask, render_template, request, jsonify
import nmap
import os

os.environ["PATH"] += os.pathsep +  r"C:\Program Files (x86)\Nmap"
app = Flask(__name__)
nm = nmap.PortScanner()


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/scan", methods=["POST"])
def scan_network():
    target = request.form.get("target")
    if not target:
        return jsonify({"error": "No target provided"}), 400

    try:
        scan_result = nm.scan(hosts=target, arguments='-F')
        return render_template("results.html", scan_result=scan_result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
