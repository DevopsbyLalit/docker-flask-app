from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "🚀 Hello, Lalit! Your first Dockerized Flask App is running!"

@app.route("/about")
def about():
    return "This is a simple beginner project in Docker using Python & Flask."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

