from flask import Flask, render_template, request, session
import cv2
import create_stamps.create_stamps as create_stamps

app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html", message="Hello nikoha!")

@app.route('/video')
def video():
	return render_template("video.html")

@app.route('/confirm_stamps')
def confirm_stamps():
  husband_last_name, wife_last_name = create_stamps.load_files('{"husband": {"last_name": "佐藤"},"wife": {"last_name": "田中"}}')
  husband_last_name_img = create_stamps.create_last_name(husband_last_name, 'husband')
  husband_last_name_img = create_stamps.create_last_name(wife_last_name, 'wife')
  create_stamps.combine_images('husband')
  create_stamps.combine_images('wife')
  return render_template("confirm_stamps.html", image="image")

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)