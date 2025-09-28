import os
import logging
from flask import Flask, jsonify, request

#basic logging
logging.basicConfig(
        level=logging.INFO,
        format = '%(asctime)s %(levelname)s %(message)s'
        )
logger = logging.getLogger(__name__)

app = Flask(__name__)

#samle healthcare data
PATIENTS = [
        {"id": "p1", "name": "Jane Doe"},
        {"id": "p2", "name": "John Doe"}
        ]

def validate_patient(p):
    """unit test validator"""
    return bool(p) and bool(p.get("id")) and bool(p.get("name"))

@app.get("/health")
def health():
    return jsonify({
        "status": "ok",
        "version": os.getenv("APP_VERSION", "dev")
        })

@app.get("/patients")
def list_patients():
    return jsonify(PATIENTS)

@app.post("/patients")
def create_patient():
    data = request.get_json(force=True, silent-True) or {}
    if not validate_patient(data):
        return jsonify({"error": "invalid payload"}), 400
    PATIENTS.append({"id": data["id"], "name": data["name"]})
    logger.info("patient_created id=%s", data["id"]) # in container logs
    return jsonify({"created": data["id"]}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 8080)))

