import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from matplotlib.backends.backend_pdf import PdfPages
from pathlib import Path
from pdf2image import convert_from_path

# 印鑑のpngファイルを75*75に縮小する
def resize_image():
  # 印鑑画像の読み込み
  original_img1 = Image.open('images/format/stamp_sample1.png')
  original_img2 = Image.open('images/format/stamp_sample2.png')
  # 75*75に縮小する
  original_img1.thumbnail((75, 75), Image.ANTIALIAS)
  original_img2.thumbnail((75, 75), Image.ANTIALIAS)
  # 保存
  original_img1.save('images/resized_stamp1.png')
  original_img2.save('images/resized_stamp2.png')
  # 縮小した印鑑のpngファイルをアルファチャンネル込みで読み込む
  husband_stamp_img = cv2.imread('images/resized_stamp1.png', -1)
  wife_stamp_img = cv2.imread('images/resized_stamp2.png', -1)
  return husband_stamp_img, wife_stamp_img

# PDFファイルのパスを格納する
def make_path():
  pdf_file = Path('images/format/format_sample.pdf')
  img_path = Path('images')
  return pdf_file, img_path

# 婚姻届のpdfをpngに変換する
def pdf_image(pdf_file, img_path, fmt = 'png', dpi = 200):
  # pdf_file, img_pathをPathにする
  pdf_path = Path(pdf_file)
  image_dir = Path(img_path)
  # PDFをImageに変換
  pages = convert_from_path(pdf_path, dpi)
  # 画像ファイルを１ページずつ保存
  for i, page in enumerate(pages):
    # 作成するpngファイル名を'format_sample_01.png'に指定する
    file_name = '{}_{:02d}.{}'.format(pdf_path.stem, i+1, fmt)
    image_path = image_dir / file_name
    page.save(image_path, fmt)
  # 生成したpngファイル'format_sample_01.png'を読み込む
  base_img = cv2.imread('images/format_sample_01.png')
  return base_img

# 'result.pdf'として保存する
def save_pdf(base_img, husband_stamp_img, wife_stamp_img):
    # 座標を与えて印鑑を合成する関数
    def stamps(x1, y1, x2, y2, stamp_img):
      base_img[y1:y2, x1:x2] = base_img[y1:y2, x1:x2] * (1 - stamp_img[:, :, 3:] / 255) + stamp_img[:, :, :3] * (stamp_img[:, :, 3:] / 255)

    # 夫の印鑑合成
    stamps(1027, 2017, 1102, 2092, husband_stamp_img)
    # 妻の印鑑合成
    stamps(1542, 2017, 1617, 2092, wife_stamp_img)

    # pngファイル'result.png'を生成
    cv2.imwrite('images/result.png', base_img)
    # pdfファイル'result.pdf'を生成
    pil_img = Image.open('images/result.png','r')
    pil_img.save('images/result.pdf', 'PDF')

if __name__ == '__main__':
  husband_stamp_img, wife_stamp_img = resize_image()
  pdf_file, img_path = make_path()
  base_img = pdf_image(pdf_file, img_path)
  save_pdf(base_img, husband_stamp_img, wife_stamp_img)
