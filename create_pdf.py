import json
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

def load_files():
    # jsonファイルの読み込み
    json_open = open('json/sample_json.json', 'r')
    json_load = json.load(json_open)

    husband_last_name = json_load['husband']['last_name']
    wife_last_name = json_load['wife']['last_name']

    return husband_last_name, wife_last_name

def create_last_name(last_name, whose_name):
    # フォントの読み込み
    fnt = ImageFont.truetype('font/ipamjm.ttf', 500)
    # Imageインスタンスを生成
    last_name_img = Image.new('RGBA',(500, 500 * len(last_name)))
    # img上のImageDrawインスタンスを生成
    draw = ImageDraw.Draw(last_name_img)
    # fontを指定
    for i in range(len(last_name)):
        draw.text((0, 500 * i), last_name[i], font = fnt, fill = 'red')
    last_name_img.save('images/{}_last_name.png'.format(whose_name))

    return last_name_img

def combine_images(whose_name):
    global base_img
    # 印鑑の外枠の読み込み
    base_img = cv2.imread('images/format/stamps_base.png', -1)
    # RGBへの変換
    base_img = cv2.cvtColor(base_img, cv2.COLOR_BGR2RGB)

    # 名字の文字画像の読み込み
    last_name_img = cv2.imread('images/{}_last_name.png'.format(whose_name), -1)
    # RGBへの変換
    last_name_img = cv2.cvtColor(last_name_img, cv2.COLOR_BGRA2RGBA)
    # 112*224に縮小する
    resized_last_name_img = cv2.resize(last_name_img, (112, 224))

    # 座標を与えて印鑑を生成する
    def combine(x1, y1, x2, y2):
        base_img[y1:y2, x1:x2] = base_img[y1:y2, x1:x2]\
         * (1 - resized_last_name_img[:, :, 3:] / 255)\
         + resized_last_name_img[:, :, :3] * (resized_last_name_img[:, :, 3:] / 255)

    # 印鑑合成
    combine(111, 55, 223, 279)

    # pngファイル'{}_last_name_img.png'を生成
    cv2.imwrite('images/{}_last_name_img.png'.format(whose_name), base_img)

    # 保存したものを読み込み→変換→上書き保存 (((汚い!!!)))
    base_img = cv2.imread('images/{}_last_name_img.png'.format(whose_name), -1)
    base_img = cv2.cvtColor(base_img, cv2.COLOR_BGRA2RGBA)
    # 白色のみTrueを返し，Alphaを0にする
    base_img[:, :, 3] = np.where(np.all(base_img == 255, axis = -1), 0, 255)
    cv2.imwrite('images/{}_last_name_img.png'.format(whose_name), base_img)


if __name__ == '__main__':
    husband_last_name, wife_last_name = load_files()
    husband_last_name_img = create_last_name(husband_last_name, 'husband')
    husband_last_name_img = create_last_name(wife_last_name, 'wife')
    combine_images('husband')
    combine_images('wife')
