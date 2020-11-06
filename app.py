from flask import Flask, render_template, request, session
import cv2

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", message="Hello nikoha!")

@app.route('/input')
def input():
    return render_template("input.html")

@app.route('/video')
def video():
    return render_template("video.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
