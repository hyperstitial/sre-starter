from flask import Flask, Response
import time
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)
REQUESTS = Counter('app_requests_total', 'Total requests')
LATENCY  = Histogram('app_request_latency_seconds', 'Request latency (s)')

@app.route("/")
def index():
    start = time.time()
    time.sleep(0.05)  # simulate work
    REQUESTS.inc()
    LATENCY.observe(time.time() - start)
    return "ok\n"

@app.route("/healthz")
def healthz():
    return "ok\n"

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
