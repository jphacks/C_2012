import cv2
import json
from pathlib import Path
from pdf2image import convert_from_path
from PIL import Image, ImageDraw, ImageFont


def load_files():
    # jsonファイルを開く
    json_open = open('json/sample_json.json', 'r')
    # jsonファイルの読み込み
    json_load = json.load(json_open)

    husband_last_name = json_load['husband']['last_name']
    husband_last_name_kana = json_load['husband']['last_name_kana']
    husband_first_name = json_load['husband']['first_name']
    husband_first_name_kana = json_load['husband']['first_name_kana']
    husband_birth_year = json_load['husband']['birth_day']['year']
    husband_birth_month = json_load['husband']['birth_day']['month']
    husband_birth_day = json_load['husband']['birth_day']['day']
    husband_address_first = json_load['husband']['address']['address_first']
    husband_address_banchi = json_load['husband']['address']['address_banchi']
    husband_address_ban = json_load['husband']['address']['address_ban']
    husband_address_gou = json_load['husband']['address']['address_gou']

    wife_last_name = json_load['wife']['last_name']
    wife_last_name_kana = json_load['wife']['last_name_kana']
    wife_first_name = json_load['wife']['first_name']
    wife_first_name_kana = json_load['wife']['first_name_kana']
    wife_birth_year = json_load['wife']['birth_day']['year']
    wife_birth_month = json_load['wife']['birth_day']['month']
    wife_birth_day = json_load['wife']['birth_day']['day']
    wife_address_first = json_load['wife']['address']['address_first']
    wife_address_banchi = json_load['wife']['address']['address_banchi']
    wife_address_ban = json_load['wife']['address']['address_ban']
    wife_address_gou = json_load['wife']['address']['address_gou']

    return husband_last_name, husband_last_name_kana, husband_first_name, husband_first_name_kana, husband_birth_year, husband_birth_month, husband_birth_day, husband_address_first, husband_address_banchi, husband_address_ban, husband_address_gou, wife_last_name, wife_last_name_kana, wife_first_name, wife_first_name_kana, wife_birth_year, wife_birth_month, wife_birth_day, wife_address_first, wife_address_banchi, wife_address_ban, wife_address_gou


def create_text_img(text, label):
    global text_img
    # フォントの読み込み
    fnt = ImageFont.truetype('font/ipaexg.ttf', 500)
    # Imageインスタンスを生成
    text_img = Image.new('RGBA', (500 * len(text or " "), 500))
    # img上のImageDrawインスタンスを生成
    draw = ImageDraw.Draw(text_img)
    draw.text((0, 0), text, font=fnt, fill='black')
    text_img.save('images/{}.png'.format(label))
    text_img = cv2.imread('images/{}.png'.format(label), -1)

    height, width = text_img.shape[:2]

    return text_img, height, width

# 文字画像の縮小
def resize_img(label, height, width):
    # 文字画像の読み込み
    original_img = Image.open('images/{}.png'.format(label))
    # width*heightに縮小する
    original_img.thumbnail((width, height), Image.ANTIALIAS)
    # 保存
    original_img.save('images/resized_{}.png'.format(label))
    # 縮小した文字のpngファイルをアルファチャンネル込みで読み込む
    resized_img = cv2.imread('images/resized_{}.png'.format(label), -1)

    resized_height, resized_width = resized_img.shape[:2]

    return resized_img, resized_height, resized_width


# PDFファイルのパスを格納する
def make_path():
    pdf_file = Path('images/format/format.pdf')
    img_path = Path('images')
    return pdf_file, img_path

# 婚姻届のpdfをpngに変換する
def pdf_image(pdf_file, img_path, fmt='png', dpi=200):
    # pdf_file, img_pathをPathにする
    pdf_path = Path(pdf_file)
    image_dir = Path(img_path)
    # PDFをImageに変換
    pages = convert_from_path(pdf_path, dpi)
    # 画像ファイルを１ページずつ保存
    for i, page in enumerate(pages):
        # 作成するpngファイル名を'renamed_format.png'に指定する
        file_name = 'renamed_{}.{}'.format(pdf_path.stem, fmt)
        image_path = image_dir / file_name
        page.save(image_path, fmt)
    # 生成したpngファイル'renamed_format.png'を読み込む
    base_img = cv2.imread('images/renamed_format.png')

    return base_img

