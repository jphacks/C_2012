from flask import Flask, render_template, request, session, redirect, url_for
import cv2
import create_stamps
import confirm_pdf
import create_pdf

app = Flask(__name__)

app.secret_key = "aaa"

@app.route('/')
def top():
	# session.init_session()
	return render_template("top.html")

@app.route('/input', methods=['GET', 'POST'])
def input():
	if request.method == 'POST':
		husband_last_name       = request.form.get("husband-last_name")
		husband_first_name      = request.form.get("husband-first_name")
		husband_last_name_kana  = request.form.get("husband-last_name_kana")
		husband_first_name_kana = request.form.get("husband-first_name_kana")
		husband_birth_year      = request.form.get("husband-birth_year")
		husband_birth_month     = request.form.get("husband-birth_month")
		husband_birth_day       = request.form.get("husband-birth_day")
		husband_address_first   = request.form.get("husband-address_first")
		husband_address_banchi  = request.form.get("husband-address_banchi")
		husband_address_ban     = request.form.get("husband-address_ban")
		husband_address_gou     = request.form.get("husband-address_gou")
		wife_last_name          = request.form.get("wife-last_name")
		wife_first_name         = request.form.get("wife-first_name")
		wife_last_name_kana     = request.form.get("wife-last_name_kana")
		wife_first_name_kana    = request.form.get("wife-first_name_kana")
		wife_birth_year         = request.form.get("wife-birth_year")
		wife_birth_month        = request.form.get("wife-birth_month")
		wife_birth_day          = request.form.get("wife-birth_day")
		wife_address_first      = request.form.get("wife-address_first")
		wife_address_banchi     = request.form.get("wife-address_banchi")
		wife_address_ban        = request.form.get("wife-address_ban")
		wife_address_gou        = request.form.get("wife-address_gou")

		session['husband_last_name'] = husband_last_name 
		session['husband_first_name'] = husband_first_name 
		session['husband_last_name_kana'] = husband_last_name_kana 
		session['husband_first_name_kana'] = husband_first_name_kana 
		session['husband_birth_year'] = husband_birth_year 
		session['husband_birth_month'] = husband_birth_month 
		session['husband_birth_day'] = husband_birth_day 
		session['husband_address_first'] = husband_address_first 
		session['husband_address_banchi'] = husband_address_banchi 
		session['husband_address_ban'] = husband_address_ban 
		session['husband_address_gou'] = husband_address_gou 
		session['wife_last_name'] = wife_last_name 
		session['wife_first_name'] = wife_first_name 
		session['wife_last_name_kana'] = wife_last_name_kana 
		session['wife_first_name_kana'] = wife_first_name_kana 
		session['wife_birth_year'] = wife_birth_year 
		session['wife_birth_month'] = wife_birth_month 
		session['wife_birth_day'] = wife_birth_day 
		session['wife_address_first'] = wife_address_first 
		session['wife_address_banchi'] = wife_address_banchi 
		session['wife_address_ban'] = wife_address_ban 
		session['wife_address_gou'] = wife_address_gou 

		confirm_pdf.create(husband_last_name, husband_first_name, husband_last_name_kana, husband_first_name_kana, husband_birth_year, husband_birth_month, husband_birth_day, husband_address_first, husband_address_banchi, husband_address_ban, husband_address_gou, wife_last_name, wife_first_name, wife_last_name_kana, wife_first_name_kana, wife_birth_year, wife_birth_month, wife_birth_day, wife_address_first, wife_address_banchi, wife_address_ban, wife_address_gou)

		return redirect(url_for("confirm_input"))
	else:
		return render_template("input.html")

@app.route('/confirm_input')
def confirm_input():
	return render_template("confirm_input.html")

@app.route('/confirm_stamp')
def confirm_stamp():
	# ディレクトリ直置きはまずいのでココでSession取り出して印鑑画像生成する（Want to do）
	husband_last_name = session['husband_last_name']
	wife_last_name = session['wife_last_name']

	husband_last_name_img = create_stamps.create_last_name(husband_last_name, 'husband')
	husband_last_name_img = create_stamps.create_last_name(wife_last_name, 'wife')
	create_stamps.combine_images('husband')
	create_stamps.combine_images('wife')

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
	husband_stamp_img = create_pdf.resize_image('husband')
	wife_stamp_img = create_pdf.resize_image('wife')
	base_img = create_pdf.load_base_img()
	create_pdf.save_pdf(base_img, husband_stamp_img, wife_stamp_img)
	return render_template("download.html")

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)
