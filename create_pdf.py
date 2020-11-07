import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from matplotlib.backends.backend_pdf import PdfPages
from pathlib import Path
from pdf2image import convert_from_path

# 印鑑のpngファイルを75*75に縮小する
def resize_image(whose_name):
  # 印鑑画像の読み込み
  original_img = Image.open('../#15_create_stamps/images/{}_last_name_img.png'.format(whose_name))
  # 75*75に縮小する
  original_img.thumbnail((75, 75), Image.ANTIALIAS)
  # 保存
  original_img.save('images/resized_{}_name.png'.format(whose_name))
  # 縮小した印鑑のpngファイルをアルファチャンネル込みで読み込む
  resized_name_img = cv2.imread('images/resized_{}_name.png'.format(whose_name), -1)
  return resized_name_img

def load_base_img():
    base_img = cv2.imread('../#16_confirm_pdf/images/result_tmp.png')

    return base_img

# 'result.pdf'として保存する
def save_pdf(base_img, husband_stamp_img, wife_stamp_img):
    # 座標を与えて画像を合成する
    def stamps(x1, y1, x2, y2, stamp_img):
      base_img[y1:y2, x1:x2] = base_img[y1:y2, x1:x2] \
      * (1 - stamp_img[:, :, 3:] / 255) + stamp_img[:, :, :3] \
      * (stamp_img[:, :, 3:] / 255)

    # 夫の印鑑合成
    stamps(837, 1770, 837 + 75, 1770 + 75, husband_stamp_img)
    # 妻の印鑑合成
    stamps(1310, 1770, 1310 + 75, 1770 + 75, wife_stamp_img)

    # 写真サイズを取得(husband_stamp_imgは例)
    picture_height, picture_width = husband_stamp_img.shape[:2]

    # 写真の合成(husband_stamp_imgは例)
    stamps(2088 - picture_width//2, 1402 - picture_height//2, 2088 - picture_width//2 + picture_width, 1402 - picture_height//2 + picture_height, husband_stamp_img)

    # pngファイル'result.png'を生成
    cv2.imwrite('images/result.png', base_img)
    # pdfファイル'result.pdf'を生成
    pil_img = Image.open('images/result.png','r')
    pil_img.save('images/result.pdf', 'PDF')

if __name__ == '__main__':
  husband_stamp_img = resize_image('husband')
  wife_stamp_img = resize_image('wife')
  base_img = load_base_img()
  save_pdf(base_img, husband_stamp_img, wife_stamp_img)