# 座標を与えて印鑑を合成する関数
def combine(x1, y1, x2, y2, text_img):
    base_img[y1:y2, x1:x2] = base_img[y1:y2, x1:x2] \
        * (1 - text_img[:, :, 3:] / 255) + text_img[:, :, :3] \
        * (text_img[:, :, 3:] / 255)

    return base_img


def save_pdf(base_img):
    # pngファイル'result_tmp.png'を生成
    cv2.imwrite('images/result_tmp.png', base_img)
    # pdfファイル'result.pdf'を生成
    pil_img = Image.open('images/result_tmp.png', 'r')
    pil_img.save('images/result_tmp.pdf', 'PDF')


if __name__ == '__main__':
    husband_last_name, husband_last_name_kana, husband_first_name, husband_first_name_kana, husband_birth_year, husband_birth_month, husband_birth_day, husband_address_first, husband_address_banchi, husband_address_ban, husband_address_gou, wife_last_name, wife_last_name_kana, wife_first_name, wife_first_name_kana, wife_birth_year, wife_birth_month, wife_birth_day, wife_address_first, wife_address_banchi, wife_address_ban, wife_address_gou = load_files()

    husband_last_name_img, husband_last_name_height, husband_last_name_width = create_text_img(
        husband_last_name, 'husband_last_name')
    husband_last_name_kana_img, husband_last_name_kana_height, husband_last_name_kana_width = create_text_img(
        husband_last_name_kana, 'husband_last_name_kana')
    husband_first_name_img, husband_first_name_height, husband_first_name_width = create_text_img(
        husband_first_name, 'husband_first_name')
    husband_first_name_kana_img, husband_first_name_kana_height, husband_first_name_kana_width = create_text_img(
        husband_first_name_kana, 'husband_first_name_kana')
    husband_birth_year_img, husband_birth_year_height, husband_birth_year_width = create_text_img(
        husband_birth_year, 'husband_birth_year')
    husband_birth_month_img, husband_birth_month_height, husband_birth_month_width = create_text_img(
        husband_birth_month, 'husband_birth_month')
    husband_birth_day_img, husband_birth_day_height, husband_birth_day_width = create_text_img(
        husband_birth_day, 'husband_birth_day')
    husband_address_first_img, husband_address_first_height, husband_address_first_width = create_text_img(
        husband_address_first, 'husband_address_first')
    husband_address_banchi_img, husband_address_banchi_height, husband_address_banchi_width = create_text_img(
        husband_address_banchi, 'husband_address_banchi')
    husband_address_ban_img, husband_address_ban_height, husband_address_ban_width = create_text_img(
        husband_address_ban, 'husband_address_ban')
    husband_address_gou_img, husband_address_gou_height, husband_address_gou_width = create_text_img(
        husband_address_gou, 'husband_address_gou')

    wife_last_name_img, wife_last_name_height, wife_last_name_width = create_text_img(
        wife_last_name, 'wife_last_name')
    wife_last_name_kana_img, wife_last_name_kana_height, wife_last_name_kana_width = create_text_img(
        wife_last_name_kana, 'wife_last_name_kana')
    wife_first_name_img, wife_first_name_height, wife_first_name_width = create_text_img(
        wife_first_name, 'wife_first_name')
    wife_first_name_kana_img, wife_first_name_kana_height, wife_first_name_kana_width = create_text_img(
        wife_first_name_kana, 'wife_first_name_kana')
    wife_birth_year_img, wife_birth_year_height, wife_birth_year_width = create_text_img(
        wife_birth_year, 'wife_birth_year')
    wife_birth_month_img, wife_birth_month_height, wife_birth_month_width = create_text_img(
        wife_birth_month, 'wife_birth_month')
    wife_birth_day_img, wife_birth_day_height, wife_birth_day_width = create_text_img(
        wife_birth_day, 'wife_birth_day')
    wife_address_first_img, wife_address_first_height, wife_address_first_width = create_text_img(
        wife_address_first, 'wife_address_first')
    wife_address_banchi_img, wife_address_banchi_height, wife_address_banchi_width = create_text_img(
        wife_address_banchi, 'wife_address_banchi')
    wife_address_ban_img, wife_address_ban_height, wife_address_ban_width = create_text_img(
        wife_address_ban, 'wife_address_ban')
    wife_address_gou_img, wife_address_gou_height, wife_address_gou_width = create_text_img(
        wife_address_gou, 'wife_address_gou')

    resized_husband_last_name_img, resized_husband_last_name_height, resized_husband_last_name_width = resize_img(
        'husband_last_name', 60, min(husband_last_name_width, 200))
    resized_husband_last_name_kana_img, resized_husband_last_name_kana_height, resized_husband_last_name_kana_width = resize_img(
        'husband_last_name_kana', 30, min(husband_last_name_kana_width, 200))
    resized_husband_first_name_img, resized_husband_first_name_height, resized_husband_first_name_width = resize_img(
        'husband_first_name', 60, min(husband_first_name_width, 200))
    resized_husband_first_name_kana_img, resized_husband_first_name_kana_height, resized_husband_first_name_kana_width = resize_img(
        'husband_first_name_kana', 30, min(husband_first_name_kana_width, 200))
    resized_husband_birth_year_img, resized_husband_birth_year_height, resized_husband_birth_year_width = resize_img(
        'husband_birth_year', 35, min(husband_birth_year_width, 190))
    resized_husband_birth_month_img, resized_husband_birth_month_height, resized_husband_birth_month_width = resize_img(
        'husband_birth_month', 35, min(husband_birth_month_width, 80))
    resized_husband_birth_day_img, resized_husband_birth_day_height, resized_husband_birth_day_width = resize_img(
        'husband_birth_day', 35, min(husband_birth_day_width, 80))
    resized_husband_address_first_img, resized_husband_address_first_height, resized_husband_address_first_width = resize_img(
        'husband_address_first', 40, min(husband_address_first_width, 460))
    resized_husband_address_ban_img, resized_husband_address_ban_height, resized_husband_address_ban_width = resize_img(
        'husband_address_ban', 40, min(husband_address_ban_width, 190))
    resized_husband_address_banchi_img, resized_husband_address_banchi_height, resized_husband_address_banchi_width = resize_img(
        'husband_address_banchi', 40, min(husband_address_banchi_width, 190))
    resized_husband_address_gou_img, resized_husband_address_gou_height, resized_husband_address_gou_width = resize_img(
        'husband_address_gou', 40, min(husband_address_gou_width, 190))

    resized_wife_last_name_img, resized_wife_last_name_height, resized_wife_last_name_width = resize_img(
        'wife_last_name', 60, min(wife_last_name_width, 200))
    resized_wife_last_name_kana_img, resized_wife_last_name_kana_height, resized_wife_last_name_kana_width = resize_img(
        'wife_last_name_kana', 30, min(wife_last_name_kana_width, 200))
    resized_wife_first_name_img, resized_wife_first_name_height, resized_wife_first_name_width = resize_img(
        'wife_first_name', 60, min(wife_first_name_width, 200))
    resized_wife_first_name_kana_img, resized_wife_first_name_kana_height, resized_wife_first_name_kana_width = resize_img(
        'wife_first_name_kana', 30, min(wife_first_name_kana_width, 200))
    resized_wife_birth_year_img, resized_wife_birth_year_height, resized_wife_birth_year_width = resize_img(
        'wife_birth_year', 35, min(wife_birth_year_width, 190))
    resized_wife_birth_month_img, resized_wife_birth_month_height, resized_wife_birth_month_width = resize_img(
        'wife_birth_month', 35, min(wife_birth_month_width, 80))
    resized_wife_birth_day_img, resized_wife_birth_day_height, resized_wife_birth_day_width = resize_img(
        'wife_birth_day', 35, min(wife_birth_day_width, 80))
    resized_wife_address_first_img, resized_wife_address_first_height, resized_wife_address_first_width = resize_img(
        'wife_address_first', 40, min(wife_address_first_width, 460))
    resized_wife_address_ban_img, resized_wife_address_ban_height, resized_wife_address_ban_width = resize_img(
        'wife_address_ban', 40, min(wife_address_ban_width, 190))
    resized_wife_address_banchi_img, resized_wife_address_banchi_height, resized_wife_address_banchi_width = resize_img(
        'wife_address_banchi', 40, min(wife_address_banchi_width, 190))
    resized_wife_address_gou_img, resized_wife_address_gou_height, resized_wife_address_gou_width = resize_img(
        'wife_address_gou', 40, min(wife_address_gou_width, 190))

    pdf_file, img_path = make_path()
    base_img = pdf_image(pdf_file, img_path)

    combine(560 - resized_husband_last_name_width // 2, 570 - resized_husband_last_name_height // 2, 560 - resized_husband_last_name_width // 2 +
            resized_husband_last_name_width, 570 - resized_husband_last_name_height // 2 + resized_husband_last_name_height, resized_husband_last_name_img)
    combine(560 - resized_husband_last_name_kana_width // 2, 500 - resized_husband_last_name_kana_height // 2, 560 - resized_husband_last_name_kana_width // 2 +
            resized_husband_last_name_kana_width, 500 - resized_husband_last_name_kana_height // 2 + resized_husband_last_name_kana_height, resized_husband_last_name_kana_img)
    combine(800 - resized_husband_first_name_width // 2, 570 - resized_husband_first_name_height // 2, 800 - resized_husband_first_name_width // 2 +
            resized_husband_first_name_width, 570 - resized_husband_first_name_height // 2 + resized_husband_first_name_height, resized_husband_first_name_img)
    combine(800 - resized_husband_first_name_kana_width // 2, 500 - resized_husband_first_name_kana_height // 2, 800 - resized_husband_first_name_kana_width // 2 +
            resized_husband_first_name_kana_width, 500 - resized_husband_first_name_kana_height // 2 + resized_husband_first_name_kana_height, resized_husband_first_name_kana_img)
    combine(560 - resized_husband_birth_year_width // 2, 627 - resized_husband_birth_year_height // 2, 560 - resized_husband_birth_year_width // 2 +
            resized_husband_birth_year_width, 627 - resized_husband_birth_year_height // 2 + resized_husband_birth_year_height, resized_husband_birth_year_img)
    combine(700 - resized_husband_birth_month_width // 2, 627 - resized_husband_birth_month_height // 2, 700 - resized_husband_birth_month_width // 2 +
            resized_husband_birth_month_width, 627 - resized_husband_birth_month_height // 2 + resized_husband_birth_month_height, resized_husband_birth_month_img)
    combine(815 - resized_husband_birth_day_width // 2, 627 - resized_husband_birth_day_height // 2, 815 - resized_husband_birth_day_width // 2 +
            resized_husband_birth_day_width, 627 - resized_husband_birth_day_height // 2 + resized_husband_birth_day_height, resized_husband_birth_day_img)
    combine(680 - resized_husband_address_first_width // 2, 680 - resized_husband_address_first_height // 2, 680 - resized_husband_address_first_width // 2 +
            resized_husband_address_first_width, 680 - resized_husband_address_first_height // 2 + resized_husband_address_first_height, resized_husband_address_first_img)
    combine(552 - resized_husband_address_ban_width // 2, 730 - resized_husband_address_ban_height // 2, 552 - resized_husband_address_ban_width // 2 +
            resized_husband_address_ban_width, 730 - resized_husband_address_ban_height // 2 + resized_husband_address_ban_height, resized_husband_address_ban_img)
    combine(552 - resized_husband_address_banchi_width // 2, 730 - resized_husband_address_banchi_height // 2, 552 - resized_husband_address_banchi_width // 2 +
            resized_husband_address_banchi_width, 730 - resized_husband_address_banchi_height // 2 + resized_husband_address_banchi_height, resized_husband_address_banchi_img)
    combine(740 - resized_husband_address_gou_width // 2, 730 - resized_husband_address_gou_height // 2, 740 - resized_husband_address_gou_width // 2 +
            resized_husband_address_gou_width, 730 - resized_husband_address_gou_height // 2 + resized_husband_address_gou_height, resized_husband_address_gou_img)

    combine(1035 - resized_wife_last_name_width // 2, 570 - resized_wife_last_name_height // 2, 1035 - resized_wife_last_name_width // 2 +
            resized_wife_last_name_width, 570 - resized_wife_last_name_height // 2 + resized_wife_last_name_height, resized_wife_last_name_img)
    combine(1035 - resized_wife_last_name_kana_width // 2, 500 - resized_wife_last_name_kana_height // 2, 1035 - resized_wife_last_name_kana_width //
            2 + resized_wife_last_name_width, 500 - resized_wife_last_name_height // 2 + resized_wife_last_name_kana_height, resized_wife_last_name_kana_img)
    combine(1270 - resized_wife_first_name_width // 2, 570 - resized_wife_first_name_height // 2, 1270 - resized_wife_first_name_width // 2 +
            resized_wife_first_name_width, 570 - resized_wife_first_name_height // 2 + resized_wife_first_name_height, resized_wife_first_name_img)
    combine(1270 - resized_wife_first_name_kana_width // 2, 500 - resized_wife_first_name_kana_height // 2, 1270 - resized_wife_first_name_kana_width // 2 +
            resized_wife_first_name_kana_width, 500 - resized_wife_first_name_kana_height // 2 + resized_wife_first_name_kana_height, resized_wife_first_name_kana_img)
    combine(1035 - resized_wife_birth_year_width // 2, 627 - resized_wife_birth_year_height // 2, 1035 - resized_wife_birth_year_width // 2 +
            resized_wife_birth_year_width, 627 - resized_wife_birth_year_height // 2 + resized_wife_birth_year_height, resized_wife_birth_year_img)
    combine(1180 - resized_wife_birth_month_width // 2, 627 - resized_wife_birth_month_height // 2, 1180 - resized_wife_birth_month_width // 2 +
            resized_wife_birth_month_width, 627 - resized_wife_birth_month_height // 2 + resized_wife_birth_month_height, resized_wife_birth_month_img)
    combine(1290 - resized_wife_birth_day_width // 2, 627 - resized_wife_birth_day_height // 2, 1290 - resized_wife_birth_day_width // 2 +
            resized_wife_birth_day_width, 627 - resized_wife_birth_day_height // 2 + resized_wife_birth_day_height, resized_wife_birth_day_img)
    combine(1153 - resized_wife_address_first_width // 2, 680 - resized_wife_address_first_height // 2, 1153 - resized_wife_address_first_width // 2 +
            resized_wife_address_first_width, 680 - resized_wife_address_first_height // 2 + resized_wife_address_first_height, resized_wife_address_first_img)
    combine(1028 - resized_wife_address_ban_width // 2, 730 - resized_wife_address_ban_height // 2, 1028 - resized_wife_address_ban_width // 2 +
            resized_wife_address_ban_width, 730 - resized_wife_address_ban_height // 2 + resized_wife_address_ban_height, resized_wife_address_ban_img)
    combine(1028 - resized_wife_address_banchi_width // 2, 730 - resized_wife_address_banchi_height // 2, 1028 - resized_wife_address_banchi_width // 2 +
            resized_wife_address_banchi_width, 730 - resized_wife_address_banchi_height // 2 + resized_wife_address_banchi_height, resized_wife_address_banchi_img)
    combine(1207 - resized_wife_address_gou_width // 2, 730 - resized_wife_address_gou_height // 2, 1207 - resized_wife_address_gou_width // 2 +
            resized_wife_address_gou_width, 730 - resized_wife_address_gou_height // 2 + resized_wife_address_gou_height, resized_wife_address_gou_img)

    save_pdf(base_img)
