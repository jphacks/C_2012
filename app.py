from flask import Flask, render_template, request, session, redirect, url_for
import cv2
import create_stamps.create_stamps as create_stamps

app = Flask(__name__)

@app.route('/top')
def top():
	return render_template("top.html")

@app.route('/confirm_input')
def confirm_input():
	return render_template("confirm_input.html")

@app.route('/confirm_stamp')
def confirm_stamp():
	# ディレクトリ直置きはまずいのでココでSession取り出して印鑑画像生成する（Want to do）
	return render_template("confirm_stamp.html")

@app.route('/smilecamera', methods=['GET', 'POST'])
def video():
	if request.method == 'POST':
		# pdf（必要事項、印鑑、写真） 作成処理？
		return # redirect(url_for("NEXT_PAGE"))
	else:
		return render_template("smilecamera.html")

@app.route('/stamp')
def stamp():
	return render_template("stamp.html")

@app.route('/download')
def download():
	return render_template("download.html")

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)
