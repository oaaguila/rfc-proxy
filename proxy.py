from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

app = Flask(__name__)
CORS(app)

API_URL = "https://3.129.253.159/api/RFC/consulta_rfc"
API_KEY = "65e84be33532fb784c48129675f9eff3a682b27168c0ea744b2cf58ee02337c5"

@app.route("/consulta_rfc/<rfc>", methods=["GET"])
def consulta_rfc(rfc):
    rfc = rfc.strip().upper()
    try:
        resp = requests.post(
            API_URL,
            data=json.dumps({"apikey": API_KEY, "rfc": rfc}),
            headers={
                "Content-Type": "application/json",
                "accept": "text/plain"
            },
            verify=False,
            timeout=10
        )
        try:
            return jsonify(resp.json())
        except Exception:
            return resp.text, resp.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
