from flask import Flask, render_template, request, session, redirect, url_for
import cv2
import create_stamps.create_stamps as create_stamps

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		# sessionに必要事項を保存

		# pdf生成

		# 印鑑生成もここ？
		# content = request.form['content'] # ex. content = '{"husband": {"last_name": "佐藤"},"wife": {"last_name": "田中"}}'
		# husband_last_name, wife_last_name = create_stamps.load_files(content)
		# husband_last_name_img = create_stamps.create_last_name(husband_last_name, 'husband')
		# husband_last_name_img = create_stamps.create_last_name(wife_last_name, 'wife')
		# create_stamps.combine_images('husband')
		# create_stamps.combine_images('wife')
		return redirect(url_for("confirm_stamps"))
	else:
		return render_template("index.html", message="Hello nikoha!")

@app.route('/confirm_stamps')
def confirm_stamps():
	# ディレクトリ直置きはまずいのでココでSession取り出して印鑑画像生成する（Want to do）
	return render_template("confirm_stamps.html")

@app.route('/video', methods=['GET', 'POST'])
def video():
	if request.method == 'POST':
		# pdf（必要事項、印鑑、写真） 作成処理？
		return # redirect(url_for("NEXT_PAGE"))
	else:
		return render_template("video.html")

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)