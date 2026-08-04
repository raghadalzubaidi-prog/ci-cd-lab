from flask import Flask

app = Flask(__name__)

return "v2 - hello from CI"

@app.route("/")
def home():
    return VERSION

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)