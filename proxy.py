from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

app = Flask(__name__)
CORS(app)

API_KEY = "b5a3ddc5-7da1f41d"

@app.route("/consulta_rfc/<rfc>", methods=["GET"])
def consulta_rfc(rfc):
    rfc = rfc.strip().upper()
    try:
        resp = requests.get(
            f"https://satpi.mx/api/search/{rfc}",
            headers={"x-api-key": API_KEY},
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
